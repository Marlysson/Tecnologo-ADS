from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Game
	

class GameSerializer(serializers.ModelSerializer):

	name = serializers.CharField(validators=[UniqueValidator(
						queryset=Game.objects.all(),
						message="Não pode haver nomes iguais.")])

	class Meta:
		model = Game
		fields = ('id', 'name', 'release_date', 'game_category', 'played')

	def empty_field(self,field_value):
		if not field_value:
			return True
		return False

	def validate_name(self,value):
		if self.empty_field(value):
			raise serializers.ValidationError("O campo não pode estar vazio.")
		return value

	def validate_release_date(self,value):
		if self.empty_field(value):
			raise serializers.ValidationError("O campo não pode estar vazio.")
		return value

	def validate_game_category(self,value):
		if self.empty_field(value):
			raise serializers.ValidationError("O campo não pode estar vazio.")
		return value