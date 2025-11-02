# Dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

# Ejecuta migraciones y seeds antes de arrancar Gunicorn
CMD python manage.py migrate --noinput && \
    python manage.py seed_emissions && \
    gunicorn --bind 0.0.0.0:8000 emissionsBackend.wsgi:application
