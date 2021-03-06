from flask_server import db
from flask_server.dto.ToolDTO import ToolDTO
from flask_server.dto.ToolForTribulationDTO import ToolForTribulationDTO

def dbSearch(start, end, status):
    status = "%{}%".format(status)
    rs = db.session.query(ToolDTO, ToolForTribulationDTO).join(ToolForTribulationDTO).filter(ToolDTO.status.like(status),ToolForTribulationDTO.time_start >= start,ToolForTribulationDTO.time_end <= end,ToolDTO.is_deleted == False).order_by(ToolDTO.tool_id).all()
    result = []
    for i in rs:
        i[0].quantity = i[1].quantity
        result.append(i[0])
    return result

def dbRead():
    return ToolDTO.query.filter(ToolDTO.is_deleted == False).order_by(ToolDTO.tool_id).all()

def dbGetByTribulationID(tribulation_id):
    rs = db.session.query(ToolDTO,ToolForTribulationDTO).join(ToolForTribulationDTO).filter(ToolDTO.is_deleted == False, ToolForTribulationDTO.tribulation_id == tribulation_id).all()
    result = []
    for i in rs:
        i[0].quantity = i[1].quantity
        result.append(i[0])
    return result

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
        tool_to_delete.is_deleted = True
        db.session.commit()
        return id
    except Exception as e:
        db.session.rollback()
        raise e
    return -1

