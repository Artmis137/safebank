import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.repository.account_repository import InMemoryAccountRepository
from app.web.dependencies import get_repository


@pytest.fixture
def client():
    """Un client HTTP de test avec un repository vide, neuf pour chaque test."""
    repository = InMemoryAccountRepository()
    app.dependency_overrides[get_repository] = lambda: repository
    yield TestClient(app)
    app.dependency_overrides.clear()
