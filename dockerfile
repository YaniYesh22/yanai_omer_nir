# Use an official Node.js runtime, Node 18 in this case
FROM node:18

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the package.json and install dependencies
COPY package*.json ./
RUN npm install

# Install the Serverless Framework and serverless-offline-sqs globally
RUN npm install -g serverless-offline serverless-offline-sqs

# Copy the rest of the application code
COPY . .

# Expose the port that serverless-offline will run on
EXPOSE 3001

# Start the Serverless Offline service
CMD ["serverless-offline", "--host", "0.0.0.0", "--port", "3001"]
