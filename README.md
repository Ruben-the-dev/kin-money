# 💰 Kin-Money 🇨🇩 — Application Simulation Bancaire

**Kin-Money** est une application de simulation bancaire **Full-Stack** conçue pour reproduire les opérations financières essentielles de manière fluide et sécurisée. Elle utilise la puissance de **FastAPI** en backend pour gérer les transactions et une interface **Responsive Design** moderne.

> **Mise à jour majeure** : Le projet utilise désormais une architecture de base de données Cloud (PostgreSQL) pour une persistance des données garantie.

---

## 🌍 Découvrir l'application

Vous pouvez tester l'expérience complète en direct sans aucune installation :

👉 **[Lancer la démo Kin-Money Client](https://kin-money.onrender.com)**
👉 **[Lancer la démo Kin-Money Admin](https://kin-money.onrender.com/admin)**

*La documentation interactive de l'API est disponible ici : [Swagger UI (/docs)](https://kin-money.onrender.com/docs)*

**🔑 Accès Panel Admin (Test) :**
* **Identifiant** : `admin`
* **Mot de passe** : `Hacker`

---

## 🚀 Fonctionnalités Clés

- **💎 Interface Client** : 
    - Création de compte avec génération d'ID unique.
    - Opérations en temps réel : Dépôts, retraits et transferts.
    - Consultation du solde et historique personnel.
- **🛡️ Panel Admin** : 
    - Surveillance globale du système et de la base de données.
    - Consultation de l'historique complet des transactions bancaires.
- **☁️ Persistance Cloud** : 
    - Intégration avec **PostgreSQL** pour conserver les données même après redémarrage.
- **📱 Design Premium** : 
    - Interface en **Dark Mode** optimisée pour Mobile, Tablette et Desktop.

---

## ⚡ Technologies utilisées

Voici les outils et technologies qui propulsent ce projet :

**Backend & Serveur :**
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" />
</p>

**Base de données & Persistance :**
<p align="left">
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Neon-00E599?style=for-the-badge&logo=neon&logoColor=black" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
</p>

**Frontend :**
<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
</p>

---

## ⚙️ Installation Locale

1️⃣ **Cloner le projet**

bash

git clone [https://github.com/Ruben-the-dev/kin-money.git](https://github.com/Ruben-the-dev/kin-money.git)
cd kin-money


2️⃣ Préparer l'environnement

Bash
pip install -r requirements.txt


3️⃣ Lancer le serveur

Bash
uvicorn main:app --reload
👉 http://127.0.0.1:8000

🛡️ Note sur la Sécurité
Le projet utilise des Variables d'Environnement pour sécuriser les accès à la base de données PostgreSQL sur Render. Dans un projet bancaire réel, j'implémente également le hachage des mots de passe (BCrypt) et une authentification via Tokens JWT.

💬 On reste en contact ?
Je réalise ce type de solutions en Freelance. Si vous avez un projet en tête, n'hésitez pas :

💼 LinkedIn : Ruben Mwanza Kankese

📧 Email : rubenthedevs@gmail.com


<p align="center"> <img src="https://komarev.com/ghpvc/?username=Ruben-the-dev&color=blue&style=flat-square&label=VUES+PROFIL" alt="Profile Views" /> </p>
