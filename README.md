# 💰 Kin-Money 🇨🇩 — Application Simulation Bancaire

**Kin-Money** est une application de simulation bancaire **Full-Stack** conçue pour reproduire les opérations financières essentielles de manière fluide et sécurisée. Elle utilise la puissance de **FastAPI** en backend pour gérer les transactions et une interface **Responsive Design** moderne pour l'expérience utilisateur.

---

## 🚀 Fonctionnalités Clés

- **💎 Interface Client** : 
    - Création de compte avec génération d'ID unique.
    - Opérations en temps réel : Dépôts, retraits et transferts.
    - Consultation du solde et historique personnel.
- **🛡️ Panel Admin** : 
    - Surveillance globale du système et de la base de données.
    - Consultation de l'historique complet des transactions bancaires.
- **📱 Design Premium** : 
    - Interface en **Dark Mode** optimisée pour Mobile, Tablette et Desktop.

---

## 🔐 Accès Démonstration & Sécurité

Pour permettre aux recruteurs et aux développeurs de tester l'intégralité des fonctionnalités (Panel Admin), les accès ont été simplifiés :

- **Lien de l'API (Swagger UI)** : [https://kin-money.onrender.com/docs](https://kin-money.onrender.com/docs)
- **Identifiant Admin** : `admin`
- **Mot de passe** : `Hacker`

> [!NOTE]
> **Avertissement de Sécurité** : Le mot de passe a été laissé en clair dans le code et cette documentation à titre **strictement démonstratif**. 
> Dans une application de production, les accès seraient sécurisés par des **Variables d'Environnement** et un système d'authentification par **Tokens JWT**.

---

## 🛠️ Stack Technique

- **Backend** : [Python](https://www.python.org/) & [FastAPI](https://fastapi.tiangolo.com/) (Haute performance)
- **Base de données** : [SQLite](https://www.sqlite.org/) avec l'ORM [SQLAlchemy](https://www.sqlalchemy.org/)
- **Frontend** : HTML5, CSS3 (Variables modernes), JavaScript Vanilla

---

## ⚙️ Installation Locale

    1️⃣ Cloner le projet:
   ```bash
   git clone [https://github.com/Ruben-the-dev/kin-money.git](https://github.com/Ruben-the-dev/kin-money.git)
   cd kin-money
   Installer les dépendances : (Nécessite Python installé)
   
    2️⃣ Installation des dépendances (Crucial)
    Cette étape installe tous les outils nécessaires (FastAPI, SQLAlchemy, Uvicorn, etc.) : pip install -r requirements.txt
   
    3️⃣ Lancement du serveur: uvicorn main:app --reload

    
    🚀 Accès à l'interface
    Une fois le serveur lancé, ouvrez votre navigateur à l'adresse suivante : 👉 http://127.0.0.1:8000/docs

  
  
