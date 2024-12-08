import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aifund_backend.settings')
app = Celery('aifund_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Add your beat schedule after the app is defined
app.conf.beat_schedule = {
    'update-gainers-every-30-min': {
        'task': 'stock_analyser.tasks.update_premarket_gainers',
        'schedule': crontab(minute='*/1'),  # every 30 minutes
    },
}
