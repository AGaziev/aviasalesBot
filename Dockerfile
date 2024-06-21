FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    python3-venv \
    postgresql-client \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv venv

RUN . venv/bin/activate && pip install --upgrade pip setuptools wheel && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PATH="/app/venv/bin:$PATH"

# Команда по умолчанию (может быть переопределена в docker-compose.yaml)
CMD ["python","./app.py"]
