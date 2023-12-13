from colorama import init, Fore

init(autoreset=True)

def valida_matrizes(primeira_matriz, segunda_matriz):
    linhas_primeira_matriz, colunas_primeira_matriz = verificar_tamanho_matriz(primeira_matriz)
    linhas_segunda_matriz, colunas_segunda_matriz = verificar_tamanho_matriz(segunda_matriz)

    if linhas_primeira_matriz != linhas_segunda_matriz or colunas_primeira_matriz != colunas_segunda_matriz:
        raise "Matrizes com tamanhos incompativeis"
    
    return linhas_primeira_matriz, colunas_primeira_matriz
    
def verificar_tamanho_matriz(matriz):
    quantidade_linhas = len(matriz)
    if quantidade_linhas == 0:
        raise "Matriz sem elementos"
    quantidade_coluna = len(matriz[0])
    for linha in matriz:
        colunas = len(linha)
        if colunas != quantidade_coluna:
            raise "Matriz com tamanho irregular para colunas"
    
    return quantidade_linhas, quantidade_coluna


def multiplicacao_linha_coluna(primeira_matriz, linha_primeira_matriz, segunda_matriz, coluna_segunda_matriz):
    soma = 0
    limite = len(primeira_matriz[linha_primeira_matriz])
    for i in range(0, limite):
        soma += (primeira_matriz[linha_primeira_matriz][i] * segunda_matriz[i][coluna_segunda_matriz])

    return soma


def soma_matrizes(primeira_matriz, segunda_matriz):
    quantidade_linhas, quantidade_coluna = valida_matrizes(primeira_matriz, segunda_matriz)

    matriz_soma = [[0 for _ in range(quantidade_coluna)] for _ in range(quantidade_linhas)]

    for linha in range(0, quantidade_linhas):
        for coluna in range(0, quantidade_coluna):
            matriz_soma[linha][coluna] = primeira_matriz[linha][coluna] + segunda_matriz[linha][coluna]

    return matriz_soma

def subtrai_matrizes(primeira_matriz, segunda_matriz):
    quantidade_linhas, quantidade_coluna = valida_matrizes(primeira_matriz, segunda_matriz)

    matriz_subtracao = [[0 for _ in range(quantidade_coluna)] for _ in range(quantidade_linhas)]

    for linha in range(0, quantidade_linhas):
        for coluna in range(0, quantidade_coluna):
            matriz_subtracao[linha][coluna] = primeira_matriz[linha][coluna] - segunda_matriz[linha][coluna]

    return matriz_subtracao

def multiplicao_matrizes(primeira_matriz, segunda_matriz):
    linhas_primeira_matriz, colunas_primeira_matriz = verificar_tamanho_matriz(primeira_matriz)
    linhas_segunda_matriz, colunas_segunda_matriz = verificar_tamanho_matriz(segunda_matriz)

    if colunas_primeira_matriz != linhas_segunda_matriz:
        raise "Número de colunas da primeira matriz é diferente da segunda matriz"
    

    matriz_multiplicao = [[0 for _ in range(colunas_segunda_matriz)] for _ in range(linhas_primeira_matriz)]

    for linha in range(0, linhas_primeira_matriz):
        for coluna in range(0, colunas_segunda_matriz):
            matriz_multiplicao[linha][coluna] = multiplicacao_linha_coluna(primeira_matriz, linha, segunda_matriz, coluna)

    return matriz_multiplicao

def calcular_quantas_comunicacoes_diretas(matriz):
    conjuto_comunicacoes_diretas = set()
    linhas, colunas = verificar_tamanho_matriz(matriz)
    for linha in range(0, linhas):
        for coluna in range(0, colunas):
            if(matriz[linha][coluna] == 1):
                conjuto_comunicacoes_diretas.add((linha, coluna))
    return conjuto_comunicacoes_diretas

def calcular_quantas_ligacoes_com_no_maximo_uma_retransmissao(matriz):
    matriz_com_ligacoes_bidirecionais = multiplicar_matriz(matriz, 2)
    conjuto_comunicacoes_bidirecionais = set()

    linhas, colunas = verificar_tamanho_matriz(matriz_com_ligacoes_bidirecionais)
    print(matriz_com_ligacoes_bidirecionais)
    for linha in range(0, linhas):
        for coluna in range(0, colunas):
            if(matriz_com_ligacoes_bidirecionais[linha][coluna] == 1):
                conjuto_comunicacoes_bidirecionais.add((linha, coluna))

    return conjuto_comunicacoes_bidirecionais

