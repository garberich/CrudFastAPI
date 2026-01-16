from abc import ABC, abstractmethod
from .user import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def exists_by_email(self, email:str) -> bool:
        pass

    # @abstractmethod
    # def get_by_id(self, user_id: str) -> User | None:
    #     pass

    # @abstractmethod
    # def get_all(self) -> list[User]:
    #     pass

    # @abstractmethod
    # def update(self, user: User) -> None:
    #     pass

    # @abstractmethod
    # def delete(self, user_id: str) -> None:
    #     pass