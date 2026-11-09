# Services SafeBank

Ce dossier contient les microservices métier de l'application SafeBank.

## Services actuels

### `account-service`

Service principal de gestion des comptes clients et des opérations de transfert.

Technologies :
- Python
- FastAPI
- Pydantic
- Uvicorn

Endpoints principaux :
- `GET /health`
- `POST /accounts`
- `GET /accounts`
- `GET /accounts/{account_id}`

### `fraud-service`

Service prévu pour la détection de fraude et l'analyse de transactions ou de comportements suspects.

À l'état actuel, ce dossier est encore un espace d'extension et doit être complété avec son propre code applicatif, ses dépendances et ses endpoints ou contrat RPC.

## Organisation

```text
services/
├── README.md
├── account-service/
└── fraud-service/
```

## Principe architectural

La séparation entre services suit une logique de domaine métier :

- `account-service` : comptes, soldes, transactions simples.
- `fraud-service` : détection, scoring, logique de risque.

Cette séparation facilite l'isolation des responsabilités et la mise en place de déploiements indépendants dans Kubernetes.
