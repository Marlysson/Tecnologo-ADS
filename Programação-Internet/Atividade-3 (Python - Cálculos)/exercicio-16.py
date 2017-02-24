# -*- coding : utf-8 -*-

def change_valores(valor_a,valor_b):
	intermediario = valor_a
	valor_a = valor_b
	valor_b = intermediario

	return {"a":valor_a,"b":valor_b}

a = 12
b = 25

print("Valor de a : {}".format(a))
print("Valor de b : {}".format(b))

resultado = change_valores(a,b)

print("Valores trocados")
print("A : {}".format(resultado["a"]))
print("B : {}".format(resultado["b"]))