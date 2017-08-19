from django.test import TestCase
from django.test import Client
from .models import Game
from .serializers import GameSerializer

class TestApi(TestCase):

	def setUp(self):
		self.client = Client()

		self.api_root = "/games/"
		self.api_resource = "/games/{}"

		self.python_object_content = {
			"name":"GTA V",
			"release_date":datetime.now(),
			"game_category":"Action/Adventure"
		}

	def test_resources_should_return_empty_when_havent_data(self):

		content = self.client.get(self.api_root).data

		self.assertEqual(content,[])

	def test_should_be_return_count_objects_created(self):

		from datetime import datetime

		game_serializer = GameSerializer(data=self.python_object_content)

		if game_serializer.is_valid():
			game_serializer.save()

		count_inserted = Game.objects.all().count()

		self.assertEqual(1,count_inserted)

	def test_should_be_return_object_created_by_post_request_using_serializer(self):

		from datetime import datetime

		game_serializer = GameSerializer(data=self.python_object_content)

		if game_serializer.is_valid():
			game_serializer.save()

		games = Game.objects.all()

		game = games.get(pk=1)

		self.assertEqual(game.name,"Watch Dogs")

	