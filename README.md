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

**Mis à jour le 09/11/2026** · Sprint en cours : **Sprint 1**

Statuts : ✅ Fait · 🔄 En cours · ⬜ À faire · 🔴 En retard

| Sprint | Période | Fait | État |
| --- | --- | --- | --- |
| Sprint 0 · Mise en place | 14/10 → 20/10 | 6 / 6 | ✅ Fait |
| Sprint 1 · Service complet dans K8s (10/20) | 21/10 → 03/11 | 4 / 9 | 🔄 En cours |
| Sprint 2 · Gateway + fraud-service (12-14/20) | 04/11 → 17/11 | 0 / 6 | ⬜ À faire |
| Sprint 3 · Base de données (16/20) | 18/11 → 29/11 | 0 / 6 | ⬜ À faire |
| Sprint 4 · gRPC + sécurité (18/20) | 30/11 → 08/12 | 0 / 7 | ⬜ À faire |
| Sprint 5 · Cloud + rapport (20/20) | 09/12 → 15/12 | 0 / 5 | ⬜ À faire |
| Marge · Finitions et envoi | 16/12 → 27/12 | 0 / 4 | ⬜ À faire |

**Déjà en place :** `account-service` (FastAPI) avec `GET /health`, `POST /accounts`, `GET /accounts`, `GET /accounts/{id}` ; Dockerization non-root, publication de l'image `nimaga02426/safebank-account-service:0.1.0` sur Docker Hub et déploiement avec Kubernetes (`Deployment` + `Service` + probes de santé) dans le namespace `safebank` sous Minikube.

**Priorité maintenant :** finaliser les routes de virement (`POST /transfers`), les tests unitaires/API du Sprint 1 et entamer `fraud-service`.

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
| 0.5 | Créer le squelette `services/fraud-service/` (uv, structure en couches, `GET /health`) | B | ✅ |
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
| 1.6 | Publier l'image `nimaga02426/safebank-account-service:0.1.0` sur Docker Hub | M | ✅ |
| 1.7 | `k8s/account-service/deployment.yaml` (probes sur `/health`) et `k8s/account-service/service.yaml` ; test sur minikube | M | ✅ |
| 1.8 | `fraud-service` : entité, règles de score, `POST /score`, tests | B | 🔄 |
| 1.9 | GitHub Actions par service (ruff + pytest + build Docker) | B | 🔄 |

### Sprint 2 · Paliers 12/20 et 14/20 : gateway + deuxième service relié (4 → 17 novembre)

Livrables et sous-tâches inchangés...

```

---

### Étape Git : effectuer le commit

Tu peux exécuter les commandes suivantes dans ton terminal pour ajouter les nouveaux manifests K8s et valider la mise à jour du `README.md` :

```bash
git add README.md k8s/
git commit -m "feat(k8s): add Kubernetes manifests for account-service and update sprint tracking"
```

Veux-tu qu'on s'attaque maintenant aux règles métier des virements (`Transfer` / `POST /transfers`) pour boucler le Sprint 1, ou qu'on passe à la configuration de la base de données PostgreSQL dans `k8s/postgres/` ?
