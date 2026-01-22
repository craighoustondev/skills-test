import pytest

from models.user import User, Address, InvalidEmail


class TestUserCreation:
    def test_creates_user_with_valid_data(self):
        # Arrange
        address = Address(
            first_line="123 Main Street",
            town="London",
            postcode="SW1A 1AA",
        )

        # Act
        user = User.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            address=address,
        )

        # Assert
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.email == "john.doe@example.com"
        assert user.address == address

    def test_rejects_invalid_email(self):
        # Arrange
        address = Address(
            first_line="123 Main Street",
            town="London",
            postcode="SW1A 1AA",
        )

        # Act & Assert
        with pytest.raises(InvalidEmail):
            User.create(
                first_name="John",
                last_name="Doe",
                email="invalid-email",
                address=address,
            )

    def test_creates_user_with_address_including_second_line(self):
        # Arrange
        address = Address(
            first_line="Flat 2",
            second_line="123 Main Street",
            town="London",
            postcode="SW1A 1AA",
        )

        # Act
        user = User.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            address=address,
        )

        # Assert
        assert user.address.second_line == "123 Main Street"
