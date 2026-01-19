import pytest
from customers.application.get_customer import GetCustomerUseCase
from customers.domain.errors import CustomerNotFoundError
from tests.fakes.in_memory_customer_repository import InMemoryCustomerRepository
from customers.domain.customer import Customer

def test_get_customer_successfully():
    repo = InMemoryCustomerRepository()
    customer = Customer.create("John Doe", "John@mail.com")
    customer.id = 1  # Manually setting ID for testing
    repo.save(customer)

    use_case = GetCustomerUseCase(repo)

    result = use_case.execute(1)

    assert result.id == 1
    assert result.email == "John@mail.com"

def test_get_customer_not_found():
    repo = InMemoryCustomerRepository()
    use_case = GetCustomerUseCase(repo)

    with pytest.raises(CustomerNotFoundError):
        use_case.execute(999)