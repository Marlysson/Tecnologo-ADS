### Questão 4

>Se dois objetos forem comparados com seus valores de atributos iguais diz que
os objetos não são iguais, pois possuem endereços diferentes de memória.

```java
Funcionario func1 = new Funcionario();
func1.nome = "Marlysson";

Funcionario func2 = new Funcionario();
func2.nome = "Marlysson";

if( func1 == func2){
	"Iguais";
}else{
	"Diferentes";
}
```
> Diferentes


#### Questão 5
>Já com um objeto criado a partir da referência de outro objeto e feito a "clonagem" do objeto de origem para o destino junto com os seus atributos é mostrado que são iguais, pois possuem mesmo endereço de memória.

```java
Funcionario func1 = new Funcionario();
func1.nome = "Marlysson";

Funcionario func2 = func1;

if( func1 == func2){
	"Iguais";
}else{
	"Diferentes";
}
```
> Iguais

#### Questão 7

Se for usado o método ```.mostra()``` antes de iniciar os atributos,é mostrado seus valores
com os valores iniciais dos seus tipos, ```int = 0``` , ```float = 0.0 ``` , e no caso dos atributos da classe vem com o valor ```null```.

```java
Funcionario func1 = new Funcionario();
func1.mostra();
```

```java
Salario : 0
RG: null
Data inicio: null
```

#### Questão 8
Se tentar acessar diretamente da classe não irá funcionar.

```java
Funcionario.salario = 1234;
```
>_**Erro:** non-static variable salario cannot be referenced from a static context._

**Explicação** : Para acessar atributos e métodos diretamente das classes, esses valores tem
que possuir sua visibilidade definida como ```static```, assim só poderão ser chamados pela própria classe.


#### Análise

```java
Funcionario.salario = 1234;
Funcionario.calculaGanhoAnual();
```
Não fazem sentido pois tem que saber qual funcionário irá ser definido, pois tanto ```salario``` quanto ```.calculaGanhoAnual()``` são representações de uma pessoa representada como objeto, e não uma abstração como um todo geral ; É de um indivíduo específico.


