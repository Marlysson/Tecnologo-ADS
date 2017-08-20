from django.test import TestCase
from django.test import Client
from .models import Game
from .serializers import GameSerializer
from pytz import timezone
from datetime import datetime
import requests

class TestSerializer(TestCase):

    def setUp(self):
        
        self.python_object_content = {
            "name":"GTA V",
            "release_date":datetime.now(),
            "game_category":"Action/Adventure"
        }

    def test_should_be_return_count_objects_created(self):

        game_serializer = GameSerializer(data=self.python_object_content)

        if game_serializer.is_valid():
            game_serializer.save()

        count_inserted = Game.objects.all().count()

        self.assertEqual(1,count_inserted)

    def test_should_be_return_object_created_by_post_request_using_serializer(self):

        from datetime import datetime

        self.python_object_content["name"] = "Watch Dogs"

        game_serializer = GameSerializer(data=self.python_object_content)

        if game_serializer.is_valid():
            game_serializer.save()

        games = Game.objects.all()

        game = games.get(pk=1)

        self.assertEqual(game.name,"Watch Dogs")


class TestApi(TestCase):

    def setUp(self):
        self.client = Client()

        self.api_root = "/games/"
        self.api_resource = "games/{}/"

        self.default_content = {
            "name":"Pro Evolution Soccer 2016",
            "release_date": datetime.now().isoformat(),
            "game_category": "Futebol"
        }

    def test_resources_should_return_empty_when_havent_data(self):

        content = self.client.get(self.api_root).data

        self.assertEqual(content,[])

    def test_should_be_return_404_error_when_request_a_not_found_object(self):

        url_object = self.api_resource.format(3)

        request = self.client.get(url_object)

        self.assertEqual(404,request.status_code)

    def test_should_return_object_created(self):

        response = self.client.post(self.api_root,self.default_content)

        game = response.data

        self.assertEqual(201, response.status_code)
        self.assertEqual(1,game["id"])
        self.assertEqual("Pro Evolution Soccer 2016", game["name"])

    def test_should_return_object_created_by_requests_library(self):

        import json

        url = "http://localhost:8000/games/"

        content = json.dumps(self.default_content)

        response = requests.post(
                            url,
                            data=content,
                            headers={"Content-Type":"application/json"}
                    )

        content = response.json()

        self.assertEqual(201,response.status_code)
        self.assertEqual("Pro Evolution Soccer 2016X",content["name"])