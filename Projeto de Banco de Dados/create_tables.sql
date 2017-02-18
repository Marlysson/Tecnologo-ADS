
CREATE TABLE hospede
(
    cod_hosp INT NOT NULL PRIMARY KEY,
    nome varchar(128) DEFAULT 'NÃO INFORMADO',
    dt_nasc date
);

CREATE TABLE categoria
(
    cod_cat INT not null CHECK (COD_CAT>=1),
    nome varchar(128),
    descricao varchar(128),
    valor_dia real,
    CONSTRAINT PRI_CAT PRIMARY KEY(COD_CAT)
);

CREATE TABLE apartamento
(
    num INT NOT NULL PRIMARY KEY,
    cod_cat integer,
    status char,
    CONSTRAINT cod_cat FOREIGN KEY (cod_cat)
        REFERENCES categoria (cod_cat) MATCH SIMPLE
);

CREATE TABLE hospedagem
(
    cod_hospedagem serial NOT NULL PRIMARY KEY,
    cod_hosp integer NOT NULL,
    num integer not null references apartamento(num),
    dt_entrada date,
    dt_saida date,
    dt_prev_saida date,
    CONSTRAINT cod_hosp FOREIGN KEY (cod_hosp)
        REFERENCES hospede (cod_hosp) MATCH SIMPLE
);


CREATE TABLE reserva
(
    cod_reserva serial NOT NULL PRIMARY KEY,
    dt_reserva date,
    cod_hosp integer NOT NULL,
    cod_cat integer NOT NULL,
    dt_prev_ent date,
    dt_prev_sai date,    
    CONSTRAINT cod_cat FOREIGN KEY (cod_cat)
        REFERENCES categoria (cod_cat) MATCH SIMPLE,
    CONSTRAINT cod_hosp FOREIGN KEY (cod_hosp)
        REFERENCES hospede (cod_hosp) MATCH SIMPLE
);

