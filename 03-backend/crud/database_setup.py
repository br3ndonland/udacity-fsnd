import os
import sys
from sqlalchemy import column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Tell Python that classes correspond to database tables for SQLAlchemy.
Base = declarative_base()

class Restaurant(Base):
    """docstring here
    """
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)


class MenuItem(Base):
    """docstring here
    """
    __tablename__ = 'menu_item '

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


# Specify database
engine = create_engine('sqlite:///restaurantmenu.db')
# Add new tables to database
Base.metadata.create_all(engine)
