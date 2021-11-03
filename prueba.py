import json

user_id = "3fa85f64-5717-4562-b3fc-2c963f66afa9"
with open("copia_users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        for user in results:
            if user["user_id"] == user_id:
                results.remove(user)
                break
        f.seek(0)
        f.write(json.dumps(results))
        print("user removed")

# with open("users.json", "r+", encoding="utf-8") as f:
#         results = json.loads(f.read())
#         user_id = str(user_id)
#         for i, user in enumerate(results):
#             if user["user_id"] == user_id:
#                 results.pop(i)
#                 break
#         f.seek(0)
#         f.write(json.dumps(results))
#         print("user removed")