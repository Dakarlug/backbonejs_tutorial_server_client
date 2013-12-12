"""
setup database , for exemple for sqlite call

>>> python setup_db.py

And you get output


CREATE TABLE "ToDos" (
        id INTEGER NOT NULL,
        do VARCHAR,
        time DATE,
        done BOOLEAN,
        PRIMARY KEY (id),
        CHECK (done IN (0, 1))
)

"""
import sys , os, datetime
sys.path.insert(0,os.path.join(os.path.dirname(__file__), ".."))
from  server_app.models import Base, ToDo , Session

def sqlite_setup():

    # add one data
    add_some_data()
    
    #retreive data added
    add_some_data_success()
   
def postgress_setup():
    pass

def add_some_data():
  
    Session.add(ToDo(do  ='Allaiter bebe',
                     time= datetime.datetime.today(),
                     done=False))
    Session.commit()
            
def add_some_data_success():
    print "=========DATA========"
    print Session.query(ToDo).all()
    

if __name__ =="__main__":
    sqlite_setup()
    
    




