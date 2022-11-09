# Test Rest API by using pytest , requests library(package)

import pytest
import requests

def test_get_all_users():
    url = "https://gorest.co.in/public/v2/users/"
    headers ={'Authorization': 'Bearer bd6648bc9827db267da725fab6f1c7332b77ec3cce9b99745e10118116c1568d'}
    payload={}
    # response = requests.request("GET",url= url,headers=headers,data=payload)
    response = requests.get(url=url,headers=headers)
    assert response.status_code == 200
    result = response.json()
    assert len(result) >0
    for i in result:
        assert i["id"] is not None
        assert i["name"] is not None
        assert i["email"] is not None