"""Couche d'accès aux données.

Pour le palier 1, les comptes sont stockés en mémoire (un simple dict).
Toute l'API passe par cette classe : au palier 4 (16/20), on la remplacera
par une version PostgreSQL sans toucher aux routes.
"""

from datetime import datetime, timezone
from uuid import UUID, uuid4

from app.schemas import Account, AccountCreate


class InMemoryAccountRepository:
    def __init__(self) -> None:
        self._accounts: dict[UUID, Account] = {}

    def create(self, data: AccountCreate) -> Account:
        account = Account(
            id=uuid4(),
            owner=data.owner,
            balance=data.initial_balance,
            created_at=datetime.now(timezone.utc),
        )
        self._accounts[account.id] = account
        return account

    def get(self, account_id: UUID) -> Account | None:
        return self._accounts.get(account_id)

    def list(self) -> list[Account]:
        return list(self._accounts.values())


# Instance unique partagée par l'application (les données vivent tant que le
# processus tourne : un redémarrage du pod Kubernetes les efface, d'où le palier BDD).
repository = InMemoryAccountRepository()


def get_repository() -> InMemoryAccountRepository:
    """Dépendance FastAPI : permet de remplacer le dépôt dans les tests."""
    return repository
