# Protobuf / contrats inter-services

Ce dossier centralise les contrats partagés entre services. Il est destiné à définir les messages et les méthodes RPC utilisées par les microservices pour communiquer entre eux.

## Fichier actuel

- `fraude.proto` : fichier de contrat de l'API de détection de fraude.

## État actuel

Le fichier est vide et doit être complété pour définir :

- les messages d'entrée/sortie,
- les services RPC exposés,
- les méthodes de vérification et de scoring de fraude,
- les types de données partagés avec le service `fraud-service`.

## Exemple de structure attendue

```proto
syntax = "proto3";

package safebank;

service FraudService {
  rpc CheckFraud (FraudRequest) returns (FraudResponse);
}

message FraudRequest {
  string account_id = 1;
  string transaction_id = 2;
  double amount = 3;
}

message FraudResponse {
  bool is_fraudulent = 1;
  string risk_level = 2;
}
```

Cette étape est importante pour garantir une intégration propre entre `account-service` et le futur `fraud-service`.
