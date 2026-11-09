"""Exceptions métier.

La couche service lève ces exceptions sans rien savoir de HTTP.
C'est la couche web qui les traduit en codes HTTP (voir app/web/errors.py).
"""

from uuid import UUID


class DomainError(Exception):
    """Classe mère de toutes les erreurs métier de SafeBank."""


class AccountNotFoundError(DomainError):
    def __init__(self, account_id: UUID) -> None:
        super().__init__(f"Compte {account_id} introuvable")
        self.account_id = account_id
