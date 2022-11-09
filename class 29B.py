import json
from tkinter import N

import requests
import string
import random


def test_get_user_based_id_valid_multiple():
    id = 4234,
    url = f"https://gorest.co.in/public/v2/users/"
    header = {
        'Authorization': 'Bearer bd6648bc9827db267da725fab6f1c7332b77ec3cce9b99745e10118116c1568d'
    }
    payload = json.dumps({
        "name": "cerulean",
        "year": 2000,
        "color": "#98B2D1",
        "pantone_value": "15-4020"
    })

    name = ''.join(random.choices(string.ascii_letters, k=N))

    response = requests.get(url, headers=header)
    assert response.status_code == 201
    result = response.json()
    assert len(result) > 0
    assert result["id"] is not None
    assert result["name"] == "Jyotsana Katri III"
    assert result["email"] == "iii_jyotsana_khatri@christiansen-bode.biz"
    assert result["gender"] == "male"
    assert result["status"] == "inactive"
