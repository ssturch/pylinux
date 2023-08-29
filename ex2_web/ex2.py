python
import unittest
from selenium import webdriver

class TestWebsite(unittest.TestCase):
    def init(self):
        self.base_url = 'https://test-stand.gb.ru'
        self.driver = webdriver.Chrome()

    def close(self):
        self.driver.quit()

    def create_post_check_title_test(self):
        # Вход на веб-сайт
        self.driver.get(f'{self.base_url}/login')
        username_input = self.driver.find_element_by_id('username')
        password_input = self.driver.find_element_by_id('password')
        login_button = self.driver.find_element_by_id('login-button')

        username_input.send_keys('your_username')
        password_input.send_keys('your_password')
        login_button.click()

        # Создание нового поста
        post_title_input = self.driver.find_element_by_id('post-title')
        post_description_input = self.driver.find_element_by_id('post-description')
        create_post_button = self.driver.find_element_by_id('create-post-button')

        post_title_input.send_keys('Test')
        post_description_input.send_keys('This is a test post')
        post_content_input.send_keys('Lorem ipsum dolor sit amet, ' \
                       'consectetur adipiscing elit, sed do eiusmod ' \
                       'tempor incididunt ut labore et dolore magna aliqua.')
        create_post_button.click()

        # Проверка наличия  поста на странице
        post_title = self.driver.find_element_by_class_name('post-title').text
        self.assertEqual(post_title, 'Test')

if __name__ == '__main__':
    unittest.main()
