from sympy import symbols, Eq, solve, sympify

class Solucao:
    def __init__(self, vetor: list[float], base_espaco: list[list[float]]) -> None:
        self.dimensao = len(vetor)
        self.vetor = vetor

        if(self.dimensao != len(base_espaco)):
            raise ValueError("A base não possui a mesma dimensão do espaço")
        
        self.base = base_espaco

    def obter_variaveis_vs_base(self, variaveis: list[str]):
        print("\nVariaveis do sistema")
        print(variaveis)
        variavel_vs_base = []
        for i in range(self.dimensao):
            vetor_variavel_elemento = []
            for j in range(self.dimensao):
                # print(f'{i}-{j} = {self.base[i][j]}')
                multiplicacao_variavel = ""
                if(self.base[i][j] == 0.0):
                    multiplicacao_variavel = "0"

                elif(self.base[i][j] > 0.0):
                    if(self.base[i][j] == 1.0):
                        multiplicacao_variavel = variaveis[i]+""
                    else:
                        multiplicacao_variavel = f'{self.base[i][j]}*{variaveis[i]}'
                
                elif(self.base[i][j] < 0.0):
                     if(self.base[i][j] == -1.0):
                        multiplicacao_variavel = "-"+variaveis[i]
                     else:
                        multiplicacao_variavel = f'{self.base[i][j]}*{variaveis[i]}'
                else:
                    multiplicacao_variavel = variaveis[i]+"*"+str(self.base[i][j])
                vetor_variavel_elemento.append(multiplicacao_variavel)
            variavel_vs_base.append(vetor_variavel_elemento)
                
        print("\nVariaveis vezes a base")
        print(variavel_vs_base)

        return variavel_vs_base

    def obter_variaveis(self):
        variaveis = []
        for i in range(self.dimensao):
            variaveis.append("x"+str(i))
        
        return variaveis
    
    def obter_equacoes_de_soma_elemento_base(self, variavel_vs_base):
        equacoes = []
        for i in range(self.dimensao):
            equacao = ""
            for j in range(self.dimensao):
                if(self.base[j][i] != 0.0):
                    if(variavel_vs_base[j][i][0] == '-'):
                        equacao += variavel_vs_base[j][i]
                    else:
                        if(j > 0):
                            equacao += f'+{variavel_vs_base[j][i]}'
                        else:
                            equacao += variavel_vs_base[j][i]
            equacoes.append(equacao)
        
        print("\nSoma dos elementos da base")
        print(equacoes)

        return equacoes
    
    def obter_equacoes_sympy(self, equacoes):
        equacoes_sistema =[]
        for indice in range(self.dimensao):
            equacoes_sistema.append(Eq(sympify(equacoes[indice]), self.vetor[indice]))
        
        print("\nEquações do sistema")
        print(equacoes_sistema)

        return equacoes_sistema
    
    def produto_interno_vetores(self, vetor1, vetor2):
        tamanho_vetores = len(vetor1)
        produto_interno = 0
        for i in range(tamanho_vetores):
            produto_interno += vetor1[i] * vetor2[i]
            
        return produto_interno
    
    def multiplicacao_vetor_por_escalar(self, escalar, vetor):
        tamanho_vetores = len(vetor)
        novo_vetor = []
        for i in range(tamanho_vetores):
            novo_vetor.append(escalar * vetor[i])
            
        return novo_vetor

    def subtracao_vetores(self, vetor1, vetor2):
        tamanho_vetores = len(vetor1)
        novo_vetor = []
        for i in range(tamanho_vetores):
            novo_vetor.append(vetor1[i] - vetor2[i])
            
        return novo_vetor
    
    def transformar_base_em_base_ortonormal(self):
        vetores_base_ortonormal = []
        vetores_base_ortonormal.append(self.base[0])

        for i in range(1, len(self.base)):
            vetor_atual = []
            for j in range(i):

                divisao_produto_interno = self.produto_interno_vetores(self.base[i], vetores_base_ortonormal[j]) / self.produto_interno_vetores(vetores_base_ortonormal[j], vetores_base_ortonormal[j])
                
                vetor_multiplicado_por_escalar = self.multiplicacao_vetor_por_escalar(divisao_produto_interno, vetores_base_ortonormal[j])

                if(len(vetor_atual) == 0):
                    vetor_atual = self.subtracao_vetores(self.base[i],  vetor_multiplicado_por_escalar)
                else:
                    vetor_atual = self.subtracao_vetores(vetor_atual, vetor_multiplicado_por_escalar)

            vetores_base_ortonormal.append(vetor_atual)

        print(vetores_base_ortonormal)
        return vetores_base_ortonormal
    
    def resolver_coordenadas_primeira_base(self):
        print("Vetor de entrada")
        print(self.vetor)
        print("Base de entrada")
        print(self.base)

        variaveis = self.obter_variaveis()
        variavel_vs_base = self.obter_variaveis_vs_base(variaveis)
        equacoes = self.obter_equacoes_de_soma_elemento_base(variavel_vs_base)
        
        variaveis_sistema = symbols(variaveis)
        equacoes_sistema  = self.obter_equacoes_sympy(equacoes)

        coordenadas_sistema = solve(equacoes_sistema, variaveis_sistema)

        # print("\nCoordenadas do sistema")
        # print(coordenadas_sistema)

        return coordenadas_sistema
    
    def resolver_coordenadas_base_ortonormal(self, base_ortonormal):
        self.base = base_ortonormal

        print("\n\nRecalcular as coordenadas com a base ortonormal")
        coordenadas = self.resolver_coordenadas_primeira_base()
        # print("Coordenadas do vetor na nova base ortonormal")
        # print(coordenadas)

        return coordenadas



    def resolver(self):
        print("\nCoordenadas 1° Base\n")
        coordenadas_base_inicial  = self.resolver_coordenadas_primeira_base()

        base_inicial = self.base

        print("\nCoordenadas Base Ortonormal\n")
        base_ortonormal = self.transformar_base_em_base_ortonormal()

        coordenadas_base_ortonormal = self.resolver_coordenadas_base_ortonormal(base_ortonormal)

        print("\n\nBase inicial")
        print(base_inicial)
        print("Coordenada base inicial")
        print(coordenadas_base_inicial)

        print("\n\nBase ortonormal")
        print(base_ortonormal)
        print("Coordenada base ortonormal")
        print(coordenadas_base_ortonormal)

def converter_entreda(entrada: str):
    numeros_str = entrada.replace(" ", "").split(',')

    numeros_float = [float(numero) for numero in numeros_str]

    return numeros_float

def ler_entrada():
    entrada = input("Digite o vetor origem com valores separados por virgula: ")
    vetor = converter_entreda(entrada)
    base = []
    for i in range(len(vetor)):
        entrada = input(f'Digite a linha {i+1} da base, com valores separados por virgula: ')
        linha_base = converter_entreda(entrada)
        base.append(linha_base)

    return (vetor, base)
        

def main():
    # vetor_b2 = [2, 4]
    # base_b2 = [[1, 1], [0, 1]]
    # vetor_b3 = [1, 0, 0]
    # base_b3 = [[1, 1, 1], [-1, 1, 0], [1, 0, -1]]
    # base_b4 = [[1, 0, 1], [1, 1, 0], [0, 0, 1]]
    # base_b2 = [[2, -1], [3, 4]]
    # solucao3 = Solucao(vetor_b3, base_b3)
    # solucao2 = Solucao(vetor_b2, base_b2)
    vetor, base = ler_entrada()
    solucao_completa = Solucao(vetor, base)
    solucao_completa.resolver()

if __name__ == "__main__":
    main()