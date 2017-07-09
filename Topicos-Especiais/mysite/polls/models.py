from django.db import models

class Question(models.Model):

	question_text = models.CharField(max_length=50)
	closed = models.BooleanField(default=False)
	pub_date = models.DateField(auto_now_add=True)

	def mudar_status(self):
		self.closed = not self.closed
		self.save()

	def addOpcao(self,text):
		choice = Choice.objects.create(question=self,
								choice_text=text)

	def delete(self,*args,**kwargs):
		print(self.opcoes)
		print(self.opcoes.all())
		for opcao in self.opcoes.all():
			opcao.resetar()

		super().delete(*args,**kwargs)

	def __str__(self):
		return self.question_text

	class Meta:
		db_table = "question"
			

class Choice(models.Model):

	question = models.ForeignKey(Question,null=True,related_name="opcoes")
	choice_text = models.CharField(max_length=50)
	votes = models.IntegerField(default=0)

	def resetar(self):
		self.question = None
		self.votes = 0

		self.save()

	def associarPara(self,question):
		self.question = question
		self.save()
		
	def __str__(self):
		return self.choice_text

	class Meta:
		db_table = "choice"