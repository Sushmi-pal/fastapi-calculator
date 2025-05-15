## FASTAPI - CALCULATOR

A simple calculator API supporting basic arithmetic operations — addition, subtraction, multiplication, and division — built with FastAPI.

___

## Prerequisites

- Python
- pip package manager
- Docker 
___

## To run locally
1. Clone the repository
```
git clone git@github.com:Sushmi-pal/fastapi-calculator.git
```

2. Install Dependencies
```
pip install -r requirements.txt
```

3. Run the FastAPI app
```
uvicorn endpoints.main:app --host 0.0.0.0 --port 8000 --reload
```
___

## To run with Docker

1. Build the Docker image
```
docker build -t fastapi-app:v1.0.0 .
```

2. Run the Docker container
```
docker run -p 8000:8000 fastapi-app:v1.0.0
```




