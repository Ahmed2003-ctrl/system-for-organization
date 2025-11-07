from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()
#-------------- Home Route -------------
@app.get("/")
def home():
    return {"message": "أهلاً بك في واجهة الطلاب! ✅"}

# -------------- Student Model --------------
class Student(BaseModel):
    id: int
    name: str
    grade: int

students = [
    Student(id=1, name="ali", grade=5),
    Student(id=2, name="ahmed", grade=3),
]

# -------------- Get all students --------------
@app.get("/students/")
def read_students():
    return students

# -------------- Create a new student --------------
@app.post("/students/")
def create_student(new_student: Student):
    students.append(new_student)
    return new_student

# -------------- Update a student --------------
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}

# uvicorn main:app --reload
# -------------- Delete a student --------------
@app.delete("/students/{student_id}")   
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student deleted "}
    return {"error": "Student not found"}


