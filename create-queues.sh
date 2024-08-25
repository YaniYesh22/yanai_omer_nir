#!/bin/bash

echo "Creating queues..."

# Create the queue and capture the response
response=$(curl -s -X POST "http://sqs:9324?Action=CreateQueue&QueueName=data-raw-q")

# Print the response from the queue creation
echo "Response from queue creation:"
echo "$response"
