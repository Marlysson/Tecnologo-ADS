# -*- coding : utf-8 -*-

nome = input("Qual seu nome: ")
quantidade_pao = int(input("Quantidade de pães vendidos: "))
quantidade_broa = int(input("Quantidade de broas vendidas: "))	

total_pao = quantidade_pao * 0.12
total_broa =  + quantidade_broa * 1.5

total = total_broa + total_pao

poupanca = total * 0.1

print("\nRELATÓRIO DO DIA")
print("Olá {}".format(nome))
print("Pães vendidos : {}, total R$ {:.2f}".format(quantidade_pao,total_pao))
print("Broas vendidas : {}, total R$ {:.2f}".format(quantidade_broa,total_broa))
print("Você deve guardar : R$ {:.2f}\n".format(poupanca))