def calcular_quantas_ligacoes_com_no_maximo_duas_retransmissoes(matriz):
    matriz_com_ligacoes_bidirecionais = soma_matrizes(matriz, multiplicar_matriz(matriz, 2))
    conjuto_comunicacoes_bidirecionais = set()

    linhas, colunas = verificar_tamanho_matriz(matriz_com_ligacoes_bidirecionais)
    for linha in range(0, linhas):
        for coluna in range(0, colunas):
            if(matriz_com_ligacoes_bidirecionais[linha][coluna] == 2):
                conjuto_comunicacoes_bidirecionais.add((linha, coluna))
    return conjuto_comunicacoes_bidirecionais

def calcular_quantas_ligacoes_com_mais_de_duas_retransmissoes(matriz):
    matriz_com_ligacoes_bidirecionais = multiplicao_matrizes(matriz, matriz)
    conjuto_comunicacoes_bidirecionais = set()

    linhas, colunas = verificar_tamanho_matriz(matriz_com_ligacoes_bidirecionais)
    for linha in range(0, linhas):
        for coluna in range(0, colunas):
            if(matriz_com_ligacoes_bidirecionais[linha][coluna] == 3):
                conjuto_comunicacoes_bidirecionais.add((linha, coluna))

    print(Fore.MAGENTA + f"Possui {len(conjuto_comunicacoes_bidirecionais)} ligacoes com mais de duas retransmissões entres os pontos")
    for saida, chegada in conjuto_comunicacoes_bidirecionais:
        print(f"Sai de {saida + 1} para -> {chegada + 1}")
    print(matriz_com_ligacoes_bidirecionais)


    

def caminhos_entre_duas_estacoes(matriz, origem, destino):
    linhas, colunas = verificar_tamanho_matriz(matriz)
    grafo = [[] for _ in range(linhas)]
    for linha in range(0, linhas):
        for coluna in range(0, colunas):
            if(matriz[linha][coluna] == 1):
                grafo[linha].append(coluna)
    
    return None

def multiplicar_matriz(matriz, vezes):
    if vezes == 1:
        return matriz
    if vezes == 2:
        return multiplicao_matrizes(matriz, matriz)
    elif vezes > 2:
        matriz_resultado = matriz
        for i in range(0, vezes - 1):
            matriz_resultado = multiplicao_matrizes(matriz_resultado, matriz)
        return matriz_resultado
    raise "Valor do expoente inválido"

def preencher_matriz():
    print("Digite quantas linhas e colunas a matriz terá um numero em cada linhas")
    linhas = int(input("Qnt linhas: "))
    colunas = int(input("Qnt colunas: "))

    matriz_input = [[] for _ in range(linhas)]
    for linha in range(0, linhas):
        print(f"linha {linha + 1}")
        for _ in range(0, colunas):
            matriz_input[linha].append(float(input()))

    return matriz_input

