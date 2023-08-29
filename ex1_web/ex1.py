import unittest
import requests

class TestWebAPI(unittest.TestCase):
    def setUp(self):
# Определение URL для API
        self.test_url = 'https://test-stand.gb.ru/api'

    def test_create_post_and_check_description(self):
# Создание тестового поста
        post_data = {
            'title': 'Test',
            'description': 'This is a test post',
            'content': 'Lorem ipsum dolor sit amet, ' \
                       'consectetur adipiscing elit, sed do eiusmod ' \
                       'tempor incididunt ut labore et dolore magna aliqua. '
        }
        response = requests.post(f'{self.base_url}/posts', json=post_data)
        self.assertEqual(response.status_code, 201)

# Получение списка постов
        response = requests.get(f'{self.base_url}/posts')
        self.assertEqual(response.status_code, 200)
        posts = response.json()

# Поиск созданного поста по полю "title"
        found_post = None
        for post in posts:
            if post['title'] == post_data['title']:
                found_post = post
                break

# Проверка созданного поста
        self.assertIsNotNone(found_post)
        self.assertEqual(found_post['title'], post_data['title'])
        self.assertEqual(found_post['description'], post_data['description'])
        self.assertEqual(found_post['content'], post_data['content'])

if __name__ == '__main__':
    unittest.main()
