import pytest
from customers.application.create_customer import CreateCustomerUseCase
from customers.domain.errors import CustomerAlreadyExistsError
from tests.fakes.in_memory_customer_repository import InMemoryCustomerRepository

def test_create_customer_successfully():
    repo = InMemoryCustomerRepository()
    use_case = CreateCustomerUseCase(repo)

    customer = use_case.execute("John", "john@mail.com")

    assert customer.email == "john@mail.com"
    assert len(repo.customers) == 1

def test_create_customer_with_existing_email():
    repo = InMemoryCustomerRepository()
    use_case = CreateCustomerUseCase(repo)

    use_case.execute("John", "john@mail.com")

    with pytest.raises(CustomerAlreadyExistsError):
        use_case.execute("Jane", "john@mail.com")
