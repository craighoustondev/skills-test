import re
from typing import Optional


class InvalidEmail(Exception):
    pass


class Address:
    def __init__(
        self,
        first_line: str,
        town: str,
        postcode: str,
        second_line: Optional[str] = None,
    ):
        self.first_line = first_line
        self.second_line = second_line
        self.town = town
        self.postcode = postcode


class User:
    def __init__(self, first_name: str, last_name: str, email: str, address: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.registered_courses = []

    @classmethod
    def create(cls, first_name: str, last_name: str, email: str, address: Address) -> "User":
        cls._validate_email(email)
        return cls(first_name, last_name, email, address)

    @staticmethod
    def _validate_email(email: str) -> None:
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            raise InvalidEmail()

    def register_for_course(self, course) -> None:
        course.register(self)
        self.registered_courses.append(course)