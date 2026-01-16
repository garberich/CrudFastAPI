from users.domain.user import User
from users.domain.user_repository import UserRepository
from users.domain.errors import UserAlreadyExistsError

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def execute(self, name: str, email: str) -> User:
        if self.user_repository.exists_by_email(email):
            raise UserAlreadyExistsError(email)
        
        user = User.create(name=name, email=email)
        self.user_repository.save(user)
        return user