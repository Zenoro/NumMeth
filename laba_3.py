"""
Лабораторная работа №3
Анализ последовательности данных

Цель работы — построение развилок и циклических конструкций 
в программах, составление программ анализа потоков данных.

Вариант 1
"""
from math import cos, pi
import numpy as np
import time
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
start_time = time.time()


"""Функция для варианта 1 + установка параметров"""
KDEG = 1
MDEG = 1
JDEG = 1
main_func = lambda x: -(cos(pi*x**MDEG / 2)**KDEG) + 2*x**JDEG


"""Задаем экспериментальный отрезок и шаг"""
a = 0
b = 10
N = 100000
h = (b-a) / N


"""1) Найти максимальное значение функции и номер узла"""
xs = np.array([a + i*h for i in range(N)])
main_res = np.array(list(map(main_func, xs)))
fmax = np.max(main_res)
fmax_index, = np.where(main_res == fmax)[0] + 1
print(f"\n{fmax = }")
print(f"Номер узла: {fmax_index}\n")


"""2) Найти минимальное значение функции"""
fmin = np.min(main_res)
fmin_index, = np.where(main_res == fmin)[0] + 1
print(f"{fmin = }")
print(f"Номер узла: {fmin_index}\n")


"""3) среднее значение f, 
      средний квадрат f и 
      среднеквадратичное значение fт функции"""
f_mean = np.mean(main_res)
f_sqr_mean = np.mean(main_res**2)
f_sqrt_sqr_mean = (f_sqr_mean) ** 0.5
print(f"Среднее значение f = {f_mean}")
print(f"Средний квадрат f = {f_sqr_mean}")
print(f"Среднеквадратичное значение f = {f_sqrt_sqr_mean}\n")


"""4) относительное число положительных р+ 
      и отрицательных р- значений функции"""
print("Относительное число положительных и отрицательных \
значений функции")
p_plus = sum(main_res > 0) / N
p_minus = sum(main_res < 0) / N
print(f"p+ = {p_plus}")
print(f"p- = {p_minus}\n")


"""5) среднеквадратичное отклонение от среднего значения"""
sigma1 = np.std(main_res)
print(f"Среднеквадратичное отклонение от среднего значения = {sigma1}\n")


"""Вывод времени работы программы (прихоть автора)"""
print(f"Время работы: {time.time() - start_time}\n")


"""Построение графика функции"""
plt.figure(1)
plt.title(f"График функции при {N} узлах")
plt.plot(xs, main_res)
plt.grid()
plt.show()
