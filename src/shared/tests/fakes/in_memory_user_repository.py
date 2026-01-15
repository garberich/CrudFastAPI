from shared.domain.user import User
from shared.domain.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = [] # type: list[User]

    def save(self, user: User) -> None:
        self.users.append(user)

    def exists_by_email(self, email: str) -> bool:
        return any(u.email == email for u in self.users)