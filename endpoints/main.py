from fastapi import FastAPI
from endpoints.router import calculator_endpoint

app = FastAPI()

app.include_router(calculator_endpoint.router)