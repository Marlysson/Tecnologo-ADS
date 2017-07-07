from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse

from .models import Question, Choice

def index(request):
	questoes = Question.objects.order_by("-pub_date")

	return render(request,"index.html",{"questoes":questoes})

def detalhe(request,question_id):
	questao = Question.objects.get(id=question_id)
	opcoes = questao.opcoes.all()

	return render(request,"question.html",{"questao":questao,"opcoes":opcoes})

def votar(request,question_id):

	escolhido = request.POST['opcao']

	opcao = Choice.objects.get(id=escolhido)
	opcao.votes += 1

	opcao.save()

	return redirect(reverse("detalhar",args=[question_id]))


def results(request,question_id):

	opcoes = Choice.objects.filter(question=question_id)

	total_votos = sum(opcoes.values_list("votes",flat=True))

	resultados = {}

	for opcao in opcoes:
		if opcao.votes == 0:
			resultados[opcao.choice_text] = 0
		else:
			resultado = (opcao.votes / total_votos) * 100
			resultados[opcao.choice_text] = resultado

	return JsonResponse(resultados)