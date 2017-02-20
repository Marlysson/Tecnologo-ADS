
-- QUESTÃO 1: 	Listagem dos hóspedes contendo nome e data de nascimento, ordenada em ordem
--		crescente por nome e decrescente por data de nascimento.

SELECT NOME , DT_NASC FROM HOSPEDE ORDER BY NOME ASC , DT_NASC DESC

-- QUESTÃO 2:   Listagem contendo os nomes das categorias, ordenados alfabeticamente. A coluna de
--		nomes deve ter a palavra ‘Categoria’ como título.

SELECT NOME_CAT "Categoria" FROM CATEGORIA ORDER BY NOME_CAT ASC

-- QUESTÃO 3:   Listagem contendo os valores de diárias e os números dos apartamentos, ordenada em
-- 		ordem decrescente de valor.

-- Usando NATURAL JOIN

SELECT NUM, VALOR_DIA FROM CATEGORIA NATURAL JOIN APARTAMENTO ORDER BY VALOR_DIA DESC

-- Usando INNER JOIN

SELECT NUM , VALOR_DIA FROM CATEGORIA INNER JOIN APARTAMENTO ON
	CATEGORIA.COD_CAT = APARTAMENTO.COD_CAT ORDER BY VALOR_DIA DESC

-- Usando PRODUTO CARTESIANO

SELECT NUM , VALOR_DIA FROM CATEGORIA , APARTAMENTO 
	WHERE CATEGORIA.COD_CAT = APARTAMENTO.COD_CAT ORDER BY VALOR_DIA DESC

-- QUESTÃO 4 : Categorias que possuem apenas um apartamento. 

SELECT NOME_CAT FROM CATEGORIA WHERE COD_CAT IN 
	(SELECT COD_CAT FROM APARTAMENTO NATURAL JOIN CATEGORIA 
		GROUP BY COD_CAT HAVING COUNT(*) = 1)

-- QUESTÃO 5:   Listagem dos nomes dos hóspedes brasileiros com mês e ano de nascimento, por ordem
--		decrescente de idade e por ordem crescente de nome do autor.		

SELECT NOME , EXTRACT(MONTH FROM DT_NASC) "Mês de nascimento" , EXTRACT(YEAR FROM DT_NASC) "Ano de nascimento" FROM HOSPEDE
	ORDER BY AGE(CURRENT_DATE,DT_NASC) DESC ,
	NOME ASC

-- QUESTÃO 6:   Listagem com 3 colunas, nome do hóspede, número do apartamento e quantidade (número
--		de vezes que aquele hóspede se hospedou naquele apartamento), em ordem decrescente de
--		quantidade.

SELECT NOME , NUM "Apartamento" , COUNT(*) "Hospedagens" FROM HOSPEDAGEM
	NATURAL JOIN HOSPEDE
	NATURAL JOIN APARTAMENTO
	GROUP BY NUM , NOME
	
-- QUESTÃO 7: Categoria cujo nome tenha comprimento superior a 15 caracteres.

SELECT NOME_CAT FROM CATEGORIA WHERE CHARACTER_LENGTH(NOME_CAT) > 15
SELECT NOME_CAT FROM CATEGORIA WHERE LENGTH(NOME_CAT) > 15

-- QIESTÃO 8: Número dos apartamentos ocupados no ano de 2017 com o respectivo nome da sua categoria.

-- Usando NATURAL JOIN

SELECT DISTINCT NUM , NOME_CAT FROM HOSPEDAGEM 
	NATURAL JOIN APARTAMENTO 
	NATURAL JOIN CATEGORIA 
	WHERE EXTRACT(YEAR FROM DT_ENTRADA) = 2017

-- Usando INNER JOIN's

SELECT DISTINCT APARTAMENTO.NUM , NOME_CAT FROM HOSPEDAGEM INNER JOIN APARTAMENTO
	ON HOSPEDAGEM.NUM = APARTAMENTO.NUM
	INNER JOIN CATEGORIA
	ON APARTAMENTO.COD_CAT = CATEGORIA.COD_CAT
	WHERE EXTRACT(YEAR FROM DT_ENTRADA) = 2017

