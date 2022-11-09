import http.client
import json

import requests
from numpy.distutils.conv_template import header


def test_create_new_record():
    url = "https://reqres.in/api/unknowi=10"

    headers = {
        'Cookie': '',
        'Content-Type': 'application/json'
    }

    pyload = json.dumps({
        "name": "cerulean",
        "year": 2000,
        "color": "#98B2D1",
        "pantone_value": "15-4020",
    })
    response = requests.post(url,headers=header)
    assert response.status_code == 201
    result = response.json()
    assert len(result) > 0
    assert result["year"] == 2000
    assert result["name"] == "cerulean"
    assert result["color"] == "#98B2D1"
    assert result["pantone_value"] == "15-4020"
    assert result["id"] == "586"
