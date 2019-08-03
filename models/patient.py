from sqlalchemy import Column, Integer, String

from models import Base


class Patient(Base):

    __tablename__ = "patients"

    name = Column(String, primary_key=True)

    def to_json(self):
        return {"name": self.name}
