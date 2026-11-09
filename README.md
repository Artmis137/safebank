# SafeBank

Projet de démonstration Cloud Native pour le M1 MLSD à l'Université Paris Cité. L'objectif est de structurer une application bancaire en microservices autour d'un modèle de déploiement Kubernetes, avec une séparation claire entre interface, API, services métier et contrats d'intégration.

## Architecture cible

SafeBank suit une architecture orientée services avec les composants suivants :

- Frontend : interface utilisateur de consultation et d'interaction bancaire.
- Hub : point d'entrée applicatif, orchestration et routage des requêtes.
- Services métier :
  - `services/account-service` : gestion des comptes et virements.
  - `services/fraud-service` : analyse de fraude / détection potentielle.
- Couche donnée : PostgreSQL pour les données métier persistantes.
- Infrastructures Kubernetes : manifests de namespace, sécurité, gateway et base de données.
- Contrats inter-services : fichiers `.proto` dans `proto/` pour la communication RPC.

## Structure du dépôt

```text
safebank/
├── README.md
├── docs/
├── frontend/
├── hub/
├── k8s/
│   ├── namespace.yaml
│   ├── account-service/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── postgres/
│   ├── security/
│   └── gateway/
├── proto/
├── services/
│   ├── account-service/
│   └── fraud-service/
└── .gitignore
```

---

## Suivi d'avancement

**Mis à jour le 09/11/2026** · Sprint en cours : **Sprint 2** (Sprint 1 en retard)

Statuts : ✅ Fait · 🔄 En cours · ⬜ À faire · 🔴 En retard

| Sprint | Période | Fait | État |
| --- | --- | --- | --- |
| Sprint 0 · Mise en place | 14/10 → 20/10 | 3 / 6 | 🔴 En retard |
| Sprint 1 · Service complet dans K8s (10/20) | 21/10 → 03/11 | 3 / 9 | 🔴 En retard |
| Sprint 2 · Gateway + fraud-service (12-14/20) | 04/11 → 17/11 | 0 / 6 | ⬜ À faire |
| Sprint 3 · Base de données (16/20) | 18/11 → 29/11 | 0 / 6 | ⬜ À faire |
| Sprint 4 · gRPC + sécurité (18/20) | 30/11 → 08/12 | 0 / 7 | ⬜ À faire |
| Sprint 5 · Cloud + rapport (20/20) | 09/12 → 15/12 | 0 / 5 | ⬜ À faire |
| Marge · Finitions et envoi | 16/12 → 27/12 | 0 / 4 | ⬜ À faire |

**Déjà en place :** `account-service` (FastAPI) avec `GET /health`, `POST /accounts`, `GET /accounts`, `GET /accounts/{id}` ; Dockerization non-root, publication de l'image `mnimaga02426/safebank-account-service:0.1.0` sur Docker Hub et déploiement avec Kubernetes (`Deployment` + `Service` + probes de santé) dans le namespace `safebank` sous Minikube.

**Priorité maintenant :** rattraper le Sprint 1 côté `account-service` (structure en couches, ruff, virements `POST /transfers` avec les règles 1 à 4, tests), puis brancher `fraud-service` (Sprint 2). Côté binôme : pousser le squelette de `fraud-service` et `POST /score`.

---

## Plan des sprints

Date limite de rendu : **dimanche 27 décembre 2026**. Objectif du binôme : projet terminé le **mardi 15 décembre 2026**, date du dernier cours de Programmation distribuée. Du 16 au 27 décembre, on ne garde que la marge : corrections, rapport final et envoi.

**M** = Mamadou, **B** = Billal, **M+B** = ensemble.

| Repère | Date |
| --- | --- |
| Cours Programmation distribuée | 9/11, 14/12, 15/12 (matin) |
| Cours Conteneurisation | 18/11, 23/11, 2/12 |
| Cours Cloud Computing | 16/11, 30/11, 7/12 |
| Hackathon (moins de temps pour le projet) | 24-25/11 |
| Fin visée du projet | 15/12 |
| Envoi au prof, au plus tard | 27/12 (viser le 20/12, avant les vacances de Noël) |

### Sprint 0 · Mise en place (14 → 20 octobre)

| # | Tâche | Qui | Statut |
| --- | --- | --- | --- |
| 0.1 | Ajouter le binôme comme collaborateur du dépôt GitHub, protéger `main` | M | ✅ |
| 0.2 | Ajouter `docs/` et un `README.md` racine | M | ✅ |
| 0.3 | Réorganiser `account-service` en couches : `entity/`, `dto/`, `repository/`, `service/`, `web/`, `exceptions.py` | M | ✅ |
| 0.4 | Ajouter ruff (`uv add --dev ruff`) et le configurer dans `pyproject.toml` | M | ✅ |
| 0.5 | Créer le squelette `services/fraud-service/` (uv, structure en couches, `GET /health`) | B | 🔴 |
| 0.6 | Installer en local : Docker, minikube, kubectl ; créer un compte Docker Hub chacun | M+B | ✅ |

### Sprint 1 · Palier 10/20 : un service complet dans Kubernetes (21 octobre → 3 novembre)

Livrable : captures de `kubectl get pods,svc`, de Docker Hub et d'un appel à l'API dans le cluster.

