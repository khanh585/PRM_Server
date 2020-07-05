from flask_server import db
from flask_server.dto.ToolDTO import ToolDTO


def dbRead():
    return ToolDTO.query.order_by(ToolDTO.name).all()

def dbGet(tool_id):
    return ToolDTO.query.get(tool_id)

def dbCreate(new_tool):
    try:
        db.session.add(new_tool)
        db.session.flush()
        db.session.commit()
        return new_tool.tool_id
    except Exception as e:
        db.session.rollback()
        raise e
    return -1

def dbUpdate(id,data):
    data = data.serialize()
    try: 
        tool_to_update = ToolDTO.query.get_or_404(id)
        tool_to_update.merge(data)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e
    return False

def dbDelete(id):
    try:
        tool_to_delete = ToolDTO.query.get_or_404(id)
        db.session.delete(tool_to_delete)
        db.session.commit()
        return id
    except Exception as e:
        db.session.rollback()
        raise e
    return -1