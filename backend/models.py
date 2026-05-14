from sqlalchemy import Column, Integer, String, Float
from database import Base

class Todo(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    studentid = Column(String(255))

    name = Column(String(255))

    email = Column(String(255))

    pas = Column(String(255))

    gender = Column(String(255))

    date = Column(String(255))

    nation = Column(String(255))

    language = Column(String(255))

    attendance = Column(String(255))

    maths = Column(Integer, default=0)

    physics = Column(Integer, default=0)

    chemistry = Column(Integer, default=0)

    english = Column(Integer, default=0)

    computer = Column(Integer, default=0)

    total = Column(Integer, default=0)

    percentage = Column(Float, default=0)

    grade = Column(String(255), default="")

    result = Column(String(255), default="")
class Admin(Base):

    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(255))

    password = Column(String(255))

    role = Column(String(100))