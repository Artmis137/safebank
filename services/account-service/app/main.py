from fastapi import FastAPI

from app.web import accounts
from app.web.errors import register_error_handlers

app = FastAPI(
    title="SafeBank - Account Service",
    description="Microservice de gestion des comptes et des virements (Cloud Native, M1 MLSD).",
    version="0.1.0",
)

app.include_router(accounts.router)
register_error_handlers(app)


@app.get("/health", tags=["monitoring"])
def health() -> dict[str, str]:
    """Sonde de santé appelée par Kubernetes (liveness/readiness probes)."""
    return {"status": "ok"}
