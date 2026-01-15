import pytest
from shared.application.create_user import CreateUserUseCase
from shared.tests.fakes.in_memory_user_repository import InMemoryUserRepository
from shared.domain.errors import UserAlreadyExistsError

def test_create_user_successfully():
    repo = InMemoryUserRepository()
    use_case = CreateUserUseCase(repo)

    user = use_case.execute("Test User", "test@mail.com")

    assert user.email == "test@mail.com"
    assert len(repo.users) == 1


def test_create_user_with_existing_email():
    repo = InMemoryUserRepository()
    use_case = CreateUserUseCase(repo)

    use_case.execute("Test User", "test@mail.com")

    with pytest.raises(UserAlreadyExistsError):
        use_case.execute("Test User", "test@mail.com")
