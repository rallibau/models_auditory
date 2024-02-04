from rest_framework import status
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def client() -> APIClient:
    return APIClient()


class TestHealthEndpoint:
    def test_health_endpoint(self, client: APIClient):
        response = client.get("/health/")

        assert response.status_code == status.HTTP_200_OK
