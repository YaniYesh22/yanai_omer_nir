# Use the official Python image from the Docker Hub based on Debian Bullseye
FROM python:3.8-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y curl gnupg2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add NodeSource GPG key
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /usr/share/keyrings/nodesource.gpg

# Add NodeSource repository
RUN echo "deb [signed-by=/usr/share/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x bullseye main" | tee /etc/apt/sources.list.d/nodesource.list

# Update Debian keyring
RUN apt-get update && \
    apt-get install -y debian-archive-keyring && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Verify Node.js and npm installation
RUN node --version && npm --version

# Initialize npm and install Node.js dependencies
RUN npm install

CMD ["./node_modules/.bin/serverless", "offline", "start", "--config", "serverless.yml", "--dockerHost", "host.docker.internal", "--host", "0.0.0.0", "--noPrependStageInUrl"]