-- QUESTÃO 9 - INVÁLIDA

-- QUESTÃO 10:  Crie a tabela funcionário com as atributos: cod_func, nome, dt_nascimento e salário.
--		Depois disso, acrescente o cod_func como chave estrangeira nas tabelas hospedagem e
--		reserva.

CREATE TABLE FUNCIONARIO (
	COD_FUNC INT NOT NULL PRIMARY KEY,
	NOME VARCHAR NOT NULL,
	DT_NASC DATE,
	SALARIO FLOAT NOT NULL
)

-- ADICIONANDO COLUNA E CONSTRAINT DE CHAVE ESTRANGEIRA PARA HOSPEDAGEM - FUNCIONARIO

ALTER TABLE HOSPEDAGEM
	ADD COLUMN COD_FUNC INT NOT NULL 
	DEFAULT 1

ALTER TABLE HOSPEDAGEM
	ADD CONSTRAINT COD_FUNC
	FOREIGN KEY (COD_FUNC)
	REFERENCES FUNCIONARIO(COD_FUNC)

-- ADICIONANDO COLUNA E CONSTRAINT DE CHAVE ESTRANGEIRA PARA RESERVA - FUNCIONARIO

ALTER TABLE RESERVA
	ADD COLUMN COD_FUNC INT NOT NULL
	DEFAULT 1
	
ALTER TABLE RESERVA
	ADD CONSTRAINT COD_FUNC
	FOREIGN KEY (COD_FUNC)
	REFERENCES FUNCIONARIO(COD_FUNC)

-- QUESTÃO 11:  Mostre o nome e o salário de cada funcionário. Extraordinariamente, cada funcionário
--		receberá um acréscimo neste salário de 10 reais para cada hospedagem realizada.

SELECT NOME , SALARIO + COUNT(*) * 10 "Reajustado" FROM HOSPEDAGEM
	NATURAL JOIN FUNCIONARIO
	NATURAL JOIN APARTAMENTO
	NATURAL JOIN CATEGORIA
	GROUP BY COD_FUNC , NOME , SALARIO
	
-- QUESTÃO 12:  Listagem das categorias cadastradas e para aquelas que possuem apartamentos, relacionar
--		também o número do apartamento, ordenada pelo nome da categoria e pelo número do
--		apartamento.

SELECT NOME_CAT , NUM FROM CATEGORIA NATURAL JOIN APARTAMENTO
	ORDER BY NOME_CAT ASC , NUM ASC

-- QUESTÃO 13 : Listagem das categorias cadastradas e para aquelas que possuem apartamentos, relacionar
--		também o número do apartamento, ordenada pelo nome da categoria e pelo número do
--		apartamento. Para aquelas que não possuem apartamentos associados, escrever "não possui
--		apartamento".

SELECT NOME_CAT , COALESCE(CAST(NUM AS VARCHAR),'Não possui apartamento') as "Apartamento"
	FROM CATEGORIA LEFT OUTER JOIN APARTAMENTO
	ON APARTAMENTO.COD_CAT = CATEGORIA.COD_CAT
	ORDER BY NOME_CAT ASC , NUM ASC


-- QUESTÃO 14 : O nome dos funcionário que atenderam o João (hospedando ou reservando) ou que
-- 		hospedaram ou reservaram apartamentos da categoria luxo.

SELECT DISTINCT NOME FROM FUNCIONARIO
WHERE COD_FUNC IN
(SELECT COD_FUNC FROM HOSPEDAGEM
	NATURAL JOIN FUNCIONARIO
	NATURAL JOIN APARTAMENTO
	NATURAL JOIN CATEGORIA
	WHERE COD_HOSP IN (SELECT COD_HOSP FROM HOSPEDE WHERE UPPER(NOME) LIKE 'JOÃO%')
	OR UPPER(NOME_CAT) LIKE 'LUXO%'
UNION
SELECT COD_FUNC FROM RESERVA
	NATURAL JOIN FUNCIONARIO
	NATURAL JOIN APARTAMENTO
	NATURAL JOIN CATEGORIA
	WHERE COD_HOSP IN (SELECT COD_HOSP FROM HOSPEDE WHERE UPPER(NOME) LIKE 'JOÃO%')
	OR UPPER(NOME_CAT) LIKE 'LUXO') ORDER BY NOME ASC

