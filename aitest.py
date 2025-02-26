import unittest
import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_upload_invalid(self):
        response = self.app.post('/upload', data={})
        self.assertEqual(response.status_code, 200)
        self.assertIn("No file part", response.get_json()["error"])

if __name__ == '__main__':
    unittest.main()
