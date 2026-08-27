import unittest

from student_record import StudentRecord


class StudentRecordCRUDTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = StudentRecord()

    def test_create_and_read_student(self) -> None:
        created = self.record.create_student("Alice", 20, "A")

        self.assertEqual(created["id"], 1)
        self.assertEqual(created["name"], "Alice")
        self.assertEqual(self.record.get_student(1), created)

    def test_list_students(self) -> None:
        first = self.record.create_student("Alice", 20, "A")
        second = self.record.create_student("Bob", 22, "B")

        self.assertEqual(self.record.list_students(), [first, second])

    def test_update_student(self) -> None:
        created = self.record.create_student("Alice", 20, "A")

        updated = self.record.update_student(created["id"], name="Alicia", age=21)

        self.assertEqual(updated["name"], "Alicia")
        self.assertEqual(updated["age"], 21)
        self.assertEqual(updated["grade"], "A")

    def test_delete_student(self) -> None:
        created = self.record.create_student("Alice", 20, "A")

        removed = self.record.delete_student(created["id"])

        self.assertTrue(removed)
        self.assertIsNone(self.record.get_student(created["id"]))

    def test_missing_student_behaviors(self) -> None:
        self.assertIsNone(self.record.get_student(999))
        self.assertIsNone(self.record.update_student(999, name="Nobody"))
        self.assertFalse(self.record.delete_student(999))


if __name__ == "__main__":
    unittest.main()
