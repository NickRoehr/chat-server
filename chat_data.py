from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///chat.db')

Base = declarative_base()

class Chat(Base):
    __tablename__='chat'
    id = Column(Integer,primary_key=True)
    message = Column(String,nullable=False)
    timestemp = Column(String,nullable=False)
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_message(message):
    new_message = Chat(message=message,timestemp=datetime.now())
    
    session.add(new_message)
    session.commit()
    