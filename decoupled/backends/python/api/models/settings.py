from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Settings(BaseModel):
    __tablename__ = "settings"

    theme_id = Column(Integer, ForeignKey("theme.id"))
    notification_preference_id = Column(
        Integer,
        ForeignKey("notification_preference.id"),
    )


class Theme(BaseModel):
    __tablename__ = "theme"

    preference = Column(String)
    settings = relationship("Settings", back_populates="settings")


class NotificationPreference(BaseModel):
    __tablename__ = "notification_preference"

    preference = Column(String)
    settings = relationship("Settings", back_populates="settings")
