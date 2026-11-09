"""Routes REST de la ressource /accounts. Aucune règle métier ici."""

from uuid import UUID

from fastapi import APIRouter, status

from app.dto.account import AccountCreate, AccountResponse
from app.web.dependencies import AccountServiceDep

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
def create_account(data: AccountCreate, service: AccountServiceDep) -> AccountResponse:
    """Ouvre un nouveau compte. Renvoie 201 Created avec le compte créé."""
    account = service.open_account(data.owner, data.initial_balance)
    return AccountResponse.model_validate(account)


@router.get("", response_model=list[AccountResponse])
def list_accounts(service: AccountServiceDep) -> list[AccountResponse]:
    """Liste tous les comptes."""
    return [AccountResponse.model_validate(a) for a in service.list_accounts()]


@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: UUID, service: AccountServiceDep) -> AccountResponse:
    """Renvoie un compte ; AccountNotFoundError devient un 404 (voir web/errors.py)."""
    return AccountResponse.model_validate(service.get_account(account_id))
