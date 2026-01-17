from .customer import Customer
from abc import ABC, abstractmethod

class CustomerRepository(ABC):
    @abstractmethod
    def save(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def get_by_id(self, customer_id: int) -> Customer | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Customer | None:
        pass

    @abstractmethod
    def list(self) -> list[Customer]:
        pass

    @abstractmethod
    def delete(self, customer_id: int) -> None:
        pass