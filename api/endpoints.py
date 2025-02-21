from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import json

router = APIRouter()

class MainRequest(BaseModel):
    param1: str
    param2: str

@router.post("/main")
async def main_endpoint(request: MainRequest):
    try:
        # implement functionality here
        print(f"param1={request.param1} param2={request.param2}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return 0

@router.get("/test")
async def test_endpoint():
    """Dummy endpoint to implement test functionality"""
    return {"status": "Test endpoint is working"}
