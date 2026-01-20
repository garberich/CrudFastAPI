from customers.domain.customer import Customer
from customers.domain.customer_repository import CustomerRepository
from customers.domain.errors import CustomerAlreadyExistsError


class CreateCustomerUseCase:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, name: str, email: str) -> Customer:
        existing = self.repository.get_by_email(email)

        if existing:
            raise CustomerAlreadyExistsError(
                f"Customer with email {email} already exists"
            )

        customer = Customer.create(name=name, email=email)
        self.repository.save(customer)

        return customer
