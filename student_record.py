from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass
class Student:
    id: int
    name: str
    age: int
    grade: str


class StudentRecord:
    def __init__(self) -> None:
        self._students: dict[int, Student] = {}
        self._next_id = 1

    def create_student(self, name: str, age: int, grade: str) -> dict:
        student = Student(id=self._next_id, name=name, age=age, grade=grade)
        self._students[self._next_id] = student
        self._next_id += 1
        return asdict(student)

    def get_student(self, student_id: int) -> dict | None:
        student = self._students.get(student_id)
        return asdict(student) if student else None

    def list_students(self) -> list[dict]:
        return [asdict(student) for student in self._students.values()]

    def update_student(self, student_id: int, *, name: str | None = None, age: int | None = None, grade: str | None = None) -> dict | None:
        student = self._students.get(student_id)
        if not student:
            return None

        if name is not None:
            student.name = name
        if age is not None:
            student.age = age
        if grade is not None:
            student.grade = grade

        return asdict(student)

    def delete_student(self, student_id: int) -> bool:
        return self._students.pop(student_id, None) is not None
