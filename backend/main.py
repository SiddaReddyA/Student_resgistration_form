from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import Todo,Admin

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create Tables
Base.metadata.create_all(bind=engine)

# Database Session
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# Home API
@app.get("/")
def home():

    return {
        "message": "FastAPI Running"
    }

# Get Students
@app.get("/students")
def get_students(db: Session = Depends(get_db)):

    return db.query(Todo).all()

# Add Student
@app.post("/students")
def add_student(student: dict, db: Session = Depends(get_db)):

    new_student = Todo(

        studentid = student["studentid"],

        name = student["name"],

        email=student["email"],
        pas=student["pas"],
        gender=student["gender"],
        date=student["date"],
        nation=student["nation"],
        language=student["language"]
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return {
        "message": "Student Added"
    }
@app.get("/students")
def get_students(db: Session = Depends(get_db)):

    return db.query(Todo).all()
@app.put("/students/{id}")
def update_student(id: int, student: dict, db: Session = Depends(get_db)):

    existing_student = db.query(Todo).filter(Todo.id == id).first()

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
@app.delete("/students/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):

    student = db.query(Todo).filter(Todo.id == id).first()

    db.delete(student)

    db.commit()

    return {
        "message": "Student Deleted"
    }
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