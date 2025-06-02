import requests
from faker import Faker
from pytest_steps import test_steps

from modules.list_methods import create_list, update_list

fake = Faker()
headers = {"Authorization": "pk_188586348_VZKFE8R6B1JLNASCXOM0QLDLLYOG7FZZ"}

def test_get_list():
    result = requests.get("https://api.clickup.com/api/v2/folder/90156767371/list",headers=headers)
    assert result.status_code == 200
    print("Test 1 passed")
    assert result.json()["lists"][0]["name"] == "Ellie"
    print("Test 2 passed")

def test_create_list():
    result = create_list()
    assert result.status_code == 200

@test_steps("Create new list", "Update created list")
def test_update_list():
    result = create_list()
    id = result.json()["id"]
    yield
    update_list(id)
    assert result.status_code == 200
    yield