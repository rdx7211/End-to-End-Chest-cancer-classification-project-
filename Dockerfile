FROM python:3.8-slim-bookworm

RUN apt update -y && apt install -y awscli

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
