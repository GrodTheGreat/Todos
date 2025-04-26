from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class ActivityLog(BaseModel):
    __tablename__ = "activity_log"

    user_id = Column(Integer, ForeignKey("user.id"))
    action_id = Column(Integer, ForeignKey("activity.id"))
    timestamp = Column(DateTime)


class Activity(BaseModel):
    __tablename__ = "activity"

    name = Column(String)
    activity_logs = relationship("ActivityLog", back_populates="activity")
