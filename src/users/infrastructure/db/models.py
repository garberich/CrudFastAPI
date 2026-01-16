from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.sqlite import BLOB
from users.infrastructure.db.base import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(BLOB, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    name = Column(String, nullable=False)