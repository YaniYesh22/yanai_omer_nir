# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js and npm (if not already installed in python:3.8-slim)
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# Initialize npm and install Node.js dependencies
RUN npm i


CMD ["./node_modules/.bin/serverless", "offline", "start", "--config", "serverless.yml", "--dockerHost", "host.docker.internal", "--host", "0.0.0.0", "--noPrependStageInUrl"]
