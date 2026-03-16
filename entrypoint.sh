#!/bin/bash

# Останавливаем выполнение при любой ошибке
set -e

# Ждем базу
echo "Проверка доступности базы данных"

python << END
import socket
import time
import os

host = os.environ.get("POSTGRES_HOST", "db")
port = int(os.environ.get("POSTGRES_PORT", 5432))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect((host, port))
        s.close()
        break
    except socket.error:
        print("База еще не готова")
        time.sleep(1)
END

echo "postgres доступен"

# Накатываем миграции
# Теперь таблицы создадутся сами при старте контейнера
echo "Запуск миграций alembic"
alembic upgrade head

# Запускаем команду.
# Это передает управление команде, написанной в docker-compose
echo "запуск"
exec "$@"