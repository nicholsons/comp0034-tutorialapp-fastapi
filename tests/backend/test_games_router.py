from fastapi.testclient import TestClient

from backend.main import app

# Create an instance of the FastAPI test client
client = TestClient(app)


def test_get_games_ok():
    # Use the test client to make a requst to the GET /games endpoint (route)
    response = client.get("/games")
    # Use pytest assertion to verify that the response to the request has a status code of 200
    assert response.status_code == 200, "Should return status code 200"
