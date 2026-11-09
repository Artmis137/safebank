# account-service

Microservice SafeBank chargé de la gestion des comptes clients et des opérations de consultation du solde.

## Rôle du service

Le service `account-service` est la couche métier responsable de :

- la création de comptes,
- la liste des comptes existants,
- la consultation d'un compte par identifiant,
- la gestion du modèle de données du compte,
- l'exposition d'une API REST pour les autres composants du système.

## Architecture du service

Le service suit une structure simple en couches :

```text
account-service/
├── README.md
├── pyproject.toml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── repository.py
│   └── api/
│       ├── __init__.py
│       └── accounts.py
├── tests/
│   └── __init__.py
└── uv.lock
```

### Couche API

Le fichier `app/main.py` initialise l'application FastAPI et enregistre le router `accounts`.

### Couche DTO / validation

Le fichier `app/schemas.py` définit :

- `AccountCreate` : payload envoyé par le client,
- `Account` : réponse renvoyée par l'API,
- les règles de validation du montant (`Decimal`, `ge=0`, `decimal_places=2`).

### Couche repository

Le fichier `app/repository.py` encapsule le stockage des comptes.

À ce stade, le dépôt est implémenté en mémoire :

- `InMemoryAccountRepository`
- `repository = InMemoryAccountRepository()`

Cela correspond au niveau de complexité attendu pour une première étape, avec une mention explicite de l'objectif de remplacement par PostgreSQL plus tard.

## API REST exposée

### Endpoint de santé

- `GET /health`

Retour :

```json
{"status": "ok"}
```

### Comptes

- `POST /accounts`
- `GET /accounts`
- `GET /accounts/{account_id}`

### Exemple de création de compte

```bash
curl -X POST http://localhost:8000/accounts \
  -H "Content-Type: application/json" \
  -d '{
    "owner": "Mamadou NIMAGA",
    "initial_balance": 100.50
  }'
```

## Démarrage local

### Prérequis

- Python 3.12+
- `pip` ou `uv`

### Installation

```bash
cd services/account-service
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Lancement

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Vérification

```bash
curl http://localhost:8000/health
```

## Points d'architecture validés

- Service FastAPI isolé et exécutable indépendamment.
- Modèle de données découpé de la logique métier.
- Séparation API / repository / contracts.
- Préparation du projet pour l'intégration Kubernetes et la persistance PostgreSQL.

## Prochaine évolution attendue

- remplacement du dépôt en mémoire par PostgreSQL,
- intégration avec le service de fraude,
- sécurisation des endpoints et gestion des transactions,
- configuration Kubernetes (Déployment, Service, ConfigMap, Secret, probes).
