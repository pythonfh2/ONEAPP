import random
import string

import pytest
import requests
import json

import status
from status import status


def test_get_user_based_id_valid():
    url = "https://gorest.co.in/public/v2/users/4266"
    header = {
            'Authorization': 'Bearer bd6648bc9827db267da725fab6f1c7332b77ec3cce9b99745e10118116c1568d'
        }
    response = requests.get(url,header)
    assert response.status_code == 200
    result = response.json()
    assert len(result) > 0
    assert result["id"] == 4269
    assert result["name"] == "Sarvin Trivedi"
    assert result["email"] == "sarvin_trivedi@mclaughlin.com"
    assert result["gender"] == "male"
    assert result["status"] == "active"


#@pytest.mark.parametrize
def test_get_user_based_id_valid_multiple():
    id = 4269
    url = f"https://gorest.co.in/public/v2/users/"
    header = {
            'Authorization': 'Bearer bd6648bc9827db267da725fab6f1c7332b77ec3cce9b99745e10118116c1568d'
        }
    response = requests.get(url,header)
    assert response.status_code == 200
    result = response.json()
    assert len(result) > 0
    assert result["id"] ==  4269
    assert result["name"] == "Sarvin Trivedi"
    assert result["email"] ==  "sarvin_trivedi@mclaughlin.com"
    assert result["gender"] == "male"
    assert result["status"] == "active"

def test_get_invalid_user():
    url = "https://gorest.co.in/public/v2/users/42753533535"
    header = {
        'Authorization': 'Bearer bd6648bc9827db267da725fab6f1c7332b77ec3cce9b99745e10118116c1568d'
    }
    response = requests.get(url, header)
    assert response.status_code == 404
    result = response.json()
    assert result["message"] == "Resource not found"


def test_create_new_record():
    url = "https://gorest.co.in/public/v2/users/"
    header = {
              'Authorization': status.token,
              'Content-Type': 'application/json',
              'Cookie': status.cookie
             }

    name  = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=7))
    payload =json.dumps({
        "name": "PythonAPI",
        "email":status.newemail,
        "gender":"male",
        "status":"active"
    })
    response = requests.post(url,headers=header,data=payload)
    assert response.status_code == 201
    result = response.json()
    assert result["id"] is not None
    assert result["email"] == status.newemail
    assert result["gender"] == "male"
    assert result["status"] == "active"