from Operador import soma_matrizes, subtrai_matrizes, multiplicao_matrizes
from colorama import init, Fore

# Inicialize o colorama
init(autoreset=True)

def equals(esperado, resultado):
    if esperado == resultado:
        print(Fore.GREEN + "Match: esperado == resultado")
    else:
        print(Fore.RED + "No Match: esperado != resultado")
        print("Esperado: ")
        print(esperado)
        print("Resultado: ")
        print(resultado)

def testeSomaMatrizes():
    print(Fore.YELLOW + "Teste de soma de matrizes")
    matriz1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    matriz2 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

    esperado = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
    resultado = soma_matrizes(matriz1, matriz2)
    equals(esperado, resultado)

def testeSubtracaoMatrizes():
    print(Fore.YELLOW + "Teste de subtração de matrizes")
    matriz1 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    matriz2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    esperado = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    resultado = subtrai_matrizes(matriz1, matriz2)
    equals(esperado, resultado)

def testeMultiplicacaoMatrizes():
    print(Fore.YELLOW + "Teste de multiplicação de matrizes")
    matriz1 = [[1, 1], [2, 2]]
    matriz2 = [[0, 1], [1, 0]]

    
    #[0] = 1 * 0 + 1 * 1 = 1
    #[1] = 1 * 1 + 1 * 0 = 1
    #[2] = 2 * 0 + 2 * 1 = 2
    #[3] = 2 * 1 + 2 * 0 = 2 

    esperado = [[1, 1], [2, 0]]
    resultado = multiplicao_matrizes(matriz1, matriz2)
    equals(esperado, resultado)


def main():
    matriz_exemplo = [[0, 1, 1, 1, 1],
                      [1, 0, 1, 1, 0],
                      [0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1],
                      [0, 0, 0, 1, 0]]

    testeSomaMatrizes()
    testeSubtracaoMatrizes()
    testeMultiplicacaoMatrizes()

if __name__ == "__main__":
    main()