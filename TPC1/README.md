
# Relatório TPC1

> 09-02-2025  
> Sofia Oliveira a104536  
> ![Foto da aluna](https://github.com/user-attachments/assets/8eb0a6bc-8efa-44d6-a0f5-ab76a4524ba8)  


---

## Resumo do Trabalho  

O objetivo deste trabalho era criar um programa em Python correspondente a um somador on/off, que deve somar continuamente os inteiros (definidos como uma sequência de dígitos) encontrados, imprimindo o resultado deste contador quando encontra o caracter '='. Além disso, ao encontrar 'Off' deve desligar o contador, voltando a ligar ao encontrar 'On'.  

Deste modo, o programa implementado cumpre estes mesmos requisitos, lendo o fluxo de entrada linha a linha e variando a forma como lida com os caracteres lidos nessa linha. Se encontrar um inteiro e o estado atual do contador, definido pela variável _ligado_, for 'On', soma o valor desse inteiro a uma variável _contador_. Caso encontre uma sequência de caracteres correspondente a 'Off' ou 'On' trata de mudar a variável _contador_ para 'False' ou 'True', respetivamente. Por fim, verifica se o caracter lido se trata de um '=' e, assim sendo, imprime o valor atual da variável _contador_.  

---

## Lista de Resultados
Para testar o programa implementado, foram criados três ficheiros de texto, que servirão como o _stdin_ lido pelo programa. Além disso, ao executar os comandos, o output foi redirecionado para ficheiros de resultados.  
Assim sendo, ao executar o programa redirecionando o _stdin_ para o ficheiro [exemplo1.txt](testes/exemplo1.txt)(_'python3 somador-on-off.py < exemplo1.txt > resultado1.txt'_), correspondente ao exemplo dado na aula teórica, o resultado esperado foi o obtido:
> 2079  
> 2086  

Este resultado pode ser observado no ficheiro [resultado1.txt](testes/resultado1.txt).  
  
Quanto ao [exemplo2.txt](testes/exemplo2.txt), o programa devolveu como _output_:
> 230  
> 405  
> 565  

Este resultado pode ser observado no ficheiro [resultado2.txt](testes/resultado2.txt).  
  
Por fim, testou-se o programa com o ficheiro de texto [exemplo3.txt](testes/exemplo3.txt), obtendo o seguinte resultado:
> 850  
> 1070  
> 2920  
> 3420  
> 4170  
> 4270  

Este resultado pode ser observado no ficheiro [resultado3.txt](testes/resultado3.txt).  