import unittest
from app import create_app
from flask import url_for

class ReportTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_report_form_access(self):
        response = self.client.get('/reports/new')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Report a Cybercrime', response.data)
