from dataclasses import dataclass
from uuid import UUID, uuid4

@dataclass
class Customer:
    id: UUID
    name: str
    email: str
    is_active: bool = True

    @staticmethod
    def create(name: str, email: str) -> "Customer":
        if '@' not in email:
            raise ValueError("Invalid email")

        return Customer(id=uuid4(), name=name, email=email, is_active=True)
    
    def deactivate(self) -> None:
        self.is_active = False