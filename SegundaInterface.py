import networkx as nx
import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
import io
from grafo import Grafo




def start():
    sg.theme(new_theme='Reddit')
    sg.theme_border_width(border_width=5)

    sg.theme_background_color(color='Cyan')

    layout_cores = [
        [sg.Text('Opções de Cores', background_color="Cyan", font=('Arial, 14'))],
        [sg.Text('blue', background_color ='blue', size=(10,0))],
        [sg.Text('pink', background_color='pink', size=(10, 0))],
        [sg.Text('yellow', background_color='yellow', size=(10, 0))],
        [sg.Text('green', background_color='green', size=(10, 0))],
        [sg.Text('red', background_color='red', size=(10, 0))],
        [sg.Text('violet', background_color='violet', size=(10, 0))],
        [sg.Text('gray', background_color='gray', size=(10, 0))],
        [sg.Text('coral', background_color='coral', size=(10, 0))],
        [sg.Text('orange', background_color='orange', size=(10, 0))],
        [sg.Text('gold', background_color='gold', size=(10, 0))],
        [sg.Text('black', background_color='black', size=(10, 0))],
        [sg.Text('skyblue', background_color='skyblue', size=(10, 0))],
        [sg.Text('brown', background_color='brown', size=(10, 0))],
        [sg.Text('lightgreen', background_color='lightgreen', size=(10, 0))],
        [sg.Text('orangered', background_color='orangered', size=(10, 0))],



    ]

    window_cor = sg.Window("Opção de Cores", layout_cores, finalize=True, size=(200, 600))

    evento, valor = window_cor.read()
    window_cor.close()

