import pandas as pd
import requests
import json


df = pd.read_excel('liste_of_users.xlsx', index_col=None)


def create_users(row):
    print("Prénom:", row["Prénom"])
    print("Nom:", row["Nom"])
    response = requests.post("http://127.0.0.1:5000/users/", json=json.dumps({'first_name': row["Prénom"], 'last_name': row["Nom"]}))
    print(response.json())
    return row


print(list(df.columns.values))
df.apply(create_users, axis=1)

print({'first_name': 'last_name'})