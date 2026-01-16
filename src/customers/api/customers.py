from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from customers.application.create_customer import CreateCustomerUseCase
from customers.domain.errors import CustomerAlreadyExistsError
from infrastructure.db.session import SessionLocal
from customers.infrastructure.sqlalchemy_customer_repository import (
    SqlAlchemyCustomerRepository
)

router = APIRouter()

# ---------- Schemas HTTP ----------

class CreateCustomerRequest(BaseModel):
    name: str
    email: EmailStr

class CustomerResponse(BaseModel):
    id: str
    name: str
    email: str
    is_active: bool

# ---------- DB Dependency ----------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- Endpoint ----------

@router.post("/", response_model=CustomerResponse, status_code=201)
def create_customer(
    data: CreateCustomerRequest,
    db: Session = Depends(get_db)
):
    repo = SqlAlchemyCustomerRepository(db)
    use_case = CreateCustomerUseCase(repo)

    try:
        customer = use_case.execute(data.name, data.email)
        return customer

    except CustomerAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
