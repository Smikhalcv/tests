import unittest
import Function
from unittest.mock import patch


# Следует протестировать основные функции по получению информации о документах,
# добавлении и удалении элементов из словаря.

class Test_Function(unittest.TestCase):
    def setUp(self):
        self.dirs, self.docs = Function.directories, Function.documents

    def test_list_doc(self):
        Function.list_doc_on_directories(self.dirs)
        self.assertTrue(Function.list_doc_on_directories(self.dirs))

    def test_add_doc(self):
        len_before = len(self.docs)
        with patch('Function.input', size_effect=['passport', '11111111', 'netology', '5']):
            Function.add_doc(self.docs, self.dirs)
        self.assertLess(len_before, len(self.docs))

    def test_del_doc(self):
        len_before = len(self.docs)
        with patch('Function.input', return_value='2207 876234'):
            Function.del_doc(self.docs, self.dirs)
        self.assertGreater(len_before, len(self.docs))