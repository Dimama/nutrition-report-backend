from models import Base
from sqlalchemy import Column, Integer, String


class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def to_json(self):
        return {"name": self.name}
