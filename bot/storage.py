import json
import os
from datetime import datetime

DB_PATH = "puffs.json"

def load_data():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

def add_puff(user_id: str):
    data = load_data()
    now = datetime.now().strftime("%Y-%m-%d")

    if user_id not in data:
        data[user_id] = {"total": 0, "daily": {}}

    user = data[user_id]
    user["total"] += 1
    user["daily"][now] = user["daily"].get(now, 0) + 1

    save_data(data)

def get_stats(user_id: str):
    data = load_data()
    now = datetime.now().strftime("%Y-%m-%d")

    if user_id not in data:
        return {"total": 0, "today": 0}

    user = data[user_id]
    return {
        "total": user.get("total", 0),
        "today": user["daily"].get(now, 0)
    }
