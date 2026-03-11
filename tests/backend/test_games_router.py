from fastapi.testclient import TestClient

from backend.core.config import get_settings
from backend.main import create_app

app = create_app()

# Create an instance of the FastAPI test client
client = TestClient(app)


def test_get_games_ok():
    # Use the test client to make a requst to the GET /games endpoint (route)
    response = client.get("/games")
    # Use pytest assertion to verify that the response to the request has a status code of 200
    assert response.status_code == 200, "Should return status code 200"


def test_get_games_by_id_ok():
    response = client.get("/games/1")
    assert response.status_code == 200, "Should return status code 200"
    assert response.json().get("id") == 1, "The response should include in the JSON {'id': 1}"
