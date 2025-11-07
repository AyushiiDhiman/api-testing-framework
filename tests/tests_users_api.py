import pytest
from core.api_client import APIClient
from core.endpoints import Endpoints
from core.assertions import Assert
from jsonschema import validate

client = APIClient()

def test_get_users():
    response = client.get(Endpoints.USERS)
    Assert.status_code(response, 200)
    
    users = response.json()
    Assert.has_keys(users[0], ["id", "name", "email"])
    Assert.response_time(response)


def test_user_schema():
    response = client.get(Endpoints.USERS + "/1")
    Assert.status_code(response, 200)
    
    data = response.json()

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "email": {"type": "string"}
        },
        "required": ["id", "name", "email"]
    }

    validate(data, schema)
