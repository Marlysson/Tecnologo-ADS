from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import Question, Choice

def index(request):

	questoes_fechadas = Question.objects.filter(closed=True).order_by("-pub_date")
	questoes_abertas = Question.objects.filter(closed=False).order_by("-pub_date")

	contexto = {"abertas":questoes_abertas,"fechadas":questoes_fechadas}

	return render(request,"index.html",contexto)

def questao(request,question_id):

	questao = Question.objects.get(id=question_id)
	opcoes = questao.opcoes.all()

	return render(request,"question.html",{"questao":questao,"opcoes":opcoes})
		
def remover_questao(request,question_id):

	questao = Question.objects.get(id=question_id)
	questao.delete()
	

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

		nome = opcao.choice_text.lower().replace(" ","")

		if opcao.votes == 0:
			resultados[nome] = 0
		else:
			resultado = (opcao.votes / float(total_votos)) * 100
			resultados[nome] = resultado
	
	return JsonResponse(resultados)

def administrar(request,question_id):

	questao = Question.objects.get(id=question_id)
	opcoes = questao.opcoes.all()

	opcoes_avulsas = Choice.objects.filter(question=None)

	contexto = {
		"questao":questao,
		"opcoes":opcoes,
		"opcoes_avulsas":opcoes_avulsas
	}

	return render(request,"manage_question.html",contexto)

def change_status(request):

	questao = request.POST["questao"]

	try:
		questao = Question.objects.get(id=questao)
		questao.mudar_status()

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


def criar_opcao(request):

	nome_opcao = request.POST["name_option"]
	id_questao = request.POST["questao"]

	try:

		questao = Question.objects.get(id=id_questao)

		opcao = Choice(choice_text=nome_opcao)
		opcao.associarPara(questao)

		dado = JsonResponse({"name":opcao.choice_text,"id":opcao.id})

		return HttpResponse(dado,content_type="text/json",status=200)
	except:
		return HttpResponse(status=404)

def associar_opcao(request,question_id):

	opcoes_selecionadas = request.POST.getlist("opcao")
	opcoes_selecionadas = list(map(int,opcoes_selecionadas))

	questao = Question.objects.get(id=question_id)

	for id_opcao in opcoes_selecionadas:
		opcao = Choice.objects.get(id=id_opcao)
		opcao.associarPara(questao)

	return redirect(reverse("administrar",args=[questao.id]))