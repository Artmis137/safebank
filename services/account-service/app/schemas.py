"""Modèles de données (DTO) exposés par l'API.

On sépare ce que le client envoie (AccountCreate) de ce que l'API renvoie
(Account) : le client ne choisit ni l'identifiant ni la date de création.
"""

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

# Les montants sont des Decimal et pas des float : 0.1 + 0.2 != 0.3 en float,
# ce qui est inacceptable pour de l'argent.
Money = Decimal


class AccountCreate(BaseModel):
    """Corps de la requête POST /accounts."""

    owner: str = Field(min_length=2, max_length=100, examples=["Mamadou NIMAGA"])
    initial_balance: Money = Field(
        default=Decimal("0.00"),
        ge=0,
        max_digits=12,
        decimal_places=2,
        description="Solde d'ouverture en euros, positif ou nul.",
    )


class Account(BaseModel):
    """Représentation d'un compte renvoyée par l'API."""

    id: UUID
    owner: str
    balance: Money
    currency: str = "EUR"
    created_at: datetime
