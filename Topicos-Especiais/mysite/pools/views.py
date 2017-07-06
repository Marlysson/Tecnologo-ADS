from django.shortcuts import render

from .models import Question

def index(request):

	questoes = Question.objects.all()
	return render(request,"index.html",{"questoes":questoes})

def detalhe(request,question_id):
	questao = Question.objects.get(id=question_id)
	return render(request,"question.html",{"questao":questao})