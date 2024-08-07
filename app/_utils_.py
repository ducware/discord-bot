import json
import os


def load_data():
  if os.path.exists("./name.json"):
    with open("name.json", "r") as f:
      return json.load(f)
  return {"name": {}, "isAdmin": {}, "command": {"default": "!"}}


def save_data(data):
  with open("name.json", "w") as f:
    json.dump(data, f, indent=4)


def load_name(user_id):
  data = load_data()
  return data["name"].get(user_id, None)


def load_leaderboard():
  if os.path.exists("./leaderboard.json"):
    with open("leaderboard.json", "r") as f:
      return json.load(f)
  return {}


def save_leaderboard(data):
  with open("leaderboard.json", "w") as f:
    json.dump(data, f, indent=4)


def increment_user_score(user_id):
  data = load_leaderboard()
  if user_id in data:
    data[user_id] += 1
  else:
    data[user_id] = 1
  save_leaderboard(data)


def get_leaderboard():
  data = load_leaderboard()
  return sorted(data.items(), key=lambda x: x[1], reverse=True)
