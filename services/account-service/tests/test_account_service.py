from decimal import Decimal
from uuid import uuid4

import pytest

from app.exceptions import AccountNotFoundError
from app.repository.account_repository import InMemoryAccountRepository
from app.service.account_service import AccountService


@pytest.fixture
def service():
    return AccountService(InMemoryAccountRepository())


def test_open_account_keeps_decimal_balance(service):
    account = service.open_account("Alice", Decimal("100.50"))
    assert account.balance == Decimal("100.50")
    assert service.get_account(account.id) is account


def test_get_unknown_account_raises(service):
    with pytest.raises(AccountNotFoundError):
        service.get_account(uuid4())
