
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer

@api_view(["GET","POST"])
def game_list(request):

	def get():
		games = Game.objects.all()
		serializer_data = GameSerializer(games,many=True)

		return Response(serializer_data.data)


	methods = {
		"GET":get()
	}


	return methods[request.method]