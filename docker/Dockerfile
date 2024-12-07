FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Collect static, etc. if needed
RUN python manage.py migrate

CMD ["gunicorn", "your_django_project.wsgi:application", "--bind", "0.0.0.0:8000"]
