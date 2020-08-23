entrada = [ 'A B C', 
            'B C E', 
            'C G',
            'D A F',
            'E F',
            'F H']

# Convete a entrada (conjunto de strings) em um dicionario para facilitar a estruturação do grafo
def entradaParaDicionario(entrada):
    matrix = []
    for i in entrada:
        lista = list(i.split(" "))
        matrix.append(lista)
    dicionario = {}
    for i in matrix:
        dicionario[i[0]] = i[1:]
    
    return dicionario

# Variavel grafo recebe a entrada que foi convertida em um dicionário
grafo = entradaParaDicionario(entrada)

# Algorítmo de busca em profundidade usado em Teoria dos Grafos
def buscaEmProfundidade(grafo, no, caminho = None):
    if no not in caminho:
        caminho.append(no)
        if no not in grafo:
            return caminho
        for vizinho in grafo[no]:
            caminho = buscaEmProfundidade(grafo, vizinho, caminho)
    return caminho

# O código abaixo serve para formatar a saída de forma mais autoexplicativa
for i in range(len(grafo)):
    caminho = list()
    caminhoToSort = list()
    caminho = buscaEmProfundidade(grafo, list(grafo)[i], [])
    for i in range(1, len(caminho)):
        caminhoToSort.append(caminho[i])
    caminhoToSort.sort()
    print('Nome da Classe: '+caminho[0]+' | Dependencias: '+' '.join(caminhoToSort))