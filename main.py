from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Configuration Base de données
DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    # Mode Local (si tu le lances sur ton PC)
    DB_URL = "sqlite:///./nexus_pay.db"
    engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
else:
    # Mode Production (Render + Neon)
    if DB_URL.startswith("postgres://"):
        DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)
    engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modèles
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    balance = Column(Float, default=0.0)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer)
    type = Column(String)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- ROUTES PAGES ---
@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.get("/admin")
async def read_admin():
    return FileResponse('static/admin.html')

# --- API CLIENT ---
@app.post("/create_account")
async def create_account(name: str, password: str):
    db = SessionLocal()
    new_user = User(name=name, password=password, balance=0.0)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user

@app.post("/login")
async def login(account_id: int, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.id == account_id, User.password == password).first()
    db.close()
    if not user:
        raise HTTPException(status_code=401, detail="Identifiants incorrects")
    return user

@app.post("/deposit")
async def deposit(account_id: int, amount: float):
    db = SessionLocal()
    user = db.query(User).filter(User.id == account_id).first()
    if user:
        user.balance += amount
        db.add(Transaction(account_id=account_id, type="Dépôt", amount=amount))
        db.commit()
        new_balance = user.balance
        db.close()
        return {"new_balance": new_balance}
    db.close()
    raise HTTPException(status_code=404)

@app.post("/withdraw")
async def withdraw(account_id: int, amount: float):
    db = SessionLocal()
    user = db.query(User).filter(User.id == account_id).first()
    if user and user.balance >= amount:
        user.balance -= amount
        db.add(Transaction(account_id=account_id, type="Retrait", amount=amount))
        db.commit()
        new_balance = user.balance
        db.close()
        return {"new_balance": new_balance}
    db.close()
    raise HTTPException(status_code=400, detail="Solde insuffisant")

@app.post("/transfer")
async def transfer(sender_id: int, receiver_id: int, amount: float):
    db = SessionLocal()
    sender = db.query(User).filter(User.id == sender_id).first()
    receiver = db.query(User).filter(User.id == receiver_id).first()
    if sender and receiver and sender.balance >= amount:
        sender.balance -= amount
        receiver.balance += amount
        db.add(Transaction(account_id=sender_id, type=f"Transfert vers #{receiver_id}", amount=amount))
        db.add(Transaction(account_id=receiver_id, type=f"Reçu de #{sender_id}", amount=amount))
        db.commit()
        new_balance = sender.balance
        db.close()
        return {"new_balance": new_balance}
    db.close()
    raise HTTPException(status_code=400, detail="Transfert impossible")

# --- API ADMIN SÉCURISÉE ---
@app.get("/api/admin/accounts")
async def admin_accounts(password: str = Query(...)):
    if password != "Hacker":
        raise HTTPException(status_code=403, detail="Accès interdit")
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

@app.get("/api/admin/history")
async def admin_history(password: str = Query(...)):
    if password != "Hacker":
        raise HTTPException(status_code=403, detail="Accès interdit")
    db = SessionLocal()
    history = db.query(Transaction).order_by(Transaction.timestamp.desc()).all()
    db.close()
    return history

# Montage des fichiers statiques

app.mount("/static", StaticFiles(directory="static"), name="static")
