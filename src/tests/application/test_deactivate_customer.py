import pytest
from customers.application.deactivate_customer import DeactivateCustomerUseCase
from customers.domain.errors import CustomerNotFoundError
from tests.fakes.in_memory_customer_repository import InMemoryCustomerRepository
from customers.domain.customer import Customer


def test_deactivate_customer():
    repo = InMemoryCustomerRepository()
    customer = Customer.create("John", "john@mail.com")
    customer.id = 1
    repo.save(customer)

    use_case = DeactivateCustomerUseCase(repo)
    use_case.execute(1)

    updated = repo.get_by_id(1)
    assert updated.is_active is False


def test_deactivate_customer_not_found():
    repo = InMemoryCustomerRepository()
    use_case = DeactivateCustomerUseCase(repo)

    with pytest.raises(CustomerNotFoundError):
        use_case.execute(1)
