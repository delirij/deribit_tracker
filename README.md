# Deribit Price Tracker

**Deribit Price Tracker** — это сервис для автоматического мониторинга курсов криптовалют (**BTC** и **ETH**) с биржи Deribit. Система каждую минуту собирает данные и предоставляет их через удобное **REST API**.


---

## Технологический стек

* **Backend**: Python 3.11, FastAPI
* **Database**: PostgreSQL + SQLAlchemy (Async)
* **Task Manager**: Celery + Redis (broker)
* **Migrations**: Alembic
* **Environment**: Docker & Docker Compose
* **Testing**: Pytest + HTTPX (AsyncClient)

---

## Быстрый запуск

Благодаря автоматизации через `entrypoint.sh`, проект разворачивается **одной командой**. Вам не нужно вручную создавать таблицы или запускать миграции.

1.  **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/delirij/deribit_tracker.git
    cd deribit_tracker
    ```

2.  **Настройте переменные окружения**:
    Создайте файл **`.env`** в корневой папке и добавьте туда следующие настройки:
    ```env
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=deribit_tracker
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

    CELERY_BROKER_URL=redis://redis:6379/0
    ```

3.  **Запустите проект**:
    ```bash
    docker compose up -d --build
    ```

> **Примечание**: При первом старте система автоматически дождется готовности базы данных и применит все миграции Alembic через скрипт входа.

---

## Документация API

После запуска интерактивная документация (Swagger) доступна по адресу:
 **[http://localhost:8000/docs](http://localhost:8000/docs)**

### Основные методы (обязательный query-параметр `ticker`)

* **`GET /prices/all`** — Возвращает всю историю сохранений по указанной валюте (например, `btc_usd`).
* **`GET /prices/latest`** — Возвращает самую последнюю актуальную цену из базы.
* **`GET /prices/filter`** — Поиск цен с фильтрацией по времени (принимает `date_from` и `date_to` в формате UNIX timestamp).

---

## Тестирование

Для проверки корректности работы реализованы **Unit-тесты** с использованием моков (база данных для тестов не требуется).

**Запуск тестов из локального окружения:**
```bash
pytest
