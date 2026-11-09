"""Injection de dépendances FastAPI (l'équivalent de @Autowired en Spring).

Une seule instance de repository vit tant que le processus tourne : un
redémarrage du pod efface les données, d'où PostgreSQL au Sprint 3.
Les tests remplacent get_repository par un repository neuf.
"""

from typing import Annotated

from fastapi import Depends

from app.repository.account_repository import InMemoryAccountRepository
from app.service.account_service import AccountService

_repository = InMemoryAccountRepository()


def get_repository() -> InMemoryAccountRepository:
    return _repository


def get_account_service(
    repository: Annotated[InMemoryAccountRepository, Depends(get_repository)],
) -> AccountService:
    return AccountService(repository)


AccountServiceDep = Annotated[AccountService, Depends(get_account_service)]
