# SecureApp 🔐

Application FastAPI sécurisée avec CI/CD, Docker, Trivy et audit de sécurité automatisé

SecureApp est une application FastAPI conçue pour démontrer la mise en place d'un pipeline CI/CD complet incluant :
- Analyse statique du code (Ruff)
- Tests unitaires (pytest)
- Audit de sécurité Python (Bandit + pip-audit)
- Build Docker automatisé
- Scan de vulnérabilités de l'image Docker (Trivy)
- Intégration DevSecOps

Ce projet sert de base pour apprendre et présenter des compétences DevOps / DevSecOps.

---

## 🚀 Fonctionnalités

- API FastAPI simple et extensible
- Validation des données via Pydantic
- Linting automatique avec Ruff
- Tests unitaires avec Pytest
- Audit de sécurité Python (Bandit, pip-audit)
- Build Docker reproductible
- Scan de vulnérabilités CRITIQUES via Trivy
- Pipeline CI/CD complet sur GitHub Actions

---

## 🧱 Architecture du projet

```
SecureApp/
│
├── app/
│   ├── main.py          # Point d'entrée FastAPI
│   ├── routers/         # Routes de l'API
│   └── models/          # Modèles Pydantic
│
├── tests/               # Tests unitaires
│
├── Dockerfile           # Build de l'image
├── requirements.txt     # Dépendances de production
├── requirements-dev.txt # Dépendances de développement
│
└── .github/workflows/
    └── ci-cd.yml        # Pipeline CI/CD complet
```

---

## 🐳 Docker

### Construire l'image

```bash
docker build -t secureapp .
```

### Lancer l'application

```bash
docker run -p 8000:8000 secureapp
```

API disponible sur :

```
http://localhost:8000
```

---

## 🔍 CI/CD — Pipeline GitHub Actions

Le pipeline exécute automatiquement :

### ✔ Linting

```bash
ruff check .
```

### ✔ Tests unitaires

```bash
pytest -v
```

### ✔ Audit de sécurité Python

```bash
bandit -r app
pip-audit
```

### ✔ Build Docker

```bash
docker build -t secureapp .
```

### ✔ Scan Trivy

```bash
trivy image secureapp --exit-code 0 --severity CRITICAL
```

`exit-code 0` permet d'afficher les vulnérabilités sans bloquer le pipeline.

---

## 🔐 Sécurité

Le pipeline détecte automatiquement :

- vulnérabilités Python
- dépendances vulnérables
- failles CRITIQUES dans l'image Docker
- mauvaises pratiques de code (Bandit)

Ce projet montre comment intégrer la sécurité dans un workflow DevOps (DevSecOps).

---

## 📦 Dépendances principales

- FastAPI
- Uvicorn
- Pydantic
- Ruff
- Pytest
- Bandit
- pip-audit
- Docker
- Trivy

---

## 📈 Améliorations futures

- Déploiement automatique (Railway, Render, Azure, etc.)
- Scan SAST (Semgrep)
- Scan secrets (Gitleaks)
- Authentification JWT
- Monitoring + logs

---

## 👤 Auteur

**Pierre Mzuafo**
Étudiant ingénieur à 3iL Ingénieurs — Limoges
Passionné par le DevOps, la sécurité applicative et l'analyse de données.
