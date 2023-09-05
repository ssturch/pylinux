from testpage import OperationHelper
import logging
import time
import requests
import yaml
from Send_Email_Test import send_mail


with open("test.yaml") as f:
    data = yaml.safe_load(f)
    name = data["username"]
    password = data["password"]
    test = data["test"]
    token = data["url_get_token"]
    api_posts = data["url_api_posts"]


def login_check(user, passwd, url, block):
    object_data = requests.post(url=url, data={'username': f'{user}', 'password': f'{password}'})
    check_login = obj_data.json()[f'{block}']
    return str(check_login)


def token_auth(token, url, block):
    res = requests.get(url=url,
                       headers={"X-Auth-Token": token},
                       params={"owner": "Me"})
    content = [item[f"{block}"] for item in res.json()['data']]
    return content


def test_step_1(browser):
    logging.info("Test_1_Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(test)
    testpage.enter_pass(test)
    testpage.click_login_button()
    time.sleep(5)
    assert "401" in login_check(test, test, token, 'code'), "Test_1_FAIL"


def test_step_2(browser):
    logging.info("Test_2_Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(name)
    testpage.enter_pass(password)
    testpage.click_login_button()
    time.sleep(5)
    assert f"{name}" in login_check(name, password, token, 'username'), "Test_2_FAIL"


def test_step_3(browser, login):
    logging.info("Test_3_Starting")
    testpage = OperationHelper(browser)
    testpage.click_to_do_new_post()
    testpage.enter_title("Field_title")
    testpage.enter_description("Field_description")
    testpage.enter_content("Field_content")
    testpage.click_save_post_button()
    time.sleep(5)
    token_auth(login, url_api_posts, 'title')
    assert "Field_title" in token_auth(login, api_posts, 'title'), "Test_3_FAIL"


def test_step_4(browser, login):
    logging.info("Test_4_Starting")
    testpage = OperationHelper(browser)
    testpage.click_contact_button()
    testpage.enter_name("username")
    testpage.enter_email("noname@nonemvich.ru")
    testpage.enter_contact_content("lorem ipsum")
    testpage.contact_us_save_button()
    time.sleep(5)
    alert = testpage.get_alert_text()
    assert alert == "Form successfully submitted", "Test_4_FAIL"

def test_step_5():
    send_mail()