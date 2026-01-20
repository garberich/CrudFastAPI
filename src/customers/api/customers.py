from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from customers.application.create_customer import CreateCustomerUseCase
from customers.application.get_customer import GetCustomerUseCase
from customers.application.list_customers import ListCustomersUseCase
from customers.application.update_customer import UpdateCustomerUseCase
from customers.application.deactivate_customer import DeactivateCustomerUseCase
from customers.domain.errors import CustomerAlreadyExistsError, CustomerNotFoundError
from infrastructure.db.session import SessionLocal
from customers.infrastructure.sqlalchemy_customer_repository import (
    SqlAlchemyCustomerRepository,
)

router = APIRouter()


# ---------- Schemas HTTP ----------
class CreateCustomerRequest(BaseModel):
    name: str
    email: EmailStr


class UpdateCustomerRequest(BaseModel):
    name: str
    email: EmailStr


class CustomerResponse(BaseModel):
    id: UUID
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
@router.post("/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(data: CreateCustomerRequest, db: Session = Depends(get_db)):
    repo = SqlAlchemyCustomerRepository(db)
    use_case = CreateCustomerUseCase(repo)

    try:
        customer = use_case.execute(data.name, data.email)
        return customer

    except CustomerAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: UUID, db: Session = Depends(get_db)):
    repo = SqlAlchemyCustomerRepository(db)
    use_case = GetCustomerUseCase(repo)

    try:
        return use_case.execute(customer_id)
    except CustomerNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    repo = SqlAlchemyCustomerRepository(db)
    use_case = ListCustomersUseCase(repo)
    return use_case.execute()


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: UUID,
    data: UpdateCustomerRequest,
    db: Session = Depends(get_db),
):
    repo = SqlAlchemyCustomerRepository(db)
    use_case = UpdateCustomerUseCase(repo)

    try:
        return use_case.execute(customer_id, data.name, data.email)
    except CustomerNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except CustomerAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def deactivate_customer(customer_id: int, db: Session = Depends(get_db)):
    repo = SqlAlchemyCustomerRepository(db)
    use_case = DeactivateCustomerUseCase(repo)

    try:
        use_case.execute(customer_id)
    except CustomerNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
