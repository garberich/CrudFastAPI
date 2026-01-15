from sqlalchemy.orm import Session
from shared.domain.user import User
from shared.domain.user_repository import UserRepository
from shared.infrastructure.db.models import UserModel

class SqlAlchemyUserRepository(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, user: User) -> None:
        db_user = UserModel(
            id=user.id.bytes,
            email=user.email,
            is_active=user.is_active,
            name=user.name
        )
        self.db.add(db_user)
        self.db.commit()

    def exists_by_email(self, email: str) -> bool:
        return (
            self.db.query(UserModel)
            .filter(UserModel.email == email)
            .first()
            is not None
        )
