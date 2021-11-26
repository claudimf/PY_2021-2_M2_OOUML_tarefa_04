class ControlePopulacional:

    def formatar(self, quantidade):
        return '{:,}'.format(quantidade).replace(",", ".")


    #Exercicio 1
    def buscarPopulacaoBrasil(self, df):
        total = 0
        for linha in df['POPULACAO']:
            total+=linha
        print("População total do Brasil =", total)

    #Exercicio 2
    def qntPopulacaoRegiao(self, df, regiao):
        total_regiao = 0
        filtro_regiao = df['REGIAO'] == regiao
        df_regiao = df[filtro_regiao]
        for linha in df_regiao['POPULACAO']:
            total_regiao +=linha
        #total_regiao = df.loc[df['REGIAO']== regiao, 'POPULACAO'].sum()
        print("Valor total(Populacao por regiao) =", total_regiao)

    #Exercicio 3
    def qntMunicipios(self, df, estado):
        total_municipios = df.loc[df['UF'] == estado, 'MUNICIPIO'].count()
        print("Número de municipios por estado:", total_municipios)

    #Exercicio4
    def qntPopulcaoMunicipio(self, df, municipio, uf):
        filtro = df.loc[(df['MUNICIPIO']== municipio) & (df['UF'] == uf)]
        total_pop_muni = filtro['POPULACAO'].values[0]
        print("O total da população na cidade de ", municipio, " é:", total_pop_muni)
    

    #Imprima o estado com a menor população
    def menorPopulacaoEstado(self, df):
        filtro = df.loc[(df['POPULACAO'] == df['POPULACAO'].min())]
        quantidade_formatada = self.formatar(filtro['POPULACAO'].values[0])
        estado = filtro['ESTADOS'].values[0]
        print("Estado com a menor população:", estado, "e a quantidade é: ", quantidade_formatada, "habitantes.")

    #Imprima o estado com a maior população
    def maiorPopulacaoEstado(self, df):
        filtro = df.loc[(df['POPULACAO'] == df['POPULACAO'].max())]
        quantidade_formatada = self.formatar(filtro['POPULACAO'].values[0])
        estado = filtro['ESTADOS'].values[0]
        print("Estado com a maior população:", estado, "e a quantidade é: ", quantidade_formatada, "habitantes.")