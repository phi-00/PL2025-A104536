# Relatório TPC2  

> 07-02-2025  
> Sofia Oliveira a104536  
> ![Foto da aluna](https://github.com/user-attachments/assets/8eb0a6bc-8efa-44d6-a0f5-ab76a4524ba8)  


---

## Resumo do Trabalho  

Para este trabalho, foi implementado um analisador léxico, usando a biblioteca ply, para a linguagem apresentada no enunciado.  
O código define uma tabela de tokens para esta linguagem e, de seguida, reconhece-as no texto através das expressões regulares que as definem. Para esta linguagem, foram definidos os seguintes tokens:  
1. SELECT
2. VAR
3. WHERE
4. LCHAV
5. RCHAV
6. TYPE
7. PREF_URI
8. STRING
9. POINT
10. LIMIT
11. NUM

---

## Lista de Resultados  
Para testar esta programa e o seu bom funcionamento, foi criado um ficheiro, [teste1.txt](testes/teste1.txt) e, executando o programa, o output devolvido corresponde ao ficheiro [resultado1.txt](testes/resultado1.txt).