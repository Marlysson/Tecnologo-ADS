from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer

@api_view(["GET","POST"])
def game_list(request):

	if request.method == 'GET':
		games = Game.objects.all()
		serializer_data = GameSerializer(games,many=True)

		return Response(serializer_data.data)

	if request.method == 'POST':

		serializer = GameSerializer(data=request.data)

		if serializer.is_valid():

			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def game_detail(request,pk):

	game = get_object_or_404(Game,pk=pk)

	if request.method == 'GET':

		serialized_game = GameSerializer(game)	

		return Response(serialized_game.data)

	elif request.method == 'PUT':

		serialized_game = GameSerializer(game,data=request.data)

		if serialized_game.is_valid():
			serialized_game.save()

			return Response(serialized_game.data)

		return Response(serialized_game.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'DELETE':
		
		from datetime import datetime

		today = timezone.make_aware(datetime.now(), timezone.get_current_timezone())

		game_is_launched = lambda date : date < today

		if game_is_launched(game.release_date):
			
			return Response({"error":"Não permitido remover jogos ainda não lançados."},
				status=status.HTTP_400_BAD_REQUEST)

		game.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		

		