from sqlalchemy import Column, Integer, String, UniqueConstraint

from models import Base


class Sipping(Base):

    __tablename__ = "sipping"
    __table_args__ = (
        UniqueConstraint("mixture", "volume_one", "how_often", "taste", "reason_for_change",
                         name="sipping_unique_constraint"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    mixture = Column(String, nullable=False)
    volume_one = Column(String, nullable=False)
    how_often = Column(String, nullable=False)
    taste = Column(String, nullable=False)
    reason_for_change = Column(String, nullable=False)

    def to_json(self):
        return {"mixture": self.mixture,
                "volume_one": self.volume_one,
                "how_often": self.how_often,
                "taste": self.taste,
                "reason_for_change": self.reason_for_change}
