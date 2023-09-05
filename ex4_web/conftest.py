import yaml
import pytest
import requests
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


with open("test.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]
    token = testdata["url_get_token"]
    name = testdata["username"]
    password = testdata["password"]


@pytest.fixture()
def login():
    object_data = requests.post(url=token, data={'username': f'{name}', 'password': f'{password }'})
    token = object_data.json()['token']
    return token


@pytest.fixture(scope="session")
def browser():
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdrive.Chrome(service=service, options=options)
    yield driver
    driver.quit()