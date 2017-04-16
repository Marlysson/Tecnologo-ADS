-- Questão 1

create table fornecedor(
    cod_fornecedor int primary key,
    nome_fornecedor varchar,
    endereco_fornecedor varchar
)

insert into fornecedor (cod_fornecedor,nome_fornecedor,endereco_fornecedor) values (1,'Fornecedor 1','Endereço fornecedor 1')
insert into fornecedor (cod_fornecedor,nome_fornecedor,endereco_fornecedor) values (2,'Fornecedor 2','Endereço fornecedor 2')
insert into fornecedor (cod_fornecedor,nome_fornecedor,endereco_fornecedor) values (3,'Fornecedor 3','Endereço fornecedor 3')
insert into fornecedor (cod_fornecedor,nome_fornecedor,endereco_fornecedor) values (4,'Fornecedor 4','Endereço fornecedor 4')

create table livro(
    cod_livro int primary key,
    cod_titulo int references titulo(cod_titulo),
    quant_estoque int,
    valor_unitario float
) 

insert into livro (cod_livro , cod_titulo , quant_estoque,valor_unitario) values (1,1,10,20)
insert into livro (cod_livro , cod_titulo , quant_estoque,valor_unitario) values (2,2,15,20)
insert into livro (cod_livro , cod_titulo , quant_estoque,valor_unitario) values (3,3,5,30)
insert into livro (cod_livro , cod_titulo , quant_estoque,valor_unitario) values (4,4,25,30)
insert into livro (cod_livro , cod_titulo , quant_estoque,valor_unitario) values (5,2,30,20)
insert into livro (cod_livro , cod_titulo , quant_estoque,valor_unitario) values (6,4,40,15)


create table titulo(
    cod_titulo int primary key,
    descr_titulo varchar
)

insert into titulo (cod_titulo,descr_titulo) values (1,'Titulo livro 1')
insert into titulo (cod_titulo,descr_titulo) values (2,'Titulo livro 2')
insert into titulo (cod_titulo,descr_titulo) values (3,'Titulo livro 3')
insert into titulo (cod_titulo,descr_titulo) values (4,'Titulo livro 5')

create table pedido (
    cod_pedido int,
    cod_fornecedor int,
    data_pedido date,
    hora_pedido time,
    valor_total_pedido float,
    quant_itens_pedidos int
)

insert into pedido (cod_pedido,cod_fornecedor,data_pedido,hora_pedido,valor_total_pedido,quant_itens_pedidos)
values (1,1,'2017-03-20','14:13:00',330,14)

insert into pedido (cod_pedido,cod_fornecedor,data_pedido,hora_pedido,valor_total_pedido,quant_itens_pedidos)
values (2,2,'2017-03-20','15:13:00',150,5)

insert into pedido (cod_pedido,cod_fornecedor,data_pedido,hora_pedido,valor_total_pedido,quant_itens_pedidos)
values (3,3,'2017-03-20','16:13:00',150,5)

insert into pedido (cod_pedido,cod_fornecedor,data_pedido,hora_pedido,valor_total_pedido,quant_itens_pedidos)
values (4,2,'2017-02-20','15:13:00',150,5)

insert into pedido (cod_pedido,cod_fornecedor,data_pedido,hora_pedido,valor_total_pedido,quant_itens_pedidos)
values (5,3,'2017-02-20','16:13:00',150,5)

create table item_pedido(
    cod_livro int,
    cod_pedido int,
    quantidade_item int,
    valor_total_item float
)

insert into item_pedido (cod_livro , cod_pedido,quantidade_item,valor_total_item) values (1,1,5,100)
insert into item_pedido (cod_livro , cod_pedido,quantidade_item,valor_total_item) values (2,1,4,80)
insert into item_pedido (cod_livro , cod_pedido,quantidade_item,valor_total_item) values (3,1,3,90)
insert into item_pedido (cod_livro , cod_pedido,quantidade_item,valor_total_item) values (4,1,2,60)
insert into item_pedido (cod_livro , cod_pedido,quantidade_item,valor_total_item) values (3,2,3,90)
insert into item_pedido (cod_livro , cod_pedido,quantidade_item,valor_total_item) values (4,2,2,60)
insert into item_pedido (cod_livro , cod_pedido,quantidade_item,valor_total_item) values (3,3,3,90)
insert into item_pedido (cod_livro , cod_pedido,quantidade_item,valor_total_item) values (4,3,2,60)

-- Questão 2

-- A
select nome_fornecedor from fornecedor natural join pedido where 
	extract(month,data_pedido) = 2
	group by cod_fornecedor having sum(valor_total_pedido) > 150 

-- B
select nome_fornecedor from fornecedor natural join pedido where 
	extract(month,data_pedido) = 2
	group by cod_fornecedor having sum(valor_total_pedido) > 150 limit 1

-- inserir mais dados

-- C
create view maiores_precos as
select sum(valor_total_pedido) maiores_vendas from fornecedor natural join pedido where
	extract(month,data_pedido) = 2
	group by cod_fornecedor

select nome_fornecedor from fornecedor where cod_fornecedor in(
    select cod_fornecedor from pedido group by cod_fornecedor
    having sum(valor_total_pedido) in (select max(maiores_vendas) from maiores_precos))


-- Questão 3

create trigger verifica_restricoes
	before INSERT on pedido
	for each statement
	when new.cod_produto in (select 

	