import time

from testpage import OperationHelper
username = "username"
password = "password"
name = "NAME"
email = "name@host.cn"
content = "Test me!"


def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login(username)
    test_page1.enter_password(password)
    test_page1.click_button()
    time.sleep(3)

    test_page1.click_contact()
    time.sleep(3)

    test_page1.enter_name(name)
    test_page1.enter_email(email)
    test_page1.enter_content(content)
    test_page1.click_button_contact()
    time.sleep(3)

    alert_text = 'Form submitted!'
    text = test_page1.get_alert_text()
    assert text == alert_text