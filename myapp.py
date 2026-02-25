import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    headers = {"content-type": "application/json"}
    r = requests.get(url=URL, headers=headers, data=json_data)
    print(r.status_code)
    print(r.text)
    data = r.json()
    print(data)


# get_data()


def post_data():
    data = {"name": "Urmi", "roll": 109, "city": "mirpur 10"}
    json_data = json.dumps(data)
    headers = {"content-type": "application/json"}

    r = requests.post(url=URL, headers=headers, data=json_data)
    print(r.status_code)
    print(r.text)
    data = r.json()
    print(data)


# post_data()


def update_data():
    data = {"id": 1, "city": "Sirajganj"}
    json_data = json.dumps(data)
    headers = {"content-type": "application/json"}

    r = requests.put(url=URL, headers=headers, data=json_data)
    # r = requests.put(url =f"{URL}{id}/" ,data = json_data)
    print(r.text) #This json string return from server 
    data = r.json()
    print(data) #Python dict


# update_data()


def delete_data():
    data = {"id": 4}
    json_data = json.dumps(data)
    headers = {"content-type": "application/json"}

    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


delete_data()
