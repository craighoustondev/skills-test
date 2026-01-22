from datetime import datetime


class CourseFull(Exception):
    pass


class TrainingCourse:
    def __init__(self, title: str, reference_number: str, scheduled_at: datetime, max_students: int):
        self.title = title
        self.reference_number = reference_number
        self.scheduled_at = scheduled_at
        self.max_students = max_students
        self.registered_students = []

    def register(self, student) -> None:
        if len(self.registered_students) >= self.max_students:
            raise CourseFull()
        self.registered_students.append(student)
