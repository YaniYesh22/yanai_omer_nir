# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the main requirements.txt file and install packages
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV AWS_ACCESS_KEY_ID=local
ENV AWS_SECRET_ACCESS_KEY=local
ENV AWS_DEFAULT_REGION=us-west-1
ENV AWS_ENDPOINT_URL=http://sqs:9324

# Copy the application code into the container
COPY . /app

# Expose the port based on the service
WORKDIR /app/scraper

# Command to run the application
CMD ["uvicorn", "spotify:app", "--host", "0.0.0.0", "--port", "3000"]
