"""Accès aux données des comptes.

Version en mémoire (un dict) pour l'instant. Au Sprint 3, une version
PostgreSQL offrira les mêmes méthodes : la couche service ne changera pas.
"""

from uuid import UUID

from app.entity.account import Account


class InMemoryAccountRepository:
    def __init__(self) -> None:
        self._accounts: dict[UUID, Account] = {}

    def save(self, account: Account) -> Account:
        self._accounts[account.id] = account
        return account

    def get(self, account_id: UUID) -> Account | None:
        return self._accounts.get(account_id)

    def list(self) -> list[Account]:
        return list(self._accounts.values())
