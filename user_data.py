from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///user.db')

Base = declarative_base()

class User(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    name = Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_user(username,password):
    new_user = User(name=username,password=password)
    
    session.add(new_user)
    session.commit()
    return "Benutzer erfolgreich erstellt."
    
    
def authenticate_user(username, password):
    
    user = session.query(User).filter_by(name=username, password=password).first()
    if user:
        return True
    return False