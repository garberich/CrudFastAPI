from typing import List, Optional
from sqlalchemy.orm import Session

from customers.domain.customer_repository import CustomerRepository
from customers.domain.customer import Customer
from customers.infrastructure.db.models import CustomerModel


class SqlAlchemyCustomerRepository(CustomerRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, customer: Customer) -> None:
        model = self.session.get(CustomerModel, customer.id)

        if model is None:
            model = CustomerModel(
                id=customer.id,
                name=customer.name,
                email=customer.email,
                is_active=customer.is_active,
            )
            self.session.add(model)
        # Update existing record
        else:
            model.name = customer.name
            model.email = customer.email
            model.is_active = customer.is_active

        self.session.commit()

    def get_by_id(self, customer_id) -> Optional[Customer]:
        model = self.session.get(CustomerModel, customer_id)

        if not model:
            return None

        return Customer(
            id=model.id,
            name=model.name,
            email=model.email,
            is_active=model.is_active,
        )

    def get_by_email(self, email: str) -> Optional[Customer]:
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
            is_active=model.is_active,
        )

    def list(self) -> List[Customer]:
        models = self.session.query(CustomerModel).all()

        return [
            Customer(
                id=model.id,
                name=model.name,
                email=model.email,
                is_active=model.is_active,
            )
            for model in models
        ]

    def delete(self, customer_id) -> None:
        model = self.session.get(CustomerModel, customer_id)

        if model:
            model.is_active = False
            self.session.commit()
