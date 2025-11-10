FROM python:3.8-slim-bookworm

RUN apt update -y && apt install awscli -y
WORKDIR /app

# Copy all files first
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
