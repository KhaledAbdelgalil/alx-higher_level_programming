#!/usr/bin/python3
"""
Contains City class and Base, an instance of declarative_base()
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Class defines City
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
