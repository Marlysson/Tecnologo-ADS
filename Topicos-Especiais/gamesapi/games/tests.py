from django.test import TestCase
from django.test import Client

class TestApi(TestCase):

	def setUp(self):
		self.client = Client()

		self.api_root = "/games/"
		self.api_resource = "/games/{}"

	def test_resources_should_return_empty_when_havent_data(self):

		content = self.client.get(self.api_root).data

		self.assertEqual(content,[])
