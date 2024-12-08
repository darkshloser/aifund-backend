FROM python:3.11-slim

WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y wget gnupg ca-certificates && rm -rf /var/lib/apt/lists/*

# Add Google’s official GPG key
RUN wget -qO - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -

# Add the Google Chrome repository
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list

# Install Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Collect static, etc. if needed
RUN python manage.py migrate

CMD ["gunicorn", "your_django_project.wsgi:application", "--bind", "0.0.0.0:8000"]
