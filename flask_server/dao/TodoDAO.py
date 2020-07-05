from flask_server.dto.model import Todo
from flask_server import db

def dbCreate(new_task):
    try:
        db.session.add(new_task)
        db.session.flush()
        db.session.commit()
        return new_task.id
    except Exception as e:
        raise e
        return -1

def dbRead():
    return Todo.query.order_by(Todo.date_create).all()

def dbGet(id):
    return Todo.query.get(id)

def dbUpdate(id,content):
    task_to_update = Todo.query.get_or_404(id)
    try: 
        task_to_update.content = content
        db.session.commit()
        return True
    except Exception as e:
        raise e
        return False
    

def dbDelete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return id
    except Exception as e:
        raise e
        return -1
