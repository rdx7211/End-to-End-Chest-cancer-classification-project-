# Use a newer, lighter base image
FROM python:3.11-slim-bookworm

# Prevent Python from writing .pyc files and buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install AWS CLI and clean cache
RUN apt-get update && \
    apt-get install -y --no-install-recommends awscli && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy only requirements first to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies efficiently
RUN pip install --no-cache-dir -r requirements.txt

# Copy remaining files
COPY . .

# Expose port (optional, if your app runs a web server)
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
