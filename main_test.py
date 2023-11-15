from collections.abc import AsyncGenerator, Generator

import pytest
from httpx import AsyncClient

from main import app


@pytest.fixture(scope="session")
def anyio_backend() -> Generator[str, None, None]:
    yield "asyncio"


@pytest.fixture(scope="session")
async def async_client(anyio_backend: str) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


async def test_root_message(async_client: AsyncClient):
    response = await async_client.get("/")
    assert response.json() == {"message": "Welcome to my awesome presentation!"}
