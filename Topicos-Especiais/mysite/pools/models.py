from django.db import models

class Question(models.Model):

	question_text = models.CharField(max_length=50)
	closed = models.BooleanField(default=False)
	pub_date = models.DateField(auto_now_add=True)
