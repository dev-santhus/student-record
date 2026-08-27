from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


app = FastAPI(title="Student Record CRUD API")


class StudentBase(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=1)
    grade: str = Field(..., min_length=1)


class StudentCreate(StudentBase):
    id: int = Field(..., ge=1)


class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    age: Optional[int] = Field(None, ge=1)
    grade: Optional[str] = Field(None, min_length=1)


class Student(StudentBase):
    id: int


students: Dict[int, Student] = {}


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate) -> Student:
    if student.id in students:
        raise HTTPException(status_code=409, detail="Student with this id already exists")

    created_student = Student(**student.model_dump())
    students[student.id] = created_student
    return created_student


@app.get("/students", response_model=List[Student])
def list_students() -> List[Student]:
    return list(students.values())


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int) -> Student:
    student = students.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student_update: StudentUpdate) -> Student:
    existing_student = students.get(student_id)
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")

    update_data = student_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    updated_student = existing_student.model_copy(update=update_data)
    students[student_id] = updated_student
    return updated_student


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int) -> Response:
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    del students[student_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
