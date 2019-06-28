import unittest
from src.app import *
import os, json


class TestApp(unittest.TestCase):
    def SetUp(self):
        current_path = str(os.path.dirname(os.path.abspath(__file__)))
        f_directories = os.path.join(current_path, 'fixtures/directories.json')
        f_documents = os.path.join(current_path, 'fixtures/documents.json')
        with open(f_documents, 'r') as out_docs:
            self.documents = json.load(out_docs)
        with open(f_directories, 'r') as out_dirs:
            self.directories = json.load(out_dirs)

    def test_insert_document(self):
        for doc_number in range(1, 4):
            for doc_type in ['passport', 'invoice', 'insurance']:
                for doc_owner_name in ['Гонджубасов Кинстинктин', 'Упырев Михаил', 'КонЧенЫй Ли']:
                    new_doc = {
                        "type": doc_type,
                        "number": doc_number,
                        "name": doc_owner_name
                    }
                    self.documents.append(new_doc)
                    append_doc_to_shelf(doc_number, f'Полка {doc_number}')


if __name__ == '__main__':

    unittest.main()
