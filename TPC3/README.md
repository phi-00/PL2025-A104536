# Relatório TPC2  

> 27-02-2025  
> Sofia Oliveira a104536  
> ![Foto da aluna](https://github.com/user-attachments/assets/8eb0a6bc-8efa-44d6-a0f5-ab76a4524ba8)  


---

## Resumo do Trabalho  

Neste trabalho, foi criado um programa em Python que, com o auxílio de expressões regulares, converte um ficheiro MARKDOWN em HTML, fazendo a devida conversão dos seguintes elementos:  
1. Cabeçalhos
2. Texto Bold
3. Texto Itálico
4. Lista Numerada
5. Link
6. Imagem  
  
Com este propósito em mente, foram criadas expressões regulares que caracterizem cada um destes elementos, tanto no seu formato em contexto de ficheiro Markdown, como no seu formato pretendido após a conversão para *sintax* HTML.  
De seguida, é utilizada a função *sub(pattern, repl, string)*, da biblioteca *re*, que retorna a string resultante de substituir o padrão fornecido como parâmetro (pattern) pela expressão desejada (repl). Neste caso, o parâmetro pattern corresponde ao formato do elemento em Markdown e o parâmetro repl corresponde à representação desse mesmo elemento em sintax HTML.

---

## Lista de Resultados  
Para testar esta programa e o seu bom funcionamento, foram criados dois ficheiros Markdown, [teste1.md](testes/teste1.md) e [teste2.md](testes/teste2.md), e executando o programa, o output devolvido corresponde aos ficheiros [teste1.html](testes/teste1.html) e [teste2.html](testes/teste2.html), todos estes ficheiros presentes na pasta [testes](testes/).