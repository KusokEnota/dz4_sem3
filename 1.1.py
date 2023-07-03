"""1. Напишите функцию для транспонирования матрицы Пример:
[[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]"""

m = [[1, 2, 3], [4, 5, 6]]


def t_m(trans_matrix):
    m_t = [[trans_matrix[j][i] for j in range(len(trans_matrix))] for i in range(len(m[0]))]
    return m_t


print(t_m(m))
