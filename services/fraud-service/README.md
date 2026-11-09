# fraud-service

Service SafeBank dédié à la détection et à l'analyse des risques de fraude.

## Rôle attendu

Le service `fraud-service` doit traiter les événements liés aux opérations bancaires afin de :

- détecter des comportements suspects,
- attribuer un niveau de risque,
- fournir un verdict sur la validité d'une transaction,
- interagir avec `account-service` via un contrat défini dans `proto/`.

## Architecture prévue

```text
fraud-service/
├── README.md
├── app/
├── tests/
├── pyproject.toml
└── Dockerfile (à prévoir)
```

## État actuel

Le dossier est vide. Il constitue une base vide pour le prochain service métier de SafeBank.

## Intégration prévue

Le service sera probablement connecté à :

- `account-service` pour récupérer les informations sur les comptes et les transactions,
- `proto/fraude.proto` pour définir le contrat gRPC,
- Kubernetes pour un déploiement séparé et un scaling propre.

## Contrat à définir

Le fichier `proto/fraude.proto` doit décrire :

- une requête de contrôle de fraude,
- une réponse avec score ou niveau de risque,
- les méthodes RPC exposées par le service.

## Prochaine étape

Implémenter le service avec :

1. un point d'entrée API ou gRPC,
2. un modèle de calcul de risque,
3. une couche de validation et d'intégration,
4. la configuration Kubernetes associée.
