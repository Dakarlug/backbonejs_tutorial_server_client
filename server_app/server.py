"""

This emulate a basic server ,  to  allow fetching and storing data
into our Pgsql database. because this is a backbone demo 
we implement only two method a --add_todo--method to add 
a new toDo Item into the DataBase Pgsql , and a --get_todos() which
will return all data present into The database.

Thank To the powefull http://flask.pocoo.org/
And also http://www.sqlalchemy.org/download.html

"""
import sys , os, datetime
sys.path.insert(0,os.path.join(os.path.dirname(__file__), ".."))
from flask import Flask, jsonify,Response
from server_app.models import Base, ToDo , Session
from flask.ext.cors import origin 
from flask import request
from datetime import datetime
import json
app = Flask(__name__)

@app.route('/' ,methods =['GET'])
@origin('*')
def get_todos():
   tasks =  Session.query(ToDo).all()
   output = []
   for task in tasks:
      print ToDo.__table__.c
      row = {}
      for field in ToDo.__table__.c:
        print field
        row[str(field).replace('ToDos.','')] = str(getattr(task, 
                        str(field).replace('ToDos.',''), None))
      output.append(row)
   return jsonify(data = output)
  
@app.route('/add', methods=['POST'])
@origin('*')
def add_todo():
  for todo in  request.form:
      todo = eval(todo)
      print todo
      try:
	 date = datetime.date(['time'])
      except:
	 date = datetime.today()
      finally:
         Session.add(ToDo(do = todo['do'],time = date))
         Session.commit()
  return jsonify({"OK": "OK"})


if __name__ == "__main__":
    app.run(debug=True)



