import pandas as pd
import requests


df = pd.read_excel("liste_of_users.xlsx", index_col=None)


def create_users(row):
    print("Prénom:", row["Prénom"])
    print("Nom:", row["Nom"])
    url = "http://127.0.0.1:5000/users/"
    headers = {"content-type": "application/json"}
    cre_users = {"first_name": row["Prénom"], "last_name": row["Nom"]}
    response = requests.post(url, json=cre_users, headers=headers)
    print(response.json())
    print(response.status_code)
    return row


df.apply(create_users, axis=1)

print({"first_name": "last_name"})
