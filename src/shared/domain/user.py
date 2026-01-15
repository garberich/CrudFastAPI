from dataclasses import dataclass
from uuid import UUID, uuid4

# Use dataclass and not use Pydantic to avoid attach fastapi with domain models
@dataclass
class User:
    id: UUID
    name: str
    email: str
    is_active: bool = True

    @classmethod
    def create(cls, email: str, name: str) -> "User":
        if '@' not in email:
            raise ValueError("Email inválido")

        return cls(id=uuid4(), name=name, email=email, is_active=True)