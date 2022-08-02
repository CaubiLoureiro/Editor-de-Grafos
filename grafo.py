import auxiliar
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import networkx as nx

class Grafo:

    def __init__(self):
        self.entradas = []
        self.e =[]
        self.cores = []
        self.v = []
        self.maior_vertice = 0
        self.colunas = len(self.entradas)

    # Método para pega a entrada do usuario e colocalas nas listas self.entradas e self.e
    def adiciona_aresta(self,vertices_c_peso):
        vertices= vertices_c_peso[0],vertices_c_peso[1],vertices_c_peso[2]
        # Condição para evitar que entre nós repetidos nas listas
        if (auxiliar.verifica_repeticao(self.entradas,vertices_c_peso[0],vertices_c_peso[1])):
            self.entradas.append(vertices)
            self.e.append(vertices_c_peso)
            self.cores.append('skyblue')

        # Escreve a entrada recebida na matriz de adjacência
        self.escreve_adjacente()
        # Escreve a entrada recebida na matriz de incidência
        self.escreve_incidente()
        # Desenha o grafo incluindo a nova entrada
        self.desenhaGrafo()

    # Método para remover uma aresta do grafo
    def remove_aresta(self,vertices):
        # Encontra indice da aresta na lista self.entradas
        i = auxiliar.procura_aresta(self.entradas,vertices[0],vertices[1])
        # Segura os pedos no iondice correspondente na lista self.e
        peso1 = self.e[i][3]
        peso2 = self.e[i][4]
        # Deleta a aresta  das entradas
        del self.entradas[i]
        del self.e[i]
        del self.cores[i]
        #verifica se o no ta sozinho
        if(auxiliar.atualiza_no(self.entradas,vertices[0])):
            self.v.append([vertices[0],peso1])
        #verifica se ta sozinho e se já entrou na lista. Ex: caso o nó se ligue com ele mesmo
        if (auxiliar.atualiza_no(self.entradas,vertices[1]) and auxiliar.verifica_repeticao(self.v,vertices[0],vertices[1])):
            self.v.append([vertices[1],peso2])
        #reescreve as matrizes, atualiza o grafo
        self.escreve_adjacente()
        self.escreve_incidente()
        self.desenhaGrafo()

    def remove_no(self,no):
        #Procura todas as arestas
        aresta = auxiliar.procura_todas_arestas(self.entradas,no)
        #remove uma por uma
        for i in range (0,len(aresta)):
            self.remove_aresta(aresta[i])
        #Nó vai entrar na lista de vértices sozinhos, procura o vertice e exclui.
        for i in range (0,len(self.v)):
            if (self.v[i][0] == no):
                del self.v[i]
                break
        #Reescreve as matrizes e atualiza o Grafo
        self.escreve_incidente()
        self.escreve_adjacente()
        self.desenhaGrafo()

    def modifica_aresta (self, entrada):

        tentativa = -1
        #procura a aresta pra remover
        i = auxiliar.procura_aresta(self.e, entrada[0], entrada[1])
        #verifica se o comprimmento foi mudado, caso contrário, mantém
        try:
            tentativa = int(entrada[2])
            comprimento = entrada[2]
        except:
            comprimento = self.e[i][2]
        #Mantém os pesos
        peso1 = self.e[i][3]
        peso2 = self.e[i][4]
        #deleta as arestas
        del (self.entradas[i])
        del (self.e[i])
        del (self.cores[i])
        #adiciona uma nova aresta
        self.adiciona_aresta((entrada[0], entrada[1], comprimento, peso1, peso2))

        #atualiza a cor se essa for a escolha do usuário
        if(entrada[3] != ''):
            self.cores[len(self.cores)-1] = entrada[3]

        #Reescreve matrizes e atualiza Grafo
        self.escreve_incidente()
        self.escreve_adjacente()
        self.desenhaGrafo()

    def modifica_pesos (self, vert1, peso):
        #Procura todas as arestas
        aux = auxiliar.procura_todas_arestas(self.entradas,vert1)
        #Modifica o peso de uma por uma
        for i in range (0, len(aux)):
            indice = auxiliar.procura_aresta(self.e,aux[i][0],aux[i][1])
            if (self.e[indice][0] == vert1):
                self.e[indice][3] = peso
            else:
                self.e[indice][4] = peso
        # Se a lista retornar vazia, procura nos vértices sozinhos
        if (len(aux) == 0):
            for i in range (0,len(self.v)):
                if self.v[i][0] == vert1:
                    self.v[i][1] = peso






    def escreve_incidente(self):

        self.colunas = len(self.entradas)
        self.maior_vertice = auxiliar.atualiza_maior(self.entradas,-1)
        matriz =[]

        # Cria matriz zerada
        for i in range (0, self.maior_vertice):
            linha = [0]*self.colunas
            matriz.append(linha)
        #Marca as arestas e vertices que se ligam como 1
        for lin in range (0, len(self.entradas)):
            for col in range (0,2):
                indice = self.entradas[lin][col]
                matriz[indice-1][lin] = 1

        self.matriz_incidente = matriz

    def escreve_adjacente(self):

        self.maior_vertice = auxiliar.atualiza_maior(self.entradas, -1)
        self.colunas = len(self.entradas)
        self.matriz_adjacente = []
        #Cria a matriz zerada
        for i in range(self.maior_vertice):
            lista = [0] * self.maior_vertice
            self.matriz_adjacente.append(lista)
        #Adiciona o comprimento dos vertíces quando eles se ligam
        for i in range(len(self.entradas)):
            self.matriz_adjacente[self.entradas[i][0] - 1][self.entradas[i][1] - 1] = self.entradas[i][2]
            self.matriz_adjacente[self.entradas[i][1] - 1][self.entradas[i][0] - 1] = self.entradas[i][2]


