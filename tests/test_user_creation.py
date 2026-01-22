import pytest
from datetime import datetime

from models.user import User, Address, InvalidEmail
from models.training_course import TrainingCourse, CourseFull


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


class TestUserRegistration:
    def test_user_can_register_for_training_course(self):
        # Arrange
        address = Address(
            first_line="123 Main Street",
            town="London",
            postcode="SW1A 1AA",
        )
        user = User.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            address=address,
        )
        course = TrainingCourse(
            title="Python Fundamentals",
            reference_number="PF-001",
            scheduled_at=datetime(2026, 3, 15, 9, 0),
            max_students=10,
        )

        # Act
        user.register_for_course(course)

        # Assert
        assert course in user.registered_courses

    def test_user_cannot_register_for_full_course(self):
        # Arrange
        address = Address(
            first_line="123 Main Street",
            town="London",
            postcode="SW1A 1AA",
        )
        first_user = User.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            address=address,
        )
        second_user = User.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            address=address,
        )
        course = TrainingCourse(
            title="Python Fundamentals",
            reference_number="PF-001",
            scheduled_at=datetime(2026, 3, 15, 9, 0),
            max_students=1,
        )
        first_user.register_for_course(course)

        # Act & Assert
        with pytest.raises(CourseFull):
            second_user.register_for_course(course)
