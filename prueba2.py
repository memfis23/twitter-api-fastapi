import json

def pololo(user_id):
    with open("users.json", "r", encoding="utf-8") as f:
            data = json.loads(f.read())
            for user in data:
                if user_id == user['user_id']:
                    return {user_id: "It exits!"}
            else:
                return {user_id: "Doesn't It exits!"}

user_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
print(pololo(user_id))