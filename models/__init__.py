from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from .en import EN
from .patient import Patient
from .record import Record
from .sipping import Sipping
