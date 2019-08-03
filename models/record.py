from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import ARRAY

from models import Base, Patient


class Record(Base):

    __tablename__ = "records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient = Column(String, ForeignKey("patients.name"), nullable=False)
    date_from = Column(String, nullable=False)
    date_to = Column(String, nullable=False)
    stool = Column(String, nullable=False)
    vomit = Column(String, nullable=False)
    appetite = Column(String, nullable=False)
    mucositis = Column(String, nullable=False)
    nausea = Column(String, nullable=False)
    ration = Column(String, nullable=False)
    sipping = Column(ARRAY(String), nullable=False)
    EN = Column(ARRAY(String), nullable=False)
    components = Column(String, nullable=False)
    interval = Column(String, nullable=False)
    needs = Column(String, nullable=False)
    doctor = Column(String, nullable=False)
