import numpy as np
from math import inf


# do funkcji podaję zmienną fi, która bedzie zliczała zredukowane koszty
def redukcja_macierzy(matrix: list[list], fi=0):
    # wyznaczam minimalne wartości w poszczególnych wierszach
    min_in_rows = np.min(matrix, axis=1)
    for i in range(len(matrix)):
        # jeśli minimalna wartość nie jest równa 0, dodaję ją do fi i odejmuję we wszystkich kolumnach
        if min_in_rows[i] != 0:
            fi += min_in_rows[i]
            for j in range(len(matrix[i])):
                matrix[i][j] -= min_in_rows[i]
    # wyznaczam minimalne wartosci w kolumnach
    min_in_cols = np.min(matrix, axis=0)
    for i in range(len(matrix[0])):
        # jeśli minimalna wartość nie jest równa 0, dodaję ją do fi i odejmuję we wszystkich wierszach
        if min_in_cols[i] != 0:
            fi += min_in_cols[i]
            for j in range(len(matrix)):
                matrix[j][i] -= min_in_cols[i]
    print(matrix)
    return matrix, fi