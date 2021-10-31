import json


email = "poto@example.com"
password = "holasoyfacundo"

with open("patas.json", "r", encoding="utf-8") as f:
    results = json.loads(f.read())

    for user in results:
        if email == user['email'] and password == user['password']:
            print('Login Succesfully!')
            break
    else:
        print("Login Unsuccesfully!")