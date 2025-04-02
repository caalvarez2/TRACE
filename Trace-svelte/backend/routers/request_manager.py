from fastapi import APIRouter, HTTPException
from models import RequestModel

router = APIRouter()

# In-memory store of requests (mock DB)
request_store: dict[int, RequestModel] = {}

@router.post("/create_request", response_model=RequestModel)
async def create_request(request: RequestModel):
    if request.id in request_store:
        raise HTTPException(status_code=400, detail="Request ID already exists")
    request_store[request.id] = request
    return request

@router.patch("/add_headers/{request_id}")
async def add_headers(request_id: int, headers: dict):
    if request_id not in request_store:
        raise HTTPException(status_code=404, detail="Request not found")
    request_store[request_id].headers.update(headers)
    return {"message": "Headers added", "headers": request_store[request_id].headers}

@router.patch("/set_payload/{request_id}")
async def set_payload(request_id: int, payload: dict):
    if request_id not in request_store:
        raise HTTPException(status_code=404, detail="Request not found")
    request_store[request_id].payload = payload
    return {"message": "Payload set", "payload": payload}

@router.patch("/update_headers/{request_id}")
async def update_headers(request_id: int, headers: dict):
    if request_id not in request_store:
        raise HTTPException(status_code=404, detail="Request not found")
    request_store[request_id].headers = headers
    return {"message": "Headers updated", "headers": headers}

@router.patch("/update_parameters/{request_id}")
async def update_parameters(request_id: int, parameters: dict):
    if request_id not in request_store:
        raise HTTPException(status_code=404, detail="Request not found")
    request_store[request_id].parameters = parameters
    return {"message": "Parameters updated", "parameters": parameters}

@router.patch("/update_payload/{request_id}")
async def update_payload(request_id: int, payload: dict):
    if request_id not in request_store:
        raise HTTPException(status_code=404, detail="Request not found")
    request_store[request_id].payload = payload
    return {"message": "Payload updated", "payload": payload}
