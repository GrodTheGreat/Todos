from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    username = Column(String)
    given_name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    email = Column(String)
    password_hash = Column(String)
    is_active = Column(Boolean)
    last_login = Column(DateTime)
    tags = relationship("Tag", back_populates="user")
    settings = relationship("Settings", back_populates="user")
    activity_logs = relationship("ActivityLog", back_populates="user")
