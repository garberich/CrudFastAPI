from dataclasses import dataclass
from uuid import UUID, uuid4
from .errors import CustomerAlreadyExistsError, InvalidCustomerError, CustomerNotFoundError

@dataclass
class Customer:
    id: UUID
    name: str
    email: str
    is_active: bool = True

    @staticmethod
    def create(name: str, email: str) -> "Customer":
        if not name:
            raise InvalidCustomerError("Customer name is required")
        
        if '@' not in email:
            raise InvalidCustomerError("Customer email is required")

        return Customer(id=uuid4(), name=name, email=email, is_active=True)
    
    def deactivate(self) -> None:
        self.is_active = False