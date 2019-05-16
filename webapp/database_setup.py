import sys
#for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String
#for configuration and class code
from sqlalchemy.ext.declarative import declarative_base
#for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship
#for configuration
from sqlalchemy import create_engine

#create declarative_base instance
Base = declarative_base()


class Grammar(Base):
   __tablename__ = 'grammar_items'
   id = Column(Integer, primary_key=True)
   grammar = Column(String(20), nullable=False)

   def __init__(s):
      sentence = s

class Sentence(Base):
   __tablename__ = 'sentences'
   id = Column(Integer, primary_key=True)
   sentence = Column(String(250), nullable=False)
   grammar_item = Column(String(20))
   blank_pos_beg = Column(Integer)
   blank_pos_end = Column(Integer)

   def __init__(s, g, b, e):
      sentence = s
      grammar_item = g
      blank_pos_beg = b
      blank_pos_end = e



# #creates a create_engine instance at the bottom of the file
# engine = create_engine('sqlite:///sentences.sqlite3')

# Base.metadata.create_all(engine)