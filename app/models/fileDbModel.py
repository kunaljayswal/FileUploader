# Standard library imports
import uuid

# Third-party imports
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define your model class
class File(Base):
    __tablename__ = 'Files'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    filename =  Column(String)
    uploadtime =  Column(DateTime)
    virusscanresult =  Column(String)
    userdetails =  Column(String)