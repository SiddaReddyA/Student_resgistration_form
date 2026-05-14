from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import Todo, Admin

app = FastAPI()

# ================= CORS =================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= CREATE TABLES =================

Base.metadata.create_all(bind=engine)

# ================= DATABASE SESSION =================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ================= HOME API =================

@app.get("/")
def home():

    return {
        "message": "FastAPI Running"
    }

# ================= GET STUDENTS =================

@app.get("/students")
def get_students(db: Session = Depends(get_db)):

    return db.query(Todo).all()

# ================= ADD STUDENT =================

@app.post("/students")
def add_student(student: dict, db: Session = Depends(get_db)):

    new_student = Todo(

        studentid = student["studentid"],

        name = student["name"],

        email = student["email"],

        pas = student["pas"],

        gender = student["gender"],

        date = student["date"],

        nation = student["nation"],

        language = student["language"],

        attendance = "Absent"
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return {
        "message": "Student Added"
    }

# ================= UPDATE STUDENT =================

@app.put("/students/{id}")
def update_student(
    id: int,
    student: dict,
    db: Session = Depends(get_db)
):

    existing_student = db.query(Todo).filter(
        Todo.id == id
    ).first()

    if not existing_student:

        return {
            "message": "Student Not Found"
        }

    existing_student.studentid = student["studentid"]

    existing_student.name = student["name"]

    existing_student.email = student["email"]

    existing_student.pas = student["pas"]

    existing_student.gender = student["gender"]

    existing_student.date = student["date"]

    existing_student.nation = student["nation"]

    existing_student.language = student["language"]

    db.commit()

    return {
        "message": "Student Updated"
    }

# ================= DELETE STUDENT =================

@app.delete("/students/{id}")
def delete_student(
    id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Todo).filter(
        Todo.id == id
    ).first()

    if not student:

        return {
            "message": "Student Not Found"
        }

    db.delete(student)

    db.commit()

    return {
        "message": "Student Deleted"
    }

# ================= LOGIN =================

@app.post("/login")
def login(user: dict, db: Session = Depends(get_db)):

    admin = db.query(Admin).filter(

        Admin.email == user["email"],

        Admin.password == user["password"]

    ).first()

    if admin:

        return {

            "message": "Login Success",

            "role": admin.role
        }

    return {

        "message": "Invalid Credentials"
    }

# ================= SIGNUP =================

@app.post("/signup")
def signup(user: dict, db: Session = Depends(get_db)):

    existing_user = db.query(Admin).filter(
        Admin.email == user["email"]
    ).first()

    if existing_user:

        return {
            "message": "Email Already Exists"
        }

    new_user = Admin(

        email = user["email"],

        password = user["password"],

        role = user["role"]
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "Signup Success"
    }

# ================= UPDATE ATTENDANCE =================

@app.put("/attendance/{id}")
def update_attendance(
    id: int,
    attendance: dict,
    db: Session = Depends(get_db)
):

    student = db.query(Todo).filter(
        Todo.id == id
    ).first()

    if not student:

        return {
            "message": "Student Not Found"
        }

    student.attendance = attendance["attendance"]

    db.commit()

    return {
        "message": "Attendance Updated"
    }