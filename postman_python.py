import requests

def test_endpoint(name, endpoint):
    url = f"http://localhost:5299/api/{endpoint}"
    response = requests.get(url)
    print(f"Testing {name}: {response.status_code}")
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")

endpoints = {
    "User": "User",
    "Character": "Character",
    "Inventory": "Inventory"
}

for name, endpoint in endpoints.items():
    test_endpoint(name, endpoint)
