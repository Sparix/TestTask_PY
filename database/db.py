import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQL_ALCHEMY_DB = f"postgresql+psycopg2://postgres:postgres@db/DataTask"
# SQL_ALCHEMY_DB = f"postgresql+psycopg2://postgres:postgres@localhost/DataTask"

engine = create_engine(
    SQL_ALCHEMY_DB,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoFlush=False,
    bind=engine,
)

Base = declarative_base()
