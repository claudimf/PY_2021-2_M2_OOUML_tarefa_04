import pandas as pd
from matplotlib import pyplot as plt

class Utilidades:

    #Abrir dataset
    def __init__(self, nome_df, aba_df):
        self.nome = nome_df
        self.aba = aba_df

    #Usa o pandas para abrir o xls
    def abrirDataset(self):
        self.df = pd.read_excel(self.nome, sheet_name=self.aba)
        return self.df

    #Exercicio5
    def plotarGrafico(self, eixo_x, eixo_y):
        plt.bar(eixo_x, eixo_y)
        plt.ticklabel_format(style='plain', axis='y')
        plt.show()