-- QUESTÃO 15: O código das hospedagens realizadas pelo hóspede mais velho que se hospedou no
-- 		apartamento mais caro.

SELECT COD_HOSPEDAGEM FROM HOSPEDAGEM
	NATURAL JOIN CATEGORIA
	NATURAL JOIN APARTAMENTO
	NATURAL JOIN HOSPEDE
	WHERE VALOR_DIA = (SELECT MAX(VALOR_DIA) FROM CATEGORIA)
	AND DT_NASC = (SELECT MIN(DT_NASC) FROM HOSPEDE)

-- QUESTÃO 16: Sem usar subquery, o nome dos hóspedes que nasceram na mesma data do hóspede de
--		código 2.

-- QUESTÃO 17: O nome do hóspede mais velho que se hospedou na categoria mais cara mo ano de 2017.

SELECT NOME FROM HOSPEDAGEM 
	NATURAL JOIN HOSPEDE
	NATURAL JOIN APARTAMENTO
	NATURAL JOIN CATEGORIA

SELECT COD_CAT FROM APARTAMENTO WHERE NUM IN ( SELECT DISTINCT NUM FROM HOSPEDAGEM WHERE EXTRACT(YEAR FROM DT_ENTRADA) = 2017)

-- QUESTÃO 18 : O nome das categorias que foram reservadas pela Maria ou que foram ocupadas pelo João
-- 		quando ele foi atendido pelo Joaquim.

SELECT NOME_CAT FROM CATEGORIA WHERE COD_CAT IN 
(SELECT COD_CAT FROM RESERVA
	NATURAL JOIN HOSPEDE
	NATURAL JOIN CATEGORIA
	WHERE UPPER(NOME) LIKE 'MARIA%'
UNION
SELECT COD_CAT FROM HOSPEDAGEM
	NATURAL JOIN HOSPEDE
	NATURAL JOIN APARTAMENTO
	NATURAL JOIN CATEGORIA
	WHERE COD_HOSP = (SELECT COD_HOSP FROM HOSPEDE WHERE UPPER(NOME) LIKE 'JOÃO%')
	AND COD_FUNC IN (SELECT COD_FUNC FROM FUNCIONARIO WHERE UPPER(NOME) LIKE 'JOAQUIM%'))

-- QUESTÃO 19: O nome e a data de nascimento dos funcionários, além do valor de diária mais cara
--		reservado por cada um deles.

SELECT NOME,DT_NASC,MAX(VALOR_DIA) FROM FUNCIONARIO
	NATURAL JOIN RESERVA
	NATURAL JOIN APARTAMENTO
	NATURAL JOIN CATEGORIA
	GROUP BY NOME , DT_NASC
		
-- QUESTÃO 20: A quantidade de apartamentos ocupados por cada um dos hóspedes (mostrar o nome).

SELECT NOME , COUNT(*) "Hospedagens" FROM HOSPEDAGEM
	NATURAL JOIN HOSPEDE
	GROUP BY NOME

-- QUESTÃO 21 : A relação com o nome dos hóspedes, a data de entrada, a data de saída e o valor total pago em diárias 
-- 		(não é necessário considerar a hora de entrada e saída, apenas as datas).

SELECT NOME, DT_ENTRADA, DT_SAIDA , EXTRACT(DAY FROM AGE(DT_SAIDA,DT_ENTRADA)) * VALOR_DIA "Preço total" FROM HOSPEDAGEM
	NATURAL JOIN HOSPEDE
	NATURAL JOIN APARTAMENTO
	NATURAL JOIN CATEGORIA 
	WHERE DT_SAIDA IS NOT NULL
	GROUP BY NOME , DT_ENTRADA, DT_SAIDA , VALOR_DIA


-- QUESTÃO 22 : O nome dos hóspedes que já se hospedaram em todos os apartamentos do hotel.
