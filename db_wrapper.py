from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Patient


class DBWrapper:
    def __init__(self, db_filename):
        self.engine = create_engine(f"sqlite:///{db_filename}")
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def add_patient(self, name):
        p = Patient(name=name)
        self.session.add(p)
        self.session.commit()

        return p.to_json()

    def get_patients(self):
        return [p.to_json() for p in self.session.query(Patient).all()]
