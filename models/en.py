from sqlalchemy import Column, Integer, String, UniqueConstraint

from models import Base


class EN(Base):

    __tablename__ = "enteral_nutrition"
    __table_args__ = (
        UniqueConstraint("mixture", "tube", "how_often", "volume_one", "reason_for_change",
                         name="enteral_nutriton_unique_constraint"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    tube = Column(String, nullable=False)
    mixture = Column(String, nullable=False)
    volume_one = Column(String, nullable=False)
    how_often = Column(String, nullable=False)
    reason_for_change = Column(String, nullable=False)

    def to_json(self):
        return {"tube": self.tube,
                "mixture": self.mixture,
                "volume_one": self.volume_one,
                "how_often": self.how_often,
                "reason_for_change": self.reason_for_change}
