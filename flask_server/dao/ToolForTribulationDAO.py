from flask_server import db

from flask_server.dto.ToolDTO import ToolDTO
from flask_server.dto.ToolForTribulationDTO import ToolForTribulationDTO as tft

from flask_server.dao import TribulationDAO
from flask_server.dao import ToolDAO

def enoughQuantity(tool_id, tribulation_id, quantity):
    tribulation = TribulationDAO.dbGet(tribulation_id)
    tool_quantity = ToolDAO.dbGet(tool_id).quantity
    result = False
    try:
        list_tool = tft.query.filter(tft.tool_id == tool_id, tft.time_start >= tribulation.time_start, tft.time_end <= tribulation.time_end).all()
        #sum quantity
        sum = 0
        for tool in list_tool:
            sum += tool.quantity
        print('tool quantity = ', tool_quantity)
        print('sum           = ', sum)
        print('quantity      = ', quantity)
        result = (tool_quantity >= (sum + quantity))
    except Exception as e:
        raise e
    return result
        

def dbCreate(new_tool):
    result = False
    try:
        if enoughQuantity(new_tool.tool_id, new_tool.tribulation_id, new_tool.quantity):
            db.session.add(new_tool)
            db.session.flush()
            db.session.commit()
            result = True
    except Exception as e:
        db.session.rollback()
        raise e
    return result

def dbUpdate(update_tool):
    data = update_tool.serialize()
    result = False
    try: 
        tool_to_update = tft.query.filter(tft.tool_id == update_tool.tool_id, tft.tribulation_id == update_tool.tribulation_id).first()
        if enoughQuantity(update_tool.tool_id, update_tool.tribulation_id, update_tool.quantity):
            tool_to_update.merge(data)
            db.session.commit()
            result = True
    except Exception as e:
        db.session.rollback()
        raise e
    return result

def dbDelete(tool_id, tribulation_id):
    result = False
    try:
        tool_to_delete = tft.query.filter(tft.tool_id == tool_id, tft.tribulation_id == tribulation_id).first()
        db.session.delete(tool_to_delete)
        db.session.commit()
        result = True
    except Exception as e:
        db.session.rollback()
        raise e
    return result


     