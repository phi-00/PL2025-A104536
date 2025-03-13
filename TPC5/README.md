# Relatório TPC2  

> 12-02-2025  
> Sofia Oliveira a104536  
> ![Foto da aluna](https://github.com/user-attachments/assets/8eb0a6bc-8efa-44d6-a0f5-ab76a4524ba8)  


---

## Resumo do Trabalho  
Este trabalho consiste na criação de um programa Python que simula o funcionamento de uma máquina de automática.  
Este programa suporta as seguintes operações:
1. Listagem dos produtos da máquina
2. Inserção de moedas na máquina
3. Seleção de produtos para compra
4. Saída do sistema com emissão de troco  
  
Este programa usa um arquivo JSON para armazenar o stock da máquina. A máquina aceita moedas de 2 euros, 1 euro, 50 cêntimos, 20 cêntimos, 10 cêntimos e 5 cêntimos. Quando um produto é selecionado, o programa verifica a sua disponibilidade e se o saldo atual é igual ou superior ao preço do produto; caso ambas as condições se verifiquem, o produto pode ser retirado e retira-se uma unidade da quantidade desse produto no stock.  
Por fim, ao sair do programa, ele reescreve o stock no ficheiro JSON, de modo a atualizar o mesmo.


---

## Lista de Resultados  
Pode ser observada uma interação com o programa em [output1.txt](testes/output.txt).