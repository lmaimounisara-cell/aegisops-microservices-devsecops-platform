from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_list_products():
    response = client.get("/api/v1/products")
    assert response.status_code == 200
    body = response.json()
    assert body["count"] == 3
    assert len(body["items"]) == 3


def test_get_existing_product():
    response = client.get("/api/v1/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Secure Cloud Storage"


def test_missing_product_returns_404():
    response = client.get("/api/v1/products/999")
    assert response.status_code == 404
