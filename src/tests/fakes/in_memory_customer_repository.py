from customers.domain.customer_repository import CustomerRepository
from customers.domain.customer import Customer
from uuid import UUID

class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self):
        self.customers: list[Customer] = []

    def save(self, customer: Customer) -> Customer:
        self.customers.append(customer)
        return customer

    def get_by_email(self, email: str) -> Customer | None:
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None
    
    def get_by_id(self, customer_id: UUID) -> Customer | None:
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None
    
    def list(self) -> list[Customer]:
        return self.customers

    def delete(self, customer_id: UUID) -> None:
        self.customers = [
            c for c in self.customers if c.id != customer_id
        ]
