from datetime import datetime

from models.training_course import TrainingCourse


class TestTrainingCourseCreation:
    def test_creates_training_course_with_required_fields(self):
        # Arrange
        title = "Python Fundamentals"
        reference_number = "PF-001"
        scheduled_at = datetime(2026, 3, 15, 9, 0)
        max_students = 10

        # Act
        course = TrainingCourse(
            title=title,
            reference_number=reference_number,
            scheduled_at=scheduled_at,
            max_students=max_students,
        )

        # Assert
        assert course.title == "Python Fundamentals"
        assert course.reference_number == "PF-001"
        assert course.scheduled_at == datetime(2026, 3, 15, 9, 0)
        assert course.max_students == 10
