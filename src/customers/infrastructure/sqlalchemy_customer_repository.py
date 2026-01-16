from sqlalchemy.orm import Session

from customers.domain.customer_repository import CustomerRepository
from customers.domain.customer import Customer
from customers.infrastructure.db.models import CustomerModel

class SqlAlchemyCustomerRepository(CustomerRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, customer: Customer) -> None:
        model = CustomerModel(
            id=customer.id,
            name=customer.name,
            email=customer.email,
            is_active=customer.is_active
        )
        self.session.add(model)
        self.session.commit()

    def get_by_email(self, email: str):
        model = (
            self.session
            .query(CustomerModel)
            .filter(CustomerModel.email == email)
            .first()
        )

        if not model:
            return None

        return Customer(
            id=model.id,
            name=model.name,
            email=model.email,
            is_active=model.is_active
        )
