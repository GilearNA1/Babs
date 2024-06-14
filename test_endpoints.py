import requests

base_url = 'http://localhost:5299/api'

endpoints = {
    "Get Users": "/User",
    "Get Characters": "/Character",
    "Get Inventory": "/Inventory",
    "Get Achievements": "/Achievement",
    "Get Quests": "/Quest",
    "Get Skills": "/Skill",
    "Get World": "/World",
    "Get NPCs": "/NPC",
    "Get Logs": "/Logging",
    "Get Notifications": "/Notification",
    "Get Leaderboard": "/Leaderboard",
    "Get Analytics": "/Analytics",
    "Get Settings": "/Settings",
    "Get Home": "/Home"
}

headers = {
    'Content-Type': 'application/json'
}

def test_endpoint(name, endpoint):
    url = base_url + endpoint
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"{name} - Success: {response.json()}")
    else:
        print(f"{name} - Failed: {response.status_code} - {response.text}")

for name, endpoint in endpoints.items():
    test_endpoint(name, endpoint)