| # | Tâche | Qui | Statut |
| --- | --- | --- | --- |
| 1.1 | Entité `Transfer` + `TransferStatus` (`ACCEPTED`, `PENDING_REVIEW`, `REJECTED`) | M | 🔴 |
| 1.2 | `TransferService` : règles 1 à 4 (comptes existants, montant > 0, comptes différents, solde suffisant) | M | 🔴 |
| 1.3 | Routes `POST /transfers` et `GET /accounts/{id}/transfers` ; exceptions métier → codes HTTP | M | 🔴 |
| 1.4 | Tests unitaires de la couche service + tests API | M | 🔴 |
| 1.5 | `Dockerfile` + `.dockerignore` de `account-service` (non root, uv) | M | ✅ |
| 1.6 | Publier l'image `mnimaga02426/safebank-account-service:0.1.0` sur Docker Hub | M | ✅ |
| 1.7 | `k8s/account-service/deployment.yaml` (probes sur `/health`) et `k8s/account-service/service.yaml` ; test sur minikube | M | ✅ |
| 1.8 | `fraud-service` : entité, règles de score, `POST /score`, tests | B | 🔄 |
| 1.9 | GitHub Actions par service (ruff + pytest + build Docker) | B | 🔄 |

### Sprint 2 · Paliers 12/20 et 14/20 : gateway + deuxième service relié (4 → 17 novembre)

Livrable : capture d'un virement accepté et d'un virement bloqué passant par la gateway.

| # | Tâche | Qui | Statut |
|---|-------|-----|--------|
| 2.1 | `Dockerfile` + image `safebank-fraud-service:0.1.0` + Deployment/Service Kubernetes | B | ⬜ |
| 2.2 | Couche `client/` dans `account-service` : appel REST à `fraud-service` (URL dans `config.py`, timeout court) | M | ⬜ |
| 2.3 | Règle 5 (ALLOW / REVIEW / BLOCK) et règle 6 (`fraud-service` indisponible → 503) + tests | M | ⬜ |
| 2.4 | ConfigMap pour `FRAUD_SERVICE_URL` | M | ⬜ |
| 2.5 | Gateway : Ingress minikube, puis Istio Gateway + VirtualService vers `account-service` | M+B | ⬜ |
| 2.6 | Vérifier que `fraud-service` n'est pas joignable depuis l'extérieur du cluster | B | ⬜ |

### Sprint 3 · Palier 16/20 : base de données (18 → 29 novembre)

Hackathon les 24-25/11 : prévoir peu de travail ces deux jours.

| # | Tâche | Qui | Statut |
|---|-------|-----|--------|
| 3.1 | Repository PostgreSQL (SQLAlchemy 2) à la place du repository en mémoire | M | ⬜ |
| 3.2 | Migrations Alembic (tables `accounts`, `transfers`) | M | ⬜ |
| 3.3 | Virement dans une transaction (débit + crédit + enregistrement, tout ou rien) | M | ⬜ |
| 3.4 | PostgreSQL dans Kubernetes : PVC + Secret + Service | B | ⬜ |
| 3.5 | `docker compose` pour lancer les deux services + PostgreSQL en local | B | ⬜ |
| 3.6 | Test : supprimer un pod `account-service`, vérifier que les données sont toujours là | M+B | ⬜ |

### Sprint 4 · Palier 18/20 + bonus gRPC (30 novembre → 8 décembre)

| # | Tâche | Qui | Statut |
|---|-------|-----|--------|
| 4.1 | `proto/fraud.proto` + génération du code Python | B | ⬜ |
| 4.2 | Serveur gRPC dans `fraud-service` (port 50051) | B | ⬜ |
| 4.3 | Client gRPC dans `account-service` ; choix REST/gRPC par `FRAUD_TRANSPORT` | M | ⬜ |
| 4.4 | Istio : mTLS strict dans le namespace `safebank` | M+B | ⬜ |
| 4.5 | RBAC : ServiceAccount par service, Role/RoleBinding minimaux | M | ⬜ |
| 4.6 | Secrets Kubernetes pour toutes les données sensibles | M | ⬜ |
| 4.7 | Docker Hub : 2FA, jeton pour la CI, scan des images (Trivy) | B | ⬜ |

### Sprint 5 · Palier 20/20 : cloud + rapport (9 → 15 décembre)

Le 15/12, le projet doit tourner de bout en bout.

| # | Tâche | Qui | Statut |
|---|-------|-----|--------|
| 5.1 | Cluster GKE, déploiement des deux services + PostgreSQL | M+B | ⬜ |
| 5.2 | Vérifier le parcours sur GKE : gateway → `account-service` → `fraud-service` → PostgreSQL | M+B | ⬜ |
| 5.3 | Rapport, première version : architecture, une section par palier avec ses captures | M+B | ⬜ |
| 5.4 | Rassembler les captures des Google labs de chacun | M+B | ⬜ |
| 5.5 | Montrer le projet au prof les 14 et 15/12 | M+B | ⬜ |

### Marge · Finitions et envoi (16 → 27 décembre)

| # | Tâche | Qui | Statut |
|---|-------|-----|--------|
| 6.1 | Corriger ce qui reste après les retours du 14-15/12 | M+B | ⬜ |
| 6.2 | Rapport final relu par les deux, `README` à jour, tag `v1.0.0` | M+B | ⬜ |
| 6.3 | Envoi par mail à benoit.charroux@gmail.com : rapport + lien du dépôt + captures | M | ⬜ |
| 6.4 | Optionnel : front React minimal ou modèle scikit-learn anti-fraude | B/M | ⬜ |

---

## Démarrage rapide

### Service comptes

```bash
cd services/account-service
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Le service expose alors :

- `GET /health`
- `POST /accounts`
- `GET /accounts`
- `GET /accounts/{account_id}`
