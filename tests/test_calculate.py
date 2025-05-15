import pytest
import asyncio
from fastapi import HTTPException
from src.calculate import new_function

def run_async(func, *args, **kwargs):
    return asyncio.run(func(*args, **kwargs))

@pytest.mark.parametrize("operands, op, expected", [
    ([2, 3], "add", 5),
    ([10, 5], "-", 5),
    ([2, 3, 4], "*", 24),
    ([100, 2, 5], "/", 10),
])
def test_operations(operands, op, expected):
    result = run_async(new_function, operands, op)
    assert result["result"] == expected

def test_insufficient_operands():
    with pytest.raises(HTTPException) as exc_info:
        run_async(new_function, [2], "add")
    assert exc_info.value.status_code == 400
    assert "At least two operands" in exc_info.value.detail

def test_unsupported_operation():
    with pytest.raises(HTTPException) as exc_info:
        run_async(new_function, [1, 2], "power")
    assert exc_info.value.status_code == 400
    assert "Unsupported operation" in exc_info.value.detail

def test_division_by_zero():
    with pytest.raises(HTTPException) as exc_info:
        run_async(new_function, [10, 0], "/")
    assert exc_info.value.status_code == 400
    assert "Division by zero" in exc_info.value.detail
