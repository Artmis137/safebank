# Kubernetes manifests

Ce dossier contient les ressources de déploiement et d'orchestration de SafeBank dans Kubernetes.

## Structure attendue

```text
k8s/
├── README.md
├── namespace.yaml
├── postgres/
├── security/
├── geteway/
```

## Composants prévus

- `namespace.yaml` : définit le namespace de travail de l'application.
- `postgres/` : configuration du stockage persistant et du service PostgreSQL.
- `security/` : services et politiques de sécurité, secrets, RBAC ou NetworkPolicy.
- `geteway/` : configuration du point d'entrée HTTP / gateway / reverse proxy.

## État actuel

Le dossier est bien structuré pour un déploiement Kubernetes, mais les manifestes sont encore incomplets. En particulier :

- `namespace.yaml` est vide ;
- les sous-dossiers `postgres`, `security` et `geteway` ne contiennent pas encore de ressources.

## Exemple de namespace attendu

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: safebank
```

Cette base est la première étape indispensable pour un déploiement cohérent de l'application.
