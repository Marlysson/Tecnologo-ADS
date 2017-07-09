
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r"^$",views.index,name="index"),
	url(r"^question/(?P<question_id>\d+)$",views.questao, name="questao"),
	url(r"^question/(?P<question_id>\d+)/remover$",views.remover_questao, name="remover_questao"),
	url(r"^question/(?P<question_id>\d+)/results$", views.results, name="resultados"),	
	url(r"^question/(?P<question_id>\d+)/manage$", views.administrar, name="administrar"),	
	url(r"^question/change_status$", views.change_status, name="change_status"),
	url(r"^question/(?P<question_id>\d+)/options/add$", views.associar_opcao, name="associar_opcao"),

	url(r"^option/add$", views.criar_opcao, name="criar_opcao"),
	url(r"^option/remove$", views.remover_opcao, name="remover_opcao"),	
	url(r"^option/vote$", views.votar, name="votar"),	
]