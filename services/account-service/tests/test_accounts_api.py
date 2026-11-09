from uuid import uuid4


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_account_returns_201(client):
    response = client.post("/accounts", json={"owner": "Alice", "initial_balance": "100.50"})
    assert response.status_code == 201
    body = response.json()
    assert body["owner"] == "Alice"
    assert body["balance"] == "100.50"
    assert body["currency"] == "EUR"


def test_get_account_by_id(client):
    created = client.post("/accounts", json={"owner": "Alice", "initial_balance": "10"}).json()
    response = client.get(f"/accounts/{created['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_list_accounts(client):
    client.post("/accounts", json={"owner": "Alice"})
    client.post("/accounts", json={"owner": "Bob"})
    assert len(client.get("/accounts").json()) == 2


def test_unknown_account_returns_404(client):
    assert client.get(f"/accounts/{uuid4()}").status_code == 404


def test_negative_initial_balance_returns_422(client):
    response = client.post("/accounts", json={"owner": "Alice", "initial_balance": "-5"})
    assert response.status_code == 422


def test_three_decimals_returns_422(client):
    response = client.post("/accounts", json={"owner": "Alice", "initial_balance": "1.234"})
    assert response.status_code == 422
