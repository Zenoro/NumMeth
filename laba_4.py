"""
Лабораторная работа №4
МЕТОДЫ РЕШЕНИЯ СЛАУ

    Задание:
Дана система четырех уравнений с четырьмя неизвестными:  
1. Решите систему уравнений методом Гаусса.  
2. Для матрицы системы найдите обратную. 
3.  Зная,  что  свободные  члены  исходной  системы  имеют 
абсолютную  погрешность  0,001,  найдите  оценку  абсолютной  и 
относительной погрешности решения. 
4. Преобразуйте систему к виду, необходимому для применения 
метода  простой  итерации.  Выбрав  в  качестве  начального 
приближения  x0=0,  найдите  k0 необходимое  число  итеративных 
шагов для решения системы методом простой итерации с точностью 
0,01. 
"""

import numpy as np
import math

# MATRIX = np.array([[4.003, 0.207, 0.519, 0.281],
#                    [0.416, 3.273, 0.326, 0.375],
#                    [0.297, 0.351, 2.997, 0.429],
#                    [0.412, 0.194, 0.215, 3.628]])
# TARGET = np.array([0.425, 0.021, 0.213, 0.946])
"""ПРИМЕР ИЗ УЧЕБНИКА"""
MATRIX = np.array([[5.526, 0.305, 0.887, 0.037],
                   [0.658, 2.453, 0.678, 0.192],
                   [0.398, 0.232, 4.957, 0.567],
                   [0.081, 0.521, 0.192, 4.988]])
TARGET = np.array([0.774, 0.245, 0.343, 0.263])

"""Задание 1"""
print("   Задание 1")

def gaussElim(a, b):
    """Решение СЛАУ методом Гаусса"""
    b_buf = b.copy()
    n = len(b_buf)
    # Фаза удаления строк
    for k in range(0, n-1):
        for i in range(k+1, n):
            if a[i,k] != 0.0:
                # если не пустое - определяем λ
                lam = a[i,k] / a[k,k]
                # подсчет новой строки матрицы
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                # изменение вектора b
                b_buf[i] = b_buf[i] - lam*b_buf[k]
                # обратная замена
    for k in range(n-1, -1, -1):
        b_buf[k] = (b_buf[k] - np.dot(a[k,k+1:n], b_buf[k+1:n])) / a[k,k]
    return b_buf

GAUSS_SOLUTION = gaussElim(MATRIX, TARGET)
# print(np.linalg.solve(MATRIX, TARGET))
# print(', '.join([f'x{i}={GAUSS_SOLUTION[i-1]}' for i in range(1,5)]))
print(GAUSS_SOLUTION)


"""Задание 2"""
print("\n   Задание 2")

MATRIX_INVERT = np.linalg.inv(MATRIX)
print(MATRIX_INVERT)


"""Задание 3"""
print("\n   Задание 3")

MATRIX_norma = np.linalg.norm(MATRIX, ord=np.inf)
MATRIX_INV_norma = np.linalg.norm(MATRIX_INVERT, ord=np.inf)
TARGET_norma = np.linalg.norm(TARGET, ord=np.inf)

absoluteerror_b = 10**(-3)
absoluteerror_x = MATRIX_INV_norma * absoluteerror_b
print("Абсолютная погрешность решения: Δx < ", absoluteerror_x)
relativeerror_b = absoluteerror_b / TARGET_norma
relativeerror_x = MATRIX_norma * MATRIX_INV_norma * relativeerror_b
print("Относительная погрешность решения: δx < ", relativeerror_x)


"""Задание 4"""
print("\n   Задание 4")

# Преобразование матрицы к необходимому виду
BMATRIX = MATRIX.copy()
CMATRIX = TARGET.copy()
for i in range(len(CMATRIX)):
    CMATRIX[i] /= BMATRIX[i][i]
    BMATRIX[i] /= BMATRIX[i][i]
    BMATRIX[i] = -BMATRIX[i]
    BMATRIX[i][i] = 0
# print(BMATRIX)
    
# Подсчет количества итераций
if (BMATRIX_norm:=np.linalg.norm(BMATRIX, ord=np.inf)) >= 1:
    quit("B norm more than 1 error")
else:
    eps = 0.01
    CMATRIX_norm = np.linalg.norm(CMATRIX, ord=np.inf)
    iter_num = math.ceil(math.log(eps*(1-BMATRIX_norm)/CMATRIX_norm) / math.log(BMATRIX_norm))
    reses = []
    reses.append(CMATRIX)
    for i in range(1, iter_num):
        reses.append(BMATRIX.dot(reses[-1]) + CMATRIX)

for num, elem in enumerate(reses):
    print(f"X{num + 1}: {elem}")
print("Значение последней итерации меньше заданного значения: ", np.linalg.norm(reses[-1] - reses[-2]) < eps)
