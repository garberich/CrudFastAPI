import pytest
from customers.domain.customer import Customer
from customers.application.update_customer import UpdateCustomerUseCase
from customers.domain.errors import CustomerNotFoundError, CustomerAlreadyExistsError
from tests.fakes.in_memory_customer_repository import InMemoryCustomerRepository

def test_update_customer_successfully():
    repository = InMemoryCustomerRepository()
    customer = Customer.create(name="Old", email="old@mail.com")
    customer.id = 1
    repository.save(customer)

    use_case = UpdateCustomerUseCase(repository)
    update = use_case.execute(customer_id=1, name="New", email="new@mail.com")

    assert update.name == "New"
    assert update.email == "new@mail.com"

def test_update_customer_not_found():
    repo = InMemoryCustomerRepository()
    use_case = UpdateCustomerUseCase(repo)

    with pytest.raises(CustomerNotFoundError):
        use_case.execute(1, "New", "new@mail.com")

def test_update_customer_with_existing_email():
    repo = InMemoryCustomerRepository()
    
    c1 = Customer.create("A", "a@mail.com")
    c1.id = 1
    repo.save(c1)

    c2 = Customer.create("B", "b@mail.com")
    c2.id = 2
    repo.save(c2)

    use_case = UpdateCustomerUseCase(repo)

    with pytest.raises(CustomerAlreadyExistsError):
        use_case.execute(2, "B", "a@mail.com")
    
