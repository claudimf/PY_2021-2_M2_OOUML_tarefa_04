from app.utils import Utilidades
from app.calculos import ControlePopulacional

def main():
    # Endereco da base de dados
    bd_address = "data/bd.xls"

    #Exercicio1 e Exercicio5
    ut_populacao_regiao = Utilidades(bd_address, "Populacao por regiao")
    ut_populacao_regiao.abrirDataset()

    #Exercicio2
    ut_populacao_estado = Utilidades(bd_address, "Populacao por estado")
    ut_populacao_estado.abrirDataset()

    #Exercicio3 e exercício4
    ut_municipios = Utilidades(bd_address, "MunicIpios")
    ut_municipios.abrirDataset()

    cp = ControlePopulacional()
    #Exercicio1
    cp.buscarPopulacaoBrasil(ut_municipios.df)

    #Exercicio2
    cp.qntPopulacaoRegiao(ut_populacao_regiao.df, "Região Norte")

    #Exercicio3
    cp.qntMunicipios(ut_municipios.df, 'São Paulo')

    #Exercicio4
    cp.qntPopulcaoMunicipio(ut_municipios.df, "Dois Vizinhos", "PR")

    #Exercicio 5 - plot
    eixo_x = ut_populacao_regiao.df['REGIAO'].values
    eixo_y = ut_populacao_regiao.df['POPULACAO'].values
    ut_populacao_regiao.plotarGrafico(eixo_x, eixo_y)

#
if __name__ == '__main__':
    main()