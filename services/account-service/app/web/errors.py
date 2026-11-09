"""Traduction des exceptions métier en réponses HTTP."""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.exceptions import AccountNotFoundError


def register_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(AccountNotFoundError)
    async def account_not_found(_: Request, exc: AccountNotFoundError) -> JSONResponse:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)})
