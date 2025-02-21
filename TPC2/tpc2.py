def leitura_dataset(file):
    compositores = set()
    obras_periodo = {}
    titulos_periodo = {}

    with open(file, 'r') as file:
        next(file)

        for linha in file:

            fields = linha.split(';')

            titulo_linha = fields[0]
            periodo_linha = fields[3]
            compositor_linha = fields[4]

            compositores.add(compositor_linha)

            obras_periodo[periodo_linha] = obras_periodo.get(periodo_linha, 0) +1

            if periodo_linha not in titulos_periodo:
                titulos_periodo[periodo_linha] = []
            titulos_periodo[periodo_linha].append(titulo_linha)

    return compositores, obras_periodo, titulos_periodo


def results(compositores, obras_periodo, titulos_periodo):
    
    # 1. Lista ordenada de compositores
    lista_compositores = sorted(compositores)
    print("Compositores:\n")
    for compositor in lista_compositores:
        print("\n" + compositor)

    #2. Distribuição de obras por períodos
    print("Obras por período:\n")
    for periodo, quantidade in obras_periodo.items():
        print(f"{periodo}: {quantidade} obras\n")

    #3. Títulos por período
    print("Títulos por período:\n")
    for periodo in titulos_periodo.keys():
        for titulo in sorted(titulos_periodo[periodo]):
            print(f"\t-> {titulo}")


def main():
    file = "obras.csv"

    try:
        compositores, obras_periodo, titulos_periodo = leitura_dataset(file)
        results(compositores, obras_periodo, titulos_periodo)
    except FileNotFoundError:
        print("Erro ao encontrar o arquivo dataset")
    except Exception as e:
        print("Erro ao processar arquivo dataset")

if __name__ == "__main__":
    main()