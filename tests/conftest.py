import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock

from app.main import app
from app.api.dependencies import get_price_repo # импорт зависимости


@pytest_asyncio.fixture(scope="function")
async def mock_repo():
    """Создаем мок для репозитория"""
    repo = AsyncMock()
    return repo


@pytest_asyncio.fixture(scope="function")
async def ac(mock_repo):
    """
    Клиент для тестов. 
    Тут мы подменяем реальный репозиторий на наш фейк (mock_repo).
    """
    # Pаменяем реальный репозиторий на мок
    app.dependency_overrides[get_price_repo] = lambda: mock_repo
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
    
    # После теста чистим за собой, чтобы другие тесты не сломались
    app.dependency_overrides.clear()