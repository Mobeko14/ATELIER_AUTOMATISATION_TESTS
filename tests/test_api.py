import requests

def test_api_status():
    response = requests.get("https://api.agify.io?name=edouard")
    assert response.status_code == 200

def test_api_content():
    data = requests.get("https://api.agify.io?name=edouard").json()
    assert "age" in data
