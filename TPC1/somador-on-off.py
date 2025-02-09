import sys

def soma_on_off():
    contador = 0
    ligado = True
    
    #Lê o input linha a linha
    for linha in sys.stdin:
        i=0

        #Percorre a linha
        while i<len(linha):

            #Caso encontre um Off
            if (i+2)<len(linha):
                if linha[i:i+3].casefold()=="off":
                    ligado = False
                    i += 3
                    continue

            #Caso encontre um On
            if (i+1)<len(linha):
                if linha[i:i+2].casefold()=="on":
                    ligado = True
                    i += 2
                    continue

            #Caso encontre um inteiro
            if linha[i] in "0123456789":
                num = ""
                while linha[i] in "0123456789":
                    num += linha[i]
                    i += 1
                if ligado:
                    contador += int(num)
                continue

            #Caso encontre um '='
            if linha[i]=='=':
                print(contador)
        
            i+=1


def main():
    soma_on_off()


if __name__ == "__main__":
    main()