FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files (including your_django_project and stock_scraper)
COPY . /app/

# The default command runs the Celery worker
CMD ["celery", "-A", "aifund_backend", "worker", "-l", "info"]
