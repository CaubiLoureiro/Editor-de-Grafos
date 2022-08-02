import PySimpleGUI as sg
from PIL import Image
import io
from grafo import Grafo
from SegundaInterface import start

GRAFO = Grafo()

sg.theme(new_theme='Reddit')
sg.theme_border_width(border_width = 5)

sg.theme_background_color(color = 'Cyan')

#Layout
layout = [
    [sg.Text('Adicionar:', size=(15,0), background_color='Black', justification='center', font=('Arial, 11'), text_color='White'),
     sg.Text('Vértice 1:', size=(10, 0), background_color='Cyan', justification='left'), sg.Input(size=(10, 1), key='vertice1'),
     sg.Text('Peso do Vértice 1:', size=(10, 0), background_color='Cyan', justification='left'), sg.Input(size=(10, 1), key='peso1'),
     sg.Text('Vértice 2:', size=(10,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='vertice2'),
     sg.Text('Peso do Vértice 2:',size=(10,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='peso2'),
     sg.Text('Comprimento da Aresta:', size=(10,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='comprimento')
     ],

    [sg.Text('Remover Aresta:', size=(15,0), background_color='Black', justification='center', font=('Arial, 11'), text_color='White'),
     sg.Text('Vértice 1:', size=(10,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='v1_remove_aresta'),
     sg.Text('Vértice 2:', size=(10,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='v2_remove_aresta')],

    [sg.Text('Modificar Aresta:', background_color='Black', size=(15,0), justification='center', font=('Arial, 11'), text_color='White'),
     sg.Text('Vértice 1:', size=(10,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='v1_mod_aresta'),
     sg.Text('Vértice 2:', size=(10,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='v2_mod_aresta'),
     sg.Text(' '*10, background_color='Cyan'), sg.Text('Novo Comprimento(opcional):', size=(20,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='novo_comprimento'),
     sg.Text(' '*10, background_color='Cyan'), sg.Text('Cor(opcional):', size=(10,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='cor'),
     sg.Button('Opções de cores', key='op_cor')],

    [sg.Text('Remover Vértice', background_color='Black', size=(15,0), justification='center', font=('Arial, 11'), text_color='White'),
     sg.Text('Vértice \npara remoção:', size=(10,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='remove_v1')],

    [sg.Text('Modificar Vértice', background_color='Black', size=(15,0), justification='center', font=('Arial, 11'), text_color='White'),
     sg.Text('Vértice \npara modificação:', size=(12,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='modifica_v1'),
     sg.Text('Novo Peso:', size=(10,0), background_color='Cyan', justification='left'), sg.Input(size=(10,1), key='novo_peso')],

    [sg.Text('_' * 208, background_color='Cyan', justification='left')],

    [sg.Button('Adicionar', key='adicionar', size=(20,0)),
     sg.Text(' '*10, background_color='Cyan'), sg.Button('Remover Aresta',  key='remove_aresta', size=(20,0)),
     sg.Text(' '*10, background_color='Cyan'), sg.Button('Modificar Aresta', key='modifica_aresta', size=(20,0)),
     sg.Text(' '*10, background_color='Cyan'), sg.Button('Remove Vértice', key='remove_vertice', size=(20,0)),
     sg.Text(' '*10, background_color='Cyan'), sg.Button('Modificar Vértice', key='modifica_vertice', size=(20,0))],

    [sg.Text('_' * 208, background_color='Cyan', justification='left')],

    [sg.Text('GRAFO', background_color='Cyan', justification='Left', font=('Arial', 14))],

    [sg.Button('Visualizar Matriz de Adjacência', key='visu_ad', size=(25,0)),
     sg.Text(' '*2, background_color='Cyan'), sg.Button('Visualizar Matriz de Incidência', key='visu_inci',size=(25,0)),
     sg.Text(' '*2, background_color='Cyan'), sg.Button("Visualizar Pesos", key='visu_pesos',size=(25,0)),
     sg.Text(' '*2, background_color='Cyan'), sg.Button("Visualizar Grafo", key='visualisar_grafo',size=(25,0)),
     sg.Text(' '*2, background_color='Cyan'), sg.Button("Visualizar Grafo 3D", key='visualizar_3D', size=(25,0)),
     sg.Text(' '*2, background_color='Cyan'), sg.Button("Limpar Grafo", key='limpar_grafo',size=(25,0))
     ],

    [sg.Text(' ', size=(50,30), background_color='Cyan'), sg.Image(key='-IMAGEM_GRAFO-'), sg.Image(key='-IMAGEM_PESO-')]
]


    #janela
window = sg.Window("Editor de Grafos",layout, finalize=True, size=(1500, 950))

def atualiza_frame(arquivo):
    image = Image.open(arquivo)
    image.thumbnail((1000, 1000))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window["-IMAGEM_GRAFO-"].update(data=bio.getvalue())



atualiza_frame("tela_preta.png")


while True:
    # Extrair os dados da tela
    event, values = window.Read()


    if (event == sg.WIN_CLOSED):
        break

    elif (event == 'adicionar'):
        try:
            entrada = [0]*5
            entrada[0] = int(values['vertice1'])
            entrada[1] = int(values['vertice2'])
            entrada[2] = int(values['comprimento'])
            entrada[3] = int(values['peso1'])
            entrada[4] = int(values['peso2'])
            GRAFO.adiciona_aresta(entrada)
            atualiza_frame("graph.png")
        except:
            continue

    elif (event == 'remove_aresta'):
        try:
            entrada = [0] * 2
            entrada[0] = int(values['v1_remove_aresta'])
            entrada[1] = int(values['v2_remove_aresta'])
            GRAFO.remove_aresta(entrada)
            atualiza_frame("graph.png")
        except:
            continue

    elif (event == 'modifica_aresta'):
        try:
            if(values['cor'] == '' and values['novo_comprimento'] != ''):
                entrada = [0] * 4
                entrada[0] = int(values['v1_mod_aresta'])
                entrada[1] = int(values['v2_mod_aresta'])
                entrada[2] = int(values['novo_comprimento'])
                entrada[3] = ''

                GRAFO.modifica_aresta(entrada)
                atualiza_frame("graph.png")

            elif (values['cor'] != '' and values['novo_comprimento'] == ''):
                entrada = [0] * 4
                entrada[0] = int(values['v1_mod_aresta'])
                entrada[1] = int(values['v2_mod_aresta'])
                entrada[2] = ''
                entrada[3] = str(values['cor'])

                GRAFO.modifica_aresta(entrada)
                atualiza_frame("graph.png")

            elif (values['cor'] != '' and values['novo_comprimento'] != ''):
                entrada = [0] * 4
                entrada[0] = int(values['v1_mod_aresta'])
                entrada[1] = int(values['v2_mod_aresta'])
                entrada[2] = int(values['novo_comprimento'])
                entrada[3] = str(values['cor'])
                GRAFO.modifica_aresta(entrada)
                atualiza_frame("graph.png")

            else:
                continue
        except:
            continue

    elif (event == 'remove_vertice'):

        try:
            entrada = [0]
            entrada[0] = int(values['remove_v1'])
            GRAFO.remove_no(entrada[0])
            atualiza_frame("graph.png")
        except:
            continue

    elif (event == 'modifica_vertice'):
        try:
            entrada = [0]*2
            entrada[0] = int(values['modifica_v1'])
            entrada[1] = int(values['novo_peso'])
            GRAFO.modifica_pesos(entrada[0], entrada[1])
            atualiza_frame("graph.png")
        except:
            continue

    elif (event == 'visualisar_grafo'):

        GRAFO.desenhaGrafoSeparado()

    elif (event == 'limpar_grafo'):
        GRAFO.limpa_grafo()
        atualiza_frame("tela_preta.png")

    elif (event == 'visu_pesos'):
        GRAFO.tabela_pesos()

    elif (event == 'visu_inci'):
        GRAFO.desenha_matriz_incidente()

    elif (event == 'visu_ad'):
        GRAFO.desenha_matriz_adjacente()

    elif (event == 'visualizar_3D'):
        GRAFO.desenha3D()

    elif (event == 'op_cor'):
        start()

