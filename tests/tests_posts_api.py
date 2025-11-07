import json
from pathlib import Path
from core.api_client import APIClient
from core.endpoints import Endpoints
from core.assertions import Assert

client = APIClient()
testdata = json.load(open(Path(__file__).parent.parent / "data/testdata.json"))

def test_create_post():
    payload = testdata["new_post"]
    response = client.post(Endpoints.POSTS, payload)
    Assert.status_code(response, 201)
    res = response.json()
    Assert.has_keys(res, ["id", "title", "body", "userId"])

def test_get_post_by_id():
    response = client.get(Endpoints.POSTS + "/1")
    Assert.status_code(response, 200)
    Assert.has_keys(response.json(), ["id", "title", "body"])
