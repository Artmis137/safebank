"""Entité métier Account : l'objet tel que la banque le manipule.

Ce n'est pas un schéma Pydantic : l'entité ne dépend ni de FastAPI ni de la base.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from decimal import Decimal
from uuid import UUID, uuid4


@dataclass
class Account:
    owner: str
    balance: Decimal
    id: UUID = field(default_factory=uuid4)
    currency: str = "EUR"
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
