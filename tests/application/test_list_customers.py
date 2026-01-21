from customers.application.list_customers import ListCustomersUseCase
from customers.domain.customer import Customer
from tests.fakes.in_memory_customer_repository import InMemoryCustomerRepository

class test_list_customers():
    repo = InMemoryCustomerRepository()
    repo.save(Customer.create("Alice", "Alice@mail.com"))
    repo.save(Customer.create("Bob", "Bob@mail.com"))

    use_case = ListCustomersUseCase(repo)
    result = use_case.execute()

    assert len(result) == 2