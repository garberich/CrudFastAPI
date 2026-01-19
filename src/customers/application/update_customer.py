from customers.domain.customer import Customer
from customers.domain.customer_repository import CustomerRepository
from customers.domain.errors import (CustomerNotFoundError, CustomerAlreadyExistsError)

class UpdateCustomerUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, customer_id: int, name: str, email: str) -> Customer:
        customer = self.repository.get_by_id(customer_id)

        if not customer:
            raise CustomerNotFoundError(f"Customer with ID {customer_id} not found.")
        
        existing = self.repository.get_by_email(email)

        if existing and existing.id != customer_id:
            raise CustomerAlreadyExistsError(f"Customer with email {email} already exists.")
        
        customer.name = name
        customer.email = email

        return self.repository.save(customer)