from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Todo(BaseModel):
    __tablename__ = "todo"

    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(String)
    description = Column(String, nullable=True)
    due = Column(DateTime, nullable=True)
    is_complete = Column(Boolean)
    priority_id = Column(Integer, ForeignKey("priority.id"), nullable=True)
    status_id = Column(Integer, ForeignKey("status.id"), nullable=True)
    tags = relationship("Tag", back_populates="todo")
    reminder = relationship("Reminder", back_populates="todo")


class Tag(BaseModel):
    __tablename__ = "tag"

    user_id = Column(Integer, ForeignKey("user.id"))
    todo_id = Column(Integer, ForeignKey("todo.id"))
    name = Column(String)


class Reminder(BaseModel):
    __tablename__ = "reminder"

    todo_id = Column(Integer, ForeignKey("todo.id"))
    remind_at = Column(DateTime)


class Priority(BaseModel):
    __tablename__ = "priority"

    name = Column(String)
    level = Column(Integer)
    todos = relationship("Todo", back_populates="priority")


class Status(BaseModel):
    __tablename__ = "status"

    name = Column(String)
    level = Column(Integer)
    todos = relationship("Todo", back_populates="status")
