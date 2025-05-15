# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install test dependencies
RUN pip install pytest

# Copy the project files
COPY . .

# Exclude env directory (just in case)
RUN rm -rf env

# Command to run the FastAPI app
CMD ["uvicorn", "endpoints.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
