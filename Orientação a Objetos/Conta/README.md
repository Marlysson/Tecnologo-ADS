1. Código

2.  > Exception in thread "main" java.lang.IllegalArgumentException

3. Código

4. Mudanças:  
- Foi preciso mostrar o método ```.getMessage()``` da Exception que foi passada via contrutor da mesma.

5. 
- Lançar a exceção com o nome da classe criada.
- Criar o contrutor da classe e herdar o contrutor da classe mãe (Exception) usando o:
 ```super()``` para definir uma mensagem na classe filha e usando o método da classe mãe para mostrar a mensagem, o ```getMessage()```;
 
6. A classe de teste fica inalterável. a única alteração foi remover a mensagem ```throws``` da exceção pelo valor inválido que foi passado.

7. Resulta em que terá que ser tratado a exceção no método em que usar a exceção, ou utilizando um tratamento ```throws``` com a exceção , ou tratando ela com o uso do ```try```.


