LINHA = "linha"
COLUNA = "coluna"

def verificar_tamanho_matriz(matriz):
    quantidade_linhas = len(matriz)
    if quantidade_linhas == 0:
        raise "Matriz sem elementos"
    quantidade_colunas = len(matriz[0])
    for linha in matriz:
        colunas = len(linha)
        if colunas != quantidade_colunas:
            raise "Matriz com tamanho irregular para colunas"
    
    return quantidade_linhas, quantidade_colunas

def calcular_determinante_matriz_3x3(matriz):
    #Calcular determinante usando o método de Sarrus
    qnt_linhas = len(matriz)
    qnt_colunas = qnt_linhas + 2
    nova_matriz = [[0 for _ in range(qnt_colunas)] for _ in range(qnt_linhas)]

    #Copiando a matriz original
    for linha in range(qnt_linhas):
        for coluna in range(qnt_linhas):
            nova_matriz[linha][coluna] = matriz[linha][coluna]

    #Copiando a parte que falta para a matriz nova
    for linha in range(qnt_linhas):
        for coluna in range(3, qnt_colunas):
            nova_matriz[linha][coluna] = matriz[linha][coluna - 3]

    #Calcula os valores das diagonais principais
    diagonais_principais = 0
    for index in range(0, 3):
        valor_diagonal = 1
        coluna = index
        linha  = 0
        maximo_coluna = index + 3
        while coluna < maximo_coluna:
            valor_diagonal *= nova_matriz[linha][coluna]
            coluna += 1
            linha += 1
        diagonais_principais += valor_diagonal

    #Calcula os valores das diagonais secundarias
    diagonais_secundarias = 0
    for index in range(0, 3):
        valor_diagonal = 1
        coluna = index
        linha  = 2
        maximo_coluna = index + 3
        while coluna < maximo_coluna:
            valor_diagonal *= nova_matriz[linha][coluna]
            coluna += 1
            linha -= 1
        diagonais_secundarias += valor_diagonal

    
    return diagonais_principais - diagonais_secundarias

def definir_melhor_escolha_linha_coluna(matriz):
    dicionario = {LINHA : (0, 0), COLUNA : (0, 0)}
    for linha in range(0, len(matriz)):
        valor_linha = 0
        for coluna in range(0, len(matriz)):
            if matriz[linha][coluna] == 0:
               valor_linha += 1
        if dicionario[LINHA][1] < valor_linha:
            dicionario[LINHA] = (linha, valor_linha)
    for coluna in range(0, len(matriz)):
        valor_coluna = 0
        for linha in range(0, len(matriz)):
            if matriz[linha][coluna] == 0:
                valor_coluna += 1
        if dicionario[COLUNA][1] < valor_coluna:
            dicionario[COLUNA] = (coluna, valor_coluna)
    
    if dicionario[LINHA][1] >= dicionario[COLUNA][1]:
        return (LINHA, dicionario[LINHA][0])
    else:
        return (COLUNA, dicionario[COLUNA][0])
            
def calcular_determinante_matriz_2x2(matriz):
    valor_diagonal_principal  = matriz[0][0] * matriz[1][1]
    valor_diagonal_secundaria = matriz[1][0] * matriz[0][1]

    return valor_diagonal_principal - valor_diagonal_secundaria
    
def cortar_matriz(tipo_corte, linha_corte, coluna_corte, matriz):
    ordem = len(matriz)
    ordem_nova_matriz = ordem - 1
    nova_matriz = [[0 for _ in range(0, ordem_nova_matriz)] for _ in range(0, ordem_nova_matriz)]
    linha_nova_matriz = 0
    coluna_nova_matriz = 0
    if tipo_corte == LINHA:
        for linha in range(0, ordem):
            if linha == linha_corte:
                continue
            for coluna in range(0, ordem):
                if coluna != coluna_corte:
                    nova_matriz[linha_nova_matriz][coluna_nova_matriz] = matriz[linha][coluna]
                    coluna_nova_matriz += 1
            linha_nova_matriz += 1
            coluna_nova_matriz = 0
    else:
        incrementa_linha = False
        for linha in range(0, ordem):
            for coluna in range(0, ordem):
                if coluna == coluna_corte:
                    continue
                if linha != linha_corte:
                    nova_matriz[linha_nova_matriz][coluna_nova_matriz] = matriz[linha][coluna]
                    coluna_nova_matriz += 1
                    incrementa_linha = True

            coluna_nova_matriz = 0
            if incrementa_linha:
                linha_nova_matriz += 1
                incrementa_linha = False
    return nova_matriz

