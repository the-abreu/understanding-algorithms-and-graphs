def insertion_sort(array):
    # Percorre o vetor a partir do segundo elemento
    for j in range(1, len(array)):

        # Elemento que será inserido na posição correta
        key = array[j]

        # Último elemento da sequência já ordenada
        i = j - 1

        # Desloca para a direita os elementos maiores que a chave
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1

        # Insere a chave na posição correta
        array[i + 1] = key

    return array