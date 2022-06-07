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
    return matrix


tab = [[inf, 2, 3, 4, 1, 3, 6, 5, 6, 8],
       [9, inf, 4, 3, 8, 3, 5, 1, 6, 3],
       [3, 4, inf, 4, 1, 6, 7, 2, 9, 3],
       [8, 6, 2, inf, 3, 2, 6, 4, 5, 5],
       [7, 4, 5, 3, inf, 7, 8, 1, 4, 6],
       [2, 3, 1, 5, 7, inf, 2, 1, 5, 4],
       [3, 4, 2, 8, 9, 1, inf, 5, 6, 3],
       [8, 4, 5, 6, 1, 2, 3, inf, 6, 1],
       [7, 2, 4, 5, 3, 6, 4, 7, inf, 5],
       [4, 1, 3, 1, 6, 3, 7, 8, 9, inf]]

print(np.array(redukcja_macierzy(tab)))