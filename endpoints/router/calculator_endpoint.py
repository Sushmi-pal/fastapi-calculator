from fastapi import APIRouter
from endpoints.model.model import CalcRequest
from src.calculate import new_function

router = APIRouter(
    prefix = "/assignment",
    tags = ["v1"]
)

@router.post("/calculated_data")
async def test_post(req: CalcRequest):

    operands = req.operands
    operation = req.operation.lower()

    output = await new_function(operands=operands, op=operation)

    return {
        "response": output
    }