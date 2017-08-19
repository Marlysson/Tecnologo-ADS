from django.shortcuts import render
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

		if serializer_data.is_valid():

			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
