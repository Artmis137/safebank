"""Routes REST de la ressource /accounts."""

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.repository import InMemoryAccountRepository, get_repository
from app.schemas import Account, AccountCreate

router = APIRouter(prefix="/accounts", tags=["accounts"])

# Injection de dépendance (équivalent de @Autowired en Spring)
Repo = Annotated[InMemoryAccountRepository, Depends(get_repository)]


@router.post("", response_model=Account, status_code=status.HTTP_201_CREATED)
def create_account(data: AccountCreate, repo: Repo) -> Account:
    """Ouvre un nouveau compte. Renvoie 201 Created avec le compte créé."""
    return repo.create(data)


@router.get("", response_model=list[Account])
def list_accounts(repo: Repo) -> list[Account]:
    """Liste tous les comptes."""
    return repo.list()


@router.get("/{account_id}", response_model=Account)
def get_account(account_id: UUID, repo: Repo) -> Account:
    """Renvoie un compte, ou 404 s'il n'existe pas."""
    account = repo.get(account_id)
    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Compte introuvable")
    return account
