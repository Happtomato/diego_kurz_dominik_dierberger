import requests
import json

API_URL = "http://localhost:5050/suggest"


def test_valid_input():
    payload = {"ingredients": ["tomaten", "eier", "käse"]}
    response = requests.post(API_URL, json=payload)

    assert response.status_code == 200
    result = response.json()
    assert result is not None


def test_invalid_input():
    payload = {"ingredients": ""}
    response = requests.post(API_URL, json=payload)

    assert response.status_code == 400
    result = response.json()
    assert "error" in result


def test_missing_field():
    response = requests.post(API_URL, json={})
    assert response.status_code == 400
    result = response.json()
    assert "error" in result
