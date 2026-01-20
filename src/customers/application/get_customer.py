from customers.domain.customer import Customer
from customers.domain.customer_repository import CustomerRepository
from customers.domain.errors import CustomerNotFoundError
from uuid import UUID


class GetCustomerUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, customer_id: UUID) -> Customer:
        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            raise CustomerNotFoundError(f"Customer with id {customer_id} not found")

        return customer
