import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_hotels_default_limit():
    response = client.get("/hotels")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 10 

def test_average_price_no_region():
    response = client.get("/average-price")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "avg_price" in data[0]

def test_top_hotels_region_limit():
    response = client.get("/top-hotels?region=Guanacaste&limit=3")
    assert response.status_code == 200
    data = response.json()
    assert len(data) <= 3
    if len(data) > 0:
        assert "name" in data[0]
        assert "rating" in data[0]

def test_stats():
    response = client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_hotels" in data
    assert "avg_price" in data
    assert "avg_rating" in data
