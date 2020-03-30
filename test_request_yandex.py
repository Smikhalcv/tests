import unittest
import request_yandex


class Tests_translator(unittest.TestCase):
    '''Тестирует файл с яндекс переводом'''

    def setUp(self) -> None:
        #
        self.data = request_yandex.translat('Привет', 'ru', 'en')

    def test_status(self):
        self.assertEqual(self.data.json()['code'], 200)

    def test_status_code(self):
        self.assertEqual(self.data.status_code, 200)

    def test_text(self):
        self.assertEqual(self.data.json()['text'][0].lower(), 'hi')

    def test_attribute(self):
        with self.assertRaises(TypeError):
            request_yandex.translat('Привет', 'ru', 'en', 'dy')

    def test_negativ_text(self):
        self.assertNotEqual(self.data.json()['text'][0].lower(), 'Привет')