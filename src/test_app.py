import unittest
from routes import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_all_employees(self):
        response = self.app.get('/employee')
        self.assertEqual(response.status_code, 200)


    def test_get_existing_employee(self):
        response = self.app.get('/employee/1')
        self.assertEqual(response.status_code, 200)


    def test_get_non_existing_employee(self):
        response = self.app.get('/employee/1000')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
