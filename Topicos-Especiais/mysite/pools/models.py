from django.db import models

class Question(models.Model):

	question_text = models.CharField(max_length=50)
	closed = models.BooleanField(default=False)
	pub_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.question_text

class Choice(models.Model):

	question = models.ForeignKey(Question,null=True,related_name="opcoes")
	choice_text = models.CharField(max_length=50)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text