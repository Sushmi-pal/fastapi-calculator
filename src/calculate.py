from fastapi import FastAPI, HTTPException

async def new_function(operands, op):
    if len(operands) < 2:
        raise HTTPException(status_code=400, detail="At least two operands are required.")

    if op == "add" or op == "+":
        result = sum(operands)

    elif op == "subtract" or op == "-":
        result = operands[0]
        for num in operands[1:]:
            result -= num

    elif op == "multiply" or op == "*":
        result = 1
        for num in operands:
            result *= num

    elif op == "divide" or op == "/":
        result = operands[0]
        try:
            for num in operands[1:]:
                result /= num
        except ZeroDivisionError:
            raise HTTPException(status_code=400, detail="Division by zero.")
    else:
        raise HTTPException(status_code=400, detail="Unsupported operation.")

    return {
        "operands": operands,
        "operation": op,
        "result": result
    }   
