from fastapi.testclient import TestClient
from ..main import api


client = TestClient(api.app)


def test_main_resource():
    response_auth = client.get("/")
    assert response_auth.status_code == 200


def test_child_resource():
    response_auth = client.get("/api/index")
    assert response_auth.status_code == 200
