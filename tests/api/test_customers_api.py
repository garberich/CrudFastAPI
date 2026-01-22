# from fastapi.testclient import TestClient
# from main import app
from uuid import uuid4

# client = TestClient(app)


def test_create_customer_successfully(client):
    payload = {"name": "John Doe", "email": "john@test.com"}

    response = client.post("/customer/", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "John Doe"
    assert data["email"] == "john@test.com"
    assert data["is_active"] is True
    assert "id" in data


def test_create_customer_with_existing_email(client):
    payload = {"name": "John Doe", "email": "duplicate@test.com"}

    client.post("/customer/", json=payload)
    response = client.post("/customer/", json=payload)

    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]


def test_get_customer_by_id(client):
    payload = {"name": "Jane Doe", "email": "jane@test.com"}

    create = client.post("/customer/", json=payload)
    customer_id = create.json()["id"]

    response = client.get(f"/customer/{customer_id}")

    assert response.status_code == 200
    assert response.json()["email"] == "jane@test.com"


def test_get_customer_not_found(client):
    response = client.get(f"/customer/{uuid4()}")
    assert response.status_code == 404


def test_list_customers(client):
    response = client.get("/customer/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_customer(client):
    create = client.post("/customer/", json={"name": "Old", "email": "old@test.com"})
    customer_id = create.json()["id"]

    update = client.put(
        f"/customer/{customer_id}", json={"name": "New", "email": "new@test.com"}
    )

    assert update.status_code == 200
    assert update.json()["name"] == "New"


def test_deactivate_customer(client):
    create = client.post(
        "/customer/", json={"name": "To Deactivate", "email": "off@test.com"}
    )
    customer_id = create.json()["id"]

    response = client.delete(f"/customer/{customer_id}")
    assert response.status_code == 204

    get_customer = client.get(f"/customer/{customer_id}")
    assert get_customer.json()["is_active"] is False
