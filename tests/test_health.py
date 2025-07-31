import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app


def test_home():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
