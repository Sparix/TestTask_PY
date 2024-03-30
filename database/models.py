from sqlalchemy import Column, Integer, String

from database.db import Base


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    population = Column(Integer, nullable=False)
    region = Column(String(255), nullable=False)