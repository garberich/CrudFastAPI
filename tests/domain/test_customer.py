import pytest
from customers.domain.customer import Customer
from customers.domain.errors import InvalidCustomerError

def test_create_customer_successfully():
    customer = Customer.create(name="John Doe", email="john.doe@test.com")

    assert customer.email == "john.doe@test.com"
    assert customer.is_active is True

def test_create_customer_without_name_fails():
    with pytest.raises(InvalidCustomerError):
        Customer.create("", "john@mail.com")

def test_create_customer_without_email_fails():
    with pytest.raises(InvalidCustomerError):
        Customer.create("John Doe", "")