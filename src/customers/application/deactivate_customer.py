from customers.domain.customer_repository import CustomerRepository
from customers.domain.errors import CustomerNotFoundError
from uuid import UUID


class DeactivateCustomerUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, customer_id: UUID) -> None:
        customer = self.repository.get_by_id(customer_id)

        if not customer:
            raise CustomerNotFoundError(f"Customer with id {customer_id} not found")

        customer.deactivate()
        self.repository.save(customer)
