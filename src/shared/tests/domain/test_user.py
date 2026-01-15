import pytest
from shared.domain.user import User

def test_create_user_with_valid_email():
    user = User.create("test@mail.com", "Test User")

    assert user.email == "test@mail.com"
    assert user.name == "Test User"
    assert user.is_active is True
    assert user.id is not None


def test_create_user_with_invalid_email():
    with pytest.raises(ValueError):
        User.create("invalid-email", "Test User")