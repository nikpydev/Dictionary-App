import json

data = json.load(open("data.json"))


def search(w):
    if w in data:
        return data[w]
