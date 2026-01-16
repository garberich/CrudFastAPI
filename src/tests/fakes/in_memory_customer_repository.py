from customers.domain.customer_repository import CustomerRepository
from customers.domain.customer import Customer

class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self):
        self.customers = []

    def save(self, customer: Customer) -> None:
        self.customers.append(customer)

    def get_by_email(self, email: str):
        return next(
            (c for c in self.customers if c.email == email),
            None
        )
