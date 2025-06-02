import requests
from faker import Faker
fake = Faker()

headers = {"Authorization": "pk_188586348_VZKFE8R6B1JLNASCXOM0QLDLLYOG7FZZ"}

def create_list():
    random_name = fake.first_name()
    body = {
        "name": random_name
    }
    result = requests.post("https://api.clickup.com/api/v2/folder/90156767371/list",headers=headers, json=body)
    print(result)
    return result

def update_list(id):
    random_name_for_update = fake.first_name()
    body_updated = {
        "name": random_name_for_update
    }
    result = requests.put("https://api.clickup.com/api/v2/list/" + id, headers=headers, json=body_updated)
    return result