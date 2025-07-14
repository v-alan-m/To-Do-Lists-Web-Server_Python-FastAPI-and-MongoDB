from datetime import datetime
from fastapi import FastAPI, APIRouter, HTTPException
from configuration import collection
from database.models import Todo
from database.schemas import all_tasks
from bson.objectid import ObjectId

app = FastAPI()
router = APIRouter()


@router.get("/")
async def get_all_todos():
    data = collection.find({"is_deleted": False})  # Do not find entries that have been (soft) deleted.
    return all_tasks(data)


@router.post("/")
async def create_task(new_task: Todo):
    try:
        resp = collection.insert_one(dict(new_task))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error detected: {e}")


@router.put("/{task_id}")
async def update_task(task_id: str, updated_task: Todo):
    try:
        obj_id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id": obj_id, "is_deleted": False})
        if not existing_doc:
            return HTTPException(status_code=404, detail=f"Task does not exist")
        updated_task.updated_at = datetime.timestamp(datetime.now())
        resp = collection.update_one({"_id": obj_id}, {"$set": dict(updated_task)})
        return {"status_code": 200, "message": "Task updated successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error detected: {e}")


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:
        obj_id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id": obj_id, "is_deleted": False})
        if not existing_doc:
            return HTTPException(status_code=404, detail=f"Task does not exist")
        # deleted_one() can be used for hard delete.
        # update_one() with {"$set": {"is_deleted": True}} is a soft delete where the data can be recovered.
        resp = collection.update_one({"_id": obj_id}, {"$set": {"is_deleted": True}})
        return {"status_code": 200, "message": "Task deleted successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error detected: {e}")

app.include_router(router, prefix="")  # no prefix = root level


