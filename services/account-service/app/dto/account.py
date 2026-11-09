"""DTO (schémas Pydantic) : ce qui entre dans l'API et ce qui en sort.

On sépare ce que le client envoie (AccountCreate) de ce que l'API renvoie
(AccountResponse) : le client ne choisit ni l'identifiant ni la date de création.
Les montants sont des Decimal, jamais des float (0.1 + 0.2 != 0.3 en float).
"""

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class AccountCreate(BaseModel):
    """Corps de la requête POST /accounts."""

    owner: str = Field(min_length=2, max_length=100, examples=["Mamadou NIMAGA"])
    initial_balance: Decimal = Field(
        default=Decimal("0.00"),
        ge=0,
        max_digits=12,
        decimal_places=2,
        description="Solde d'ouverture en euros, positif ou nul.",
    )


class AccountResponse(BaseModel):
    """Représentation d'un compte renvoyée par l'API."""

    # Permet de construire le DTO directement depuis l'entité (dataclass).
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    owner: str
    balance: Decimal
    currency: str
    created_at: datetime
