import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Blog_User(Base):
    __tablename__ = "blog_User"
    id = Column(Integer, primary_key=True)
    user = Column(String(20), nullable=False, unique=True)
    first_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    id_post = Column(Integer)
    id_user = Column(Integer, ForeignKey('blog_User.id'))
    blog_user = relationship(Blog_User)

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, ForeignKey('favorite.id_post'), primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    home_world = Column(String(250), nullable=False)
    home_world_id = Column(Integer, ForeignKey('planet.id'))
    favorite = relationship(Favorite)

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, ForeignKey('favorite.id_post'), primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    population = Column(Integer)
    favorite = relationship(Favorite)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')