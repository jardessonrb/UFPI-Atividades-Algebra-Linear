import numpy as np
from sympy import symbols, det, Eq, solve, Matrix

class Calculador:
    def __init__(self, matriz):
       self.matriz_base = matriz
    
    def calcular_autovalores_matriz(self):
        variavel_lambda = symbols('L')

        matriz_base_matrix = Matrix(self.matriz_base)

        for i in range(matriz_base_matrix.shape[0]):
            matriz_base_matrix[i, i] -= variavel_lambda

        polinomio_caracteristico = det(matriz_base_matrix)

       
        autovalores = solve(Eq(polinomio_caracteristico, 0), variavel_lambda)

        return autovalores
    
    def traduzir_autovalores_dicionario(self, dicionario_autovetor: dict, variaveis):
        valores = []
        novo_dicionario = {str(chave): valor for chave, valor in dicionario_autovetor.items()}
        for variavel in variaveis:
            if variavel in novo_dicionario:
                valor = novo_dicionario[variavel]
                valor = ""+str(valor)
                if "*" in valor:
                    numero = valor.split("*")
                    valores.append(numero[0])
                elif "sqrt" in valor:
                    valores.append(valor)
                elif valor in variaveis:
                    valores.append("1")
                else:
                    if '-' in valor and valor[1:] in variaveis:
                        valores.append("-1")
                    else:
                        valores.append(valor)
                
            else:
            
                valores.append("1")
        return valores
        
    def traduzir_autovetor(self, dicionario_autovetor, variaveis):
        valores = []
        if isinstance(dicionario_autovetor, list):
            for dicionario in dicionario_autovetor:
                valores.append(self.traduzir_autovalores_dicionario(dicionario, variaveis))
        elif isinstance(dicionario_autovetor, dict):
            return self.traduzir_autovalores_dicionario(dicionario_autovetor, variaveis)
        
        return valores

    
    def calcular_autovetores(self, autovalores):
        nomes_variaveis = [f'x{i}' for i in range(len(self.matriz_base))]
        variaveis_str = ' '.join(nomes_variaveis)
        variaveis = symbols(variaveis_str)
        matriz = Matrix(self.matriz_base)

        autovetores = []

        for autovalor in autovalores:
            A_minus_lambdaI = matriz.copy()
            for i in range(matriz.shape[0]):
                A_minus_lambdaI[i, i] -= autovalor

            valores_autovetor = []

            sistema_equacoes = []
            for linha in range(matriz.shape[0]):
                equacao = Eq(sum(A_minus_lambdaI[linha, col] * variaveis[col] for col in range(matriz.shape[1])), 0)
                sistema_equacoes.append(equacao)

            solucao = solve(sistema_equacoes, nomes_variaveis)
            print(solucao)
            print(self.traduzir_autovetor(solucao, nomes_variaveis))

        return autovetores


def converter_entreda(entrada: str):
    numeros_str = entrada.replace(" ", "").split(',')

    numeros_float = [float(numero) for numero in numeros_str]

    return numeros_float

def ler_entrada():
    ordem = int(input("Ordem da matriz: "))
    matriz = []
    for i in range(ordem):
        entrada = input(f'Digite a linha {i+1} matriz, com valores separados por virgula: ')
        linha_base = converter_entreda(entrada)
        matriz.append(linha_base)

    return matriz

def main():
    # matriz = ler_entrada()

    # matriz = [[-3, 1, -3], [20, 3, 10], [2, -2, 4]]
    matriz = [[1, 4], [2, 3]]

    calculador = Calculador(matriz)
    autovalores = calculador.calcular_autovalores_matriz()
    print(autovalores)
    autovetores = calculador.calcular_autovetores(autovalores)


if __name__ == "__main__":
    main()