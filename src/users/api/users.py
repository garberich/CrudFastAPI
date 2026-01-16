from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from users.schemas.user import UserCreate, UserResponse
from users.application.create_user import CreateUserUseCase
from users.infrastructure.sqlalchemy_user_repository import SqlAlchemyUserRepository
from infrastructure.db.session import SessionLocal
from users.domain.errors import UserAlreadyExistsError

# router = APIRouter(prefix="/users", tags=["users"])
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=UserResponse)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    repo = SqlAlchemyUserRepository(db)
    use_case = CreateUserUseCase(repo)

    try:
        user = use_case.execute(payload.name, payload.email)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "id": str(user.id),
        "email": user.email,
        "is_active": user.is_active,
        "name": user.name
    }
