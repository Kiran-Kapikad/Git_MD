# Use official Python 3.10 slim base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

#Copy the code
 COPY . .

# Install system dependencies if needed
 RUN apt-get update && apt-get install -y python3-dev libpq-dev
 COPY requirements.txt .
 RUN pip install --no-cache-dir -r requirements.txt
 EXPOSE 5000

# Default command (can be overridden)
CMD ["python3","app.py"]

