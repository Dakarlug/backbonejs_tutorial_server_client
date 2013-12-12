from sqlalchemy import Column, Integer, String , Date , Boolean 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

import sys , os, datetime
sys.path.insert(0,os.path.join(os.path.dirname(__file__), ".."))

class ToDo(Base):
    __tablename__ = 'ToDos'
    id   = Column(Integer, primary_key=True)
    do   = Column(String)
    time = Column(Date)
    done = Column(Boolean)

    def __repr__(self):
        return "<User(do='%s', time='%s', done='%s')>" % (
                                self.do, self.time, self.done)


#engine  = create_engine('sqlite:///:memory:', echo=True)
engine  = create_engine('postgresql://postgres:test@localhost:5432/mypgdb')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session = Session()
    