def app():
    matriz_exemplo = [[0, 1, 1, 1, 1],
                      [1, 0, 1, 1, 0],
                      [0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1],
                      [0, 0, 0, 1, 0]]
    matriz_input = []

    opcoes = [1, 2, 3, 4, 5]
    print("+++++++++++++++++++++++++++++++++++++++++++++++++:")
    print("Opcoes:")
    print("1 ver quantas e quais ligacoes diretas entre dois pontos A e B")
    print("2 ver quantas e quais comunicações com uma retransmissao")
    print("3 ver quantas e quais com duas retransmissoes")
    print("4 exponenciação de matriz na forma (Amxn)^expoente")
    print("5 para sair")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++:")
    while True:
        opcao = int(input("Digite o numero da opcao:"))
        if opcao not in opcoes:
            print("Opcao invalida")
            continue

        if opcao == 5:
            print(Fore.YELLOW + "Saindo ...")
            break

        if opcao == 1:
            print("Digite dois pontos que deseja saber se existe comunicação direta:")
            saida   = int(input("Digite estacao saida:"))
            chegada = int(input("Digite estacao chegada:"))
            opc = int(input("Digite 1 para digitar uma nova matriz e 2 para usar matriz padrao: "))
            conjunto = []
            matriz = []
            if opc == 2:
                matriz = matriz_exemplo
                conjunto = calcular_quantas_comunicacoes_diretas(matriz_exemplo)
            elif opc == 1:
                matriz = preencher_matriz()
                conjunto = calcular_quantas_comunicacoes_diretas(matriz)
            else:
                print("Operação não valida.")
            existe = False
            for s, c in conjunto:
                if saida == s and chegada == c:
                    print(Fore.GREEN + f"Existe um caminho direto entre {s} -> {c}")
                    existe = True
                    break
            print(matriz)
            if not existe:
                print(Fore.RED + f"Não existe um caminho direto entre {saida} -> {chegada}")
        
        if opcao == 2:
            opc = int(input("Digite 1 para digitar uma nova matriz e 2 para usar matriz padrao: "))
            conjunto = []
            if opc == 2:
                conjunto = calcular_quantas_ligacoes_com_no_maximo_uma_retransmissao(matriz_exemplo)
            elif opc == 1:
                matriz_input = preencher_matriz()
                conjunto = calcular_quantas_ligacoes_com_no_maximo_uma_retransmissao(matriz_input)
            else:
                print(Fore.RED + "Operação não valida.")
            
            opc = int(input("Digite 1 para ver todos os pontos 2 para dois pontos:"))
            if opc == 1:
                print(Fore.YELLOW + f"Possui {len(conjunto)} ligacoes com uma retransmissão entres os pontos")
                for saida, chegada in conjunto:
                    print(f"Sai de {saida} para -> {chegada}")
            elif opc == 2:
                existe = False
                saida   = int(input("Digite estacao saida:"))
                chegada = int(input("Digite estacao chegada:"))
                for s, c in conjunto:
                    if saida == s and c == chegada:
                        print(f"Sai de {saida} para -> {chegada}")
                        existe = True
                        break

                if not existe:
                    print(Fore.RED + f"Não existe um caminho direto entre {saida} -> {chegada}")
            else:
                print(Fore.RED + "Operação não valida.")

        if opcao == 3:
            opc = int(input("Digite 1 para digitar uma nova matriz e 2 para usar matriz padrao: "))
            conjunto = []
            if opc == 2:
                conjunto = calcular_quantas_ligacoes_com_no_maximo_duas_retransmissoes(matriz_exemplo)
            elif opc == 1:
                matriz_input = preencher_matriz()
                conjunto = calcular_quantas_ligacoes_com_no_maximo_duas_retransmissoes(matriz_input)
            else:
                print(Fore.RED + "Operação não valida.")
            
            opc = int(input("Digite 1 para ver todos os pontos 2 para dois pontos:"))
            if opc == 1:
                print(Fore.YELLOW + f"Possui {len(conjunto)} ligacoes com duas retransmissões entres os pontos")
                for saida, chegada in conjunto:
                    print(Fore.GREEN + f"Sai de {saida} para -> {chegada}")

            elif opc == 2:
                existe = False
                saida   = int(input("Digite estacao saida:"))
                chegada = int(input("Digite estacao chegada:"))
                for s, c in conjunto:
                    if saida == s and c == chegada:
                        print(Fore.GREEN + f"Sai de {saida} para -> {chegada}")
                        existe = True
                        break
                if not existe:
                    print(Fore.RED + f"Não existe um caminho direto entre {saida} -> {chegada}")

            else:
                print(Fore.RED + "Operação não valida.")


        if opcao == 4:
            opc = int(input("Digite 1 para digitar uma nova matriz e 2 para usar matriz padrao: "))
            matriz = []
            if opc == 2:
                matriz = matriz_exemplo
            elif opc == 1:
                matriz = preencher_matriz()
                
            expoente = int(input("Digite o expoente: "))
            matriz_resultado = multiplicar_matriz(matriz, expoente)
            print("Matriz original:")
            print(matriz)
            print(f"Matriz elevado a {expoente}")
            print(matriz_resultado)


def main():
    app()


if __name__ == "__main__":
    main()