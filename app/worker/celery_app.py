from celery import Celery
from celery.schedules import crontab

from app.core.config import settings

# Инициализация приложения Celery с брокером сообщений Redis
app = Celery("deribit_updater", broker=settings.CELERY_BROKER_URL)

# Настройка расписания для периодического запуска задач
app.conf.beat_schedule = {
    'get_ticker_price_every_minute': {
        'task': 'get_ticker_price',
        'schedule': crontab(minute='*'),
    },
}

# Автоматический поиск задач
app.autodiscover_tasks(['app.worker'])