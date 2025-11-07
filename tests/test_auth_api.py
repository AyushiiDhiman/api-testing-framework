from core.api_client import APIClient
from core.assertions import Assert

client = APIClient()

def test_dummy_auth():
    response = client.get("/posts/1")
    Assert.status_code(response, 200)
