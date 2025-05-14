from pydantic import BaseModel
from typing import List


class CalcRequest(BaseModel):
    operands: List[float]
    operation: str
