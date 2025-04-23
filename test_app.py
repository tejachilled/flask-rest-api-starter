import unittest
from app import app

class ItemsApiTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_items_status_code(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)

    def test_get_items_returns_list(self):
        response = self.client.get('/items')
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)

    def test_items_have_id_and_name(self):
        response = self.client.get('/items')
        data = response.get_json()
        if data:
            item = data[0]
            self.assertIsInstance(item, dict)
            self.assertIn('id', item)
            self.assertIn('name', item)

    def test_sample_item_present(self):
        response = self.client.get('/items')
        data = response.get_json()
        names = [item['name'] for item in data]
        self.assertIn('Sample Item 1', names)

if __name__ == '__main__':
    unittest.main()
