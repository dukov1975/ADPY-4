import unittest
import json
import app
from mock import patch

documents = []
directories = {}


def setUpModule():
    with open('fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
    with open('fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))


@patch('app.documents', documents, create=True)
@patch('app.directories', directories, create=True)
class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        self.example_set = {
            'shelf': 33,
            'doc': 22
        }

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)
        self.assertGreater(len(app.get_all_doc_owners_names()), 0)

    def test_append_doc_to_shelf(self):
        app.append_doc_to_shelf(self.example_set['doc'], self.example_set['shelf'])
        self.assertIn(self.example_set['doc'], directories.get(self.example_set['shelf']))

    def test_delete_doc(self):
        self.assertTrue(app.check_document_existance("11-2"))  # check before deleting doc

        with patch('app.input', return_value="11-2") as child1:
            app.delete_doc()

        self.assertFalse(app.check_document_existance("11-2"))  # check after deleting doc


if __name__ == '__main__':
    unittest.main()