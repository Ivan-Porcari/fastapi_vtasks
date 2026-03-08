from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types  import String, Integer, Text, Enum
from .database import Base
from tasks.schemes import StatusType


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20)) #, unique=True
    description = Column(Text())
    status = Column(Enum(StatusType))
    category_id = Column(Integer, ForeignKey('categories.id'), nullable = False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    surname = Column(String(20))
    email = Column(String(50))
    website = Column(String(50))