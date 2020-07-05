from flask import render_template, request, redirect, Blueprint
from flask_server.dao.TodoDAO import *
from flask_server import app
todo = Blueprint('todo', __name__, url_prefix='/todo')

@todo.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)
        try:
            dbCreate(new_task)
            return redirect('/')
        except Exception as e:
            print(e)
            return 500,"Server error" 
    else:
        tasks = dbRead()
        return render_template('index.html',tasks = tasks)


@todo.route('/delete/<int:id>')
def delete(id):
    try:
        dbDelete(id)
        return redirect('/')
    except Exception as e:
        print(e)
        return 500,"Server error" 

@todo.route('/update/<int:id>',methods=['POST','GET'])
def update(id):
    if request.method == 'POST':
        content = request.form['content']
        try: 
            dbUpdate(id,content)
            return redirect('/')
        except Exception as e:
            print(e)
            return 500,"Server error"
    else:
        return render_template('update.html',task = dbGet(id))
