import requests
import json

data = {
    "user_a_id": 1,
    "user_b_id": 2,
    "amount": 100
}

print(requests.post("http://127.0.0.1:5000/market/trade", data=json.dumps(data),
                    headers={"Content-Type": "application/json"}))
