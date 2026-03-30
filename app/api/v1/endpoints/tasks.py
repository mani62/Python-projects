from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_tasks():
    return {"message": "Tasks endpoint is working."}