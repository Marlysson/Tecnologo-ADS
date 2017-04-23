## Projeto em django proposto para modelar no ORM do Django o modelo proposto : Fluxo de venda e compra de produtos.

> Para testar a app há duas formas:

- Via shell do django
- Testes

> Para executar os comandos no shell do python usando o django faça:

```shell
$ python manage.py shell
```

```python
>>> from venda.models import *
>>> # Copie e cole os comandos dos arquivos de testes no console e vá executando.
```

> Para executar via testes:

```bash
$ python manage.py test venda.tests
```