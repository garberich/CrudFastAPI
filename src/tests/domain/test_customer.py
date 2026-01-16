import pytest
from customers.domain.customer import Customer

def test_create_customer_successfully():
    customer = Customer.create(name="John Doe", email="john.doe@test.com")

    assert customer.email == "john.doe@test.com"
    assert customer.is_active is True

def test_cannot_create_customer_without_email():
    with pytest.raises(ValueError):
        Customer.create("John Doe", "")