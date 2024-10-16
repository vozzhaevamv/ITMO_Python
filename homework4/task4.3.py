import numpy as np
matrixa = np.random.rand(10, 10)
det = np.linalg.det(matrixa)
if np.isclose(det, 0):
    print("Матрица вырождена, определитель равен:", det)
else:
    print("Определитель матрицы:", det)
transposed_matrix = matrixa.T
print(transposed_matrix)
rank = np.linalg.matrix_rank(matrixa)
print("Ранг матрицы:", rank)
eigenvalues, eigenvectors = np.linalg.eig(matrixa)
print("Собственные значения:", eigenvalues)
print("Собственные векторы:", eigenvectors)
matrixa2 = np.random.rand(10, 10)
summatrix= matrixa + matrixa2
print("Сумма матриц:",summatrix)
multiplication = np.dot(matrixa, matrixa2)
print("Произведение матриц:",multiplication)