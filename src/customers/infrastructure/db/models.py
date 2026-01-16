from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid

from infrastructure.db.base import Base

class CustomerModel(Base):
    __tablename__ = "customers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
