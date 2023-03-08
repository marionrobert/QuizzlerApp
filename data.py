import requests

url = "https://opentdb.com/api.php"
params = {
    "amount": 20,
    "type": "boolean",
    "difficulty": "medium"
}

response = requests.get(url, params)
response.raise_for_status()
data = response.json()
question_data = data["results"]