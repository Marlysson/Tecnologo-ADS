# -*- coding:utf8 -*-


produto1 = raw_input('Código 1,Número de peças,Valor unitário:').split()
produto2 = raw_input('Código 2,Número de peças,Valor unitário:').split()

cod1,quant_peca1,valor1 = int(produto1[0]),int(produto1[1]),float(produto1[2])
cod2,quant_peca2,valor2 = int(produto2[0]),int(produto2[1]),float(produto2[2])

total = quant_peca1 * valor1 + quant_peca2 * valor2

print 'Valor a pagar: R$ {:.2f}'.format(total)