def split_linha_arquivo(linha:str):
    valores = linha.replace(" ", "").split(",")
    valores_numericos = []
    for valor in valores:
        valores_numericos.append(float(valor))
    return valores_numericos

def calcular_determinante(matriz):
    qnt_linhas, qnt_colunas = verificar_tamanho_matriz(matriz)
    if qnt_linhas != qnt_colunas:
        raise "Matriz não é uma matriz quadrada"
    
    if qnt_linhas == qnt_colunas ==  1:
        return matriz[0][0]
    
    if qnt_linhas == qnt_colunas == 2:
        return calcular_determinante_matriz_2x2(matriz)
    
    if qnt_linhas == qnt_colunas == 3:
        return calcular_determinante_matriz_3x3(matriz)
    
    elif qnt_linhas == qnt_colunas and qnt_colunas > 3:
        tipo_corte, posicao = definir_melhor_escolha_linha_coluna(matriz)
        ordem = len(matriz)
        determinante = 0
        if tipo_corte == LINHA:
            linha = posicao
            for coluna in range(0, ordem):
                if matriz[linha][coluna] != 0:
                    matriz_reduzida_linha_coluna = cortar_matriz(LINHA, posicao, coluna, matriz)
                    determinante += (matriz[linha][coluna] * (pow(-1, linha + coluna) * calcular_determinante(matriz_reduzida_linha_coluna)))
        else:
            coluna = posicao
            for linha in range(0, ordem):
                if matriz[linha][coluna] != 0:
                    matriz_reduzida_linha_coluna = cortar_matriz(COLUNA, linha, posicao, matriz)
                    determinante += (matriz[linha][coluna] * (pow(-1, linha + coluna) * calcular_determinante(matriz_reduzida_linha_coluna)))
        return determinante
    return None

def app():
    matriz = []
    with open("input.txt", 'r') as arquivo: 
        for linha_entrada in arquivo:
            linha = split_linha_arquivo(linha_entrada)
            matriz.append(linha)

    print(f"Matriz lida tem ordem {len(matriz)}")
    print(matriz)
    print(f"Determinante da matriz = {calcular_determinante(matriz)}")
    
if __name__ == "__main__":
    app()





    # matriz_exemplo_1x1 = [[4]]

    # matriz_exemplo_2x2 = [[1, 2], [2, 6]]

    # matriz_exemplo_3x3 = [[1, -2, 3], [2, 1,  -1], [-2, -1, 2]]

    # matriz_exemplo_4x4 = [[4, 0, 0, 0], [1, 0, 1, 1], [-6, 6, 1, 3], [2, 0, -1, 1]]

    # matriz_exemplo_5x5 = [[1, 2, 3, -3, 1], [0, 4, 0, 0, 0], [0, 1, 0, 1, 1], [0, -6, 6, 1, 3], [0, 2, 0, -1, 1]]

    # matriz_exemplo_6x6 = [[-2, -1, 1, 3, 5, 7], [0, 2, 1, 3, 2, 4], [0, 0, 3, -1, 4, 8], [0, 0, 0, 1, 2, 3], [0, 0, 0, 1, 5, 4], [0, 0, 0, 0, 4, 2]]
    # print(calcular_determinante(matriz_exemplo_6x6))
    # print(cortar_matriz(COLUNA, 2, 1, matriz_exemplo_4x4))
    # print(cortar_matriz(LINHA, 0, 0, matriz_exemplo_4x4))
    # print(definir_melhor_escolha_linha_coluna(matriz_exemplo_4x4))
    # print(definir_melhor_escolha_linha_coluna(matriz_exemplo_5x5))
    # print(calcular_determinante(matriz_exemplo_3x3))
    # print(calcular_determinante_matriz_3x3(matriz_exemplo_3x3))
    # print(calcular_determinante_matriz_2x2(matriz_exemplo_2x2))

