from sqlalchemy import create_engine

from database.database import Base
from models import User

engine = create_engine("sqlite:///database/todos.db")

Base.metadata.create_all(engine)
