"""Règles métier sur les comptes. Ne connaît pas HTTP : lève des exceptions métier."""

from decimal import Decimal
from uuid import UUID

from app.entity.account import Account
from app.exceptions import AccountNotFoundError
from app.repository.account_repository import InMemoryAccountRepository


class AccountService:
    def __init__(self, repository: InMemoryAccountRepository) -> None:
        self._repository = repository

    def open_account(self, owner: str, initial_balance: Decimal) -> Account:
        return self._repository.save(Account(owner=owner, balance=initial_balance))

    def get_account(self, account_id: UUID) -> Account:
        account = self._repository.get(account_id)
        if account is None:
            raise AccountNotFoundError(account_id)
        return account

    def list_accounts(self) -> list[Account]:
        return self._repository.list()
