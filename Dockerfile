FROM python:3.11-slim

# Настройки для питона: не создаем кэш и сразу выводим логи в терминал
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Ставим Poetry
RUN pip install --no-cache-dir poetry

# Копируем только файлы зависимостей
COPY pyproject.toml poetry.lock* ./

# Ставим библиотеки без виртуального окружения
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Копируем все файлы проекта
COPY . .

# Копируем скрипт входа и даем ему права на запуск
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Назначаем скрипт главной командой
ENTRYPOINT ["/app/entrypoint.sh"]