from customers.domain.customer_repository import CustomerRepository
from customers.domain.customer import Customer

class ListCustomersUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self) -> list[Customer]:
        return self.repository.list()