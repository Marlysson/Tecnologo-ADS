from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import Question, Choice

def index(request):

	questoes_fechadas = Question.objects.filter(closed=True).order_by("-pub_date")
	questoes_abertas = Question.objects.filter(closed=False).order_by("-pub_date")

	contexto = {"abertas":questoes_abertas,"fechadas":questoes_fechadas}

	return render(request,"index.html",contexto)

def detalhe(request,question_id):
	questao = Question.objects.get(id=question_id)
	opcoes = questao.opcoes.all()

	return render(request,"question.html",{"questao":questao,"opcoes":opcoes})

def votar(request):

	escolhido = request.POST['opcao']

	try:
		opcao = Choice.objects.get(id=escolhido)
		opcao.votes += 1
		opcao.save()
	except:
		tudo_ok = False


	return HttpResponse(status=200)


def results(request,question_id):

	opcoes = Choice.objects.filter(question=question_id)

	total_votos = sum(opcoes.values_list("votes",flat=True))

	resultados = {}

	for opcao in opcoes:
		if opcao.votes == 0:
			resultados[opcao.choice_text] = 0
		else:
			resultado = (opcao.votes / float(total_votos)) * 100
			resultados[opcao.choice_text] = resultado
	
	return JsonResponse(resultados)

def administrar(request,question_id):

	questao = Question.objects.get(id=question_id)
	opcoes = questao.opcoes.all()

	return render(request,"manage_question.html",{"questao":questao,"opcoes":opcoes})

def change_status(request):

	questao = request.POST["questao"]

	try:
		questao = Question.objects.get(id=questao)
		questao.toggle_status()

		return HttpResponse(status=200)
	except:
		return HttpResponse(status=404)


def remover_opcao(request):

	option_id = request.POST["opcao"]

	try:

		opcao = Choice.objects.get(id=option_id)
		opcao.resetar()

		return HttpResponse(status=200)

	except Exception as e:
		return HttpResponse(status=404)

