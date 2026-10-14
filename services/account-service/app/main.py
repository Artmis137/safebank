from fastapi import FastAPI

from app.api import accounts

app = FastAPI(
    title="SafeBank - Account Service",
    description="Microservice de gestion des comptes et des virements (projet Cloud Native, M1 MLSD).",
    version="0.1.0",
)

app.include_router(accounts.router)


@app.get("/health", tags=["monitoring"])
def health() -> dict[str, str]:
    """Sonde de santé : Kubernetes l'appellera (liveness/readiness probes) au palier 1."""
    return {"status": "ok"}
