from sqlalchemy import Column, Integer, String, Date
from database import Base

class Todo(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    studentid = Column(Integer)

    name = Column(String(255))

    email = Column(String(255))

    pas = Column(String(255))

    gender = Column(String(50))

    date = Column(Date)

    nation = Column(String(100))

    language = Column(String(100))