import requests

url = "http://127.0.0.1:8000"

print(requests.get(f"{url}/reset").json())

actions = ["fill_missing", "remove_duplicates", "drop_missing"]

for a in actions:
    res = requests.post(f"{url}/step", params={"action": a})
    print(res.json())