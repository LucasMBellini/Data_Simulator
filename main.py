# Dice simulator
# Random 1 at 6
from random import *
import PySimpleGUI as sg

class DiceSimulator:
    def __init__(self):
        self.valor_min = 1
        self.valor_max = 6
        #Layout
        self.layout = [
            [sg.Text('Lançar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def start(self):
        # Window
        self.janela = sg.Window('Dice Simulator', layout=self.layout)
        # Read the valors
        self.eventos, self.valores = self.janela.Read()
        # Action
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.ValorDice()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Obrigado por participar')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def ValorDice(self):
        print(randint(self.valor_min, self.valor_max))

simulator = DiceSimulator()
simulator.start()
