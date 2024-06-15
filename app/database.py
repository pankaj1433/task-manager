from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()


# Base class can directly imported from sqlalchemy as below.
# However, it doesn’t provide any custom functionality or shared behavior for models.
# Some advantages of custom Base class are:
#   - automatic table name generation on the basis of class name
#   - shared functionality
#   - custom meta data in one place
#   - easy to maintain


# TODO: Check why below is not working


# from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base
# @as_declarative()
# class Base:
#     id: any
#     __name__: str

#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name.lower()
