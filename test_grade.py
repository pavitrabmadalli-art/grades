import pytest
from app import grade_for


class TestStudentGrade(pytest.TestCase):
    def test_grade_s(self):
        self.assertEqual(grade_for(95), "S")

    def test_grade_a(self):
        self.assertEqual(grade_for(85), "A")

    def test_grade_b(self):
        self.assertEqual(grade_for(70), "B")

    def test_grade_c(self):
        self.assertEqual(grade_for(55), "C")

    def test_grade_d(self):
        self.assertEqual(grade_for(45), "D")

    def test_grade_f(self):
        self.assertEqual(grade_for(30), "F")


if __name__ == "__main__":
    pytest.main()