#######################################################################################################################################################


    def desenha_matriz_adjacente (self):
        fig, ax = plt.subplots(1, 1)
        column_labels = []

        for j in range (0,(auxiliar.atualiza_maior(self.entradas,-1))):
            column_labels.append(j+1)
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=self.matriz_adjacente, colLabels=column_labels, loc="center", rowLabels=column_labels)
        plt.show()



    def desenha_matriz_incidente(self):
        fig, ax = plt.subplots(1, 1)
        colunas = []
        linha = []
        for j in range(0, (auxiliar.atualiza_maior(self.entradas, -1))):
            colunas.append(j + 1)
        for i in range (0, len(self.entradas )):
            linha.append(chr(i+65))

        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=self.matriz_incidente, colLabels=linha ,loc="center", rowLabels=colunas)
        plt.show()



    def montaGrafo(self):
        G = nx.Graph()
        plt.cla()
        plt.clf()
        color_map = []
        cor = 'green'
        E = self.entradas
        for i in range(0, len(self.v)):
            G.add_node(self.v[i][0])
        G.add_weighted_edges_from(E)
        for node in G:
            for i in range (0,len(self.entradas)):
                if (self.entradas[i][0] == node) or (self.entradas[i][1] == node):
                    cor = self.cores[i]
            color_map.append(cor)
        return G,color_map

    def desenhaGrafo(self):
        G,color_map = self.montaGrafo()
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight="bold", node_color = color_map)
        edge_weight = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
        plt.savefig('graph.png')
        plt.close()



    def desenhaGrafoSeparado(self):
        G, color_map = self.montaGrafo()
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight="bold", node_color = color_map)
        edge_weight = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
        plt.show()



    def tabela_pesos(self):
        pesos = []
        vertices = []
        for i in range(0, len(self.e)):
            vertice1 = self.e[i][0]
            vertice2 = self.e[i][1]
            peso1 = self.e[i][3]
            peso2 = self.e[i][4]

            if vertice1 not in vertices:
                pesos.append([vertice1, peso1])
                vertices.append(vertice1)

            if vertice2 not in vertices:
                pesos.append([vertice2, peso2])
                vertices.append(vertice2)

        for j in range(0, len(self.v)):
            pesos.append([self.v[j][0], self.v[j][1]])

        fig, ax = plt.subplots(1, 1)
        column_labels = ["Vértice", "Peso"]
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=pesos, colLabels=column_labels, loc="center")
        ax.set_facecolor('Blue')

        plt.show()



    def desenha3D(self):

        ######## Criando grafo em 2D #############

        #Cria figura graph
        G = nx.Graph()
        #Lista para o comprimento das arestas
        aresta_comprimento = []

        for i in range(0, len(self.entradas)):
            G.add_edge(self.entradas[i][0], self.entradas[i][1], weight = self.entradas[i][2])
            comprimento = self.entradas[i][2]
            aresta_comprimento.append(comprimento)

        Num_nodes = len(G.nodes)


        arestas = G.edges()

        # Plotando o grafo 2D em 3D
        dicionario_3D = nx.spring_layout(G, dim = 3, k = 0.5)


        # Separando as coordenadas X, Y, Z para Plotar
        # dicionario_3D é um dicionário onde as chaves são de 1 a 6
        x_no= [dicionario_3D[key][0] for key in dicionario_3D.keys()] # x-coordenadas do nó
        y_no = [dicionario_3D[key][1] for key in dicionario_3D.keys()] # y-coordenadas do nó
        z_no = [dicionario_3D[key][2] for key in dicionario_3D.keys()] # z-coordenadas do nó

        # Criando uma listas que contem as coordenadas inicial e final de cada aresta.
        x_arestas=[]
        y_arestas=[]
        z_arestas=[]

        # Criando uma listas contendo pontos médios que serão usados para ancorar o texto
        x_tx = []
        y_tx = []
        z_tx = []

        # Preenchendo as coordenadas

        for edge in arestas:
            #format: [beginning,ending,None]
            x_coords = [dicionario_3D[edge[0]][0],dicionario_3D[edge[1]][0],None]
            x_arestas += x_coords
            x_tx.append(0.5*(dicionario_3D[edge[0]][0]+ dicionario_3D[edge[1]][0]))

            y_coords = [dicionario_3D[edge[0]][1],dicionario_3D[edge[1]][1],None]
            y_arestas += y_coords
            y_tx.append(0.5*(dicionario_3D[edge[0]][1]+ dicionario_3D[edge[1]][1]))

            z_coords = [dicionario_3D[edge[0]][2],dicionario_3D[edge[1]][2],None]
            z_arestas += z_coords
            z_tx.append(0.5*(dicionario_3D[edge[0]][2]+ dicionario_3D[edge[1]][2]))

        ############# Style das arestas #########
        etext = [f'weight={w}' for w in aresta_comprimento]

        trace_weights = go.Scatter3d(x=x_tx, y=y_tx, z=z_tx,
            mode='markers',
            marker =dict(color='rgb(125,125,125)', size=1), #definindo a mesma cor das linhas e das borda

            text = etext, hoverinfo='text')
        ###########################################################################################

        # Criando as arestas
        trace_edges = go.Scatter3d(x=x_arestas, y=y_arestas, z=z_arestas, mode='lines', line=dict(color='black', width=2), hoverinfo='none')

        # Criando os nós
        trace_nodes = go.Scatter3d(x=x_no, y=y_no, z=z_no, mode='markers', marker=dict(symbol='circle', size=10, color='skyblue'))

        # Inclui traça as arestas e os nós e criar uma figura com os nós e arestas
        data = [trace_edges, trace_nodes, trace_weights]
        fig = go.Figure(data=data)

        # Mostra a figura criada
        fig.show()

    def limpa_grafo(self):
        self.entradas = []
        self.e = []
        self.v = []
        self.maior_vertice = 0
        self.colunas = len(self.entradas)
        self.cores = []
        self.desenhaGrafo()