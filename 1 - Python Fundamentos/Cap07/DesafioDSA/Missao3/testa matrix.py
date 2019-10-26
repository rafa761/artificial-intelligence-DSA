max_cols = 4
max_rows = 8
matrix = [[1] * max_cols for _ in range(max_rows)]
matrix[1][1] = 0
matrix[2][2] = 0
matrix[3][0] = 0
matrix[4][2] = 0
matrix[5][3] = 0
matrix[6][1] = 0
matrix[6][3] = 0
matrix[7][1] = 0

matrix[7][2] = 0


def find_path(matrix):
    if not matrix:
        return None
    if len(matrix) <= 1:
        return None

    fim_matrix = (len(matrix) - 1, len(matrix[0]) - 1)
    posicao_atual = [0, 0]
    caminho = [(0, 0)]
    while (andar_vertical(posicao_atual[0], posicao_atual[1])) or (andar_horizontal(posicao_atual[0], posicao_atual[1])):
        if andar_vertical(posicao_atual[0], posicao_atual[1]):
            posicao_atual[0] += 1
            caminho.append(tuple(posicao_atual))
        elif andar_horizontal(posicao_atual[0], posicao_atual[1]):
            posicao_atual[1] += 1
            caminho.append(tuple(posicao_atual))

    if caminho[-1] == fim_matrix:
        return caminho
    else:
        return None



def andar_vertical(linha, coluna):
    linha += 1
    try:
        if matrix[linha][coluna] == 0:
            return False
        if linha >= len(matrix):
            return False
    except:
        return False
    return True


def andar_horizontal(linha, coluna):
    coluna += 1
    try:
        if matrix[linha][coluna] == 0:
            return False
        if coluna >= len(matrix[0]):
            return False
    except:
        return False
    return True


if __name__ == "__main__":
    print(find_path(matrix))
