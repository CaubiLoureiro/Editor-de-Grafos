def procura_todas_arestas(entradas,verti1):
    arestas =[]

    for i in range (0,len(entradas)):
        for j in range (0,2):

            if (entradas[i][j] == verti1) and (entradas[i] not in arestas) :
                arestas.append(entradas[i])

    return arestas

def procura_aresta (entradas,verti1,verti2):
    linha = -1
    for i in range (0,len(entradas)):
        if (((entradas[i][0] == verti1) and (entradas[i][1] == verti2)) or
        ((entradas[i][0] == verti2) and (entradas[i][1] == verti1))):
            linha = i
            break
    return linha

def atualiza_maior(entradas, maior_vertice):
    for i in range(len(entradas)):
        if(entradas[i][0] > maior_vertice):
            maior_vertice = entradas[i][0]

        if(entradas[i][1] > maior_vertice):
            maior_vertice = entradas[i][1]
    return  maior_vertice

def verifica_repeticao (entradas, v1,v2):
    continua = True
    for i in range (0,len(entradas)):
        if ((entradas[i][0] == v1) or (entradas[i][1] == v1)) and ((entradas[i][0] == v2) or (entradas[i][1] == v2)):
            continua = False

    return continua

def atualiza_no(entradas, v1):
    for i in range (0,len(entradas)):
        if (entradas[i][0] == v1 or entradas[i][1] == v1) :
            return False

    return True