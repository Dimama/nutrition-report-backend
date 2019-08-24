from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Patient, Record, Sipping, EN


class DBWrapper:
    def __init__(self, db_host, db_port, database, db_user, db_password):
        self.engine = create_engine(f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{database}")
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def add_patient(self, name):
        p = Patient(name=name)
        self.session.add(p)
        self.session.commit()

        return p.to_json()

    def get_patients(self):
        return [p.to_json() for p in self.session.query(Patient).all()]

    def add_record(self, data):
        sipping_ids = []
        for sipping in data["sipping"]:
            if not self._object_is_empty(sipping):
                sipping_ids.append(self._add_sipping(sipping))

        en_ids = []
        for en in data["EN"]:
            if not self._object_is_empty(en):
                en_ids.append(self._add_en(en))

        record = Record(patient=data["patient"],
                        date_from=data["dateFrom"],
                        date_to=data["dateTo"],
                        stool=data["stool"],
                        vomit=data["vomit"],
                        appetite=data["appetite"],
                        mucositis=data["mucositis"],
                        nausea=data["nausea"],
                        ration=data["ration"],
                        sipping=sipping_ids,
                        EN=en_ids,
                        components=data["components"],
                        interval=data["interval"],
                        needs=data["needs"],
                        doctor=data["doctor"])

        self.session.add(record)
        self.session.commit()

    def _add_sipping(self, data):
        mixture = data["mixture"]
        volume_one = data["volumeOne"]
        how_often = data["howOften"]
        taste = data["taste"]
        reason_for_change = data["reasonForChange"]

        sipping = self.session.query(Sipping).filter(Sipping.reason_for_change == reason_for_change,
                                                     Sipping.taste == taste,
                                                     Sipping.volume_one == volume_one,
                                                     Sipping.how_often == how_often,
                                                     Sipping.mixture == mixture).first()

        if sipping is None:
            sipping = Sipping(mixture=mixture,
                              volume_one=volume_one,
                              how_often=how_often,
                              taste=taste,
                              reason_for_change=reason_for_change)
            self.session.add(sipping)
            self.session.commit()

        return sipping.id

    def _add_en(self, data):
        tube = data["tube"]
        mixture = data["mixture"]
        volume_one = data["volumeOne"]
        how_often = data["howOften"]
        reason_for_change = data["reasonForChange"]

        en = self.session.query(EN).filter(EN.reason_for_change == reason_for_change,
                                           EN.tube == tube,
                                           EN.volume_one == volume_one,
                                           EN.how_often == how_often,
                                           EN.mixture == mixture).first()
        if en is None:
            en = EN(tube=tube,
                    mixture=mixture,
                    volume_one=volume_one,
                    how_often=how_often,
                    reason_for_change=reason_for_change)
            self.session.add(en)
            self.session.commit()

        return en.id

    @staticmethod
    def _object_is_empty(obj):
        for value in obj.values():
            if value != "":
                return False
        return True
