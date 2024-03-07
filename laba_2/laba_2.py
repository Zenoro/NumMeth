"""
Практическая работа 2
Округление чисел. Верные значащие цифры
"""

import math
import pandas as pd
from laba_2_extra import *


"""
Задание 1: Число X, все цифры которого верны в строгом смысле, округлите до
трех значащих цифр. Для полученного числа X1=X найдите предельную
абсолютную и предельную относительную погрешности. В записи числа
X1 укажите количество верных цифр (в узком и широком смысле).
"""
numberX = 0.068147


# Округляем число до трех значащих цифр
numberX1 = round_to_n_significant_figures(numberX, 3)
print(f"Округленное число: {numberX1}")


# Находим предельную абсолютную и относительную погрешности
absoluteerror = round(abs(numberX - numberX1), 8)
relativeerror = absoluteerror / numberX
print("Предельная абсолютная погрешность: %f" % absoluteerror)
print(f"Предельная относительная погрешность: {relativeerror}")


# Находим количество верных цифр (в узком и широком смысле)
narrowaccuracy, wideaccuracy = count_correct_digits(numberX1, absoluteerror)
print(f"Количество верных цифр (в узком смысле): {narrowaccuracy}")
print(f"Количество верных цифр (в широком смысле): {wideaccuracy}")


"""
Задание 2
Вычислить значение величины Z при заданных значениях параметров a, b и с, 
используя «ручные» расчетные таблицы для пошаговой регистрации результатов вычислений,
тремя способами:
1) по правилам подсчета цифр;
2) по методу строгого учета границ абсолютных погрешностей;
3) по способу границ.
"""

# ПРИМЕР ИЗ УЧЕБНИКА
# A = 12.762
# B = 0.4534
# C = 0.291
"""
A1, B1, C1 = (AbsoluteBordersNumber(i) for i in [A, B, C]) 
A1B1 = A1 * B1
C4 = C1 * 4
numerator = A1B1 - C4
ln_a = round(math.log(A1.num), A1.prec_len + 1)
LN_a = AbsoluteBordersNumber(ln_a, 1 / (A1.num) * A1.absolut, int(str(ln_a)[-1]))
denum = LN_a + B1
Z = numerator / denum
print(Z)
"""

A = 1.105
B = 6.453
C = 3.54


"""Правила подсчета цифр"""
print("\n  Правила подсчета цифр\n")

A1, B1, C1 = (Counting_Number(i) for i in [A, B, C])
B1_minus_C1 = B1 - C1
numerator = B1_minus_C1 * B1_minus_C1
A1_mul_2 = A1 * 2
denum = A1_mul_2 + B1
Z = numerator / denum
# print(Z)
df1 = pd.DataFrame([['a', A1.num, A1.extra_sign],
                    ['b', B1.num, B1.extra_sign],
                    ['c', C1.num, C1.extra_sign],
                    ['b - c', B1_minus_C1.num, B1_minus_C1.extra_sign],
                    ['(b - c)^2', numerator.num, numerator.extra_sign],
                    ['2*a', A1_mul_2.num, A1_mul_2.extra_sign],
                    ['2*a + b', denum.num, denum.extra_sign],
                    ['Z', Z.num, Z.extra_sign]],
                    columns=["Операция", "Значение", "Запасная цифра"])
print(df1)
# df1.to_csv('res1.csv', index=False)
print()


"""Метод строгого учета границ абсолютных погрешностей"""
print("\n  Метод строгого учета границ абсолютных погрешностей\n")

A1, B1, C1 = (AbsoluteBordersNumber(i) for i in [A, B, C]) 
B1_minus_C1 = B1 - C1
numerator = B1_minus_C1 * B1_minus_C1
A1_mul_2 = A1 * 2
denum = A1_mul_2 + B1
Z = numerator / denum
# print(Z)
df1 = pd.DataFrame([['a', A1.num, A1.extra_sign, 'Δa', A1.absolut],
                    ['b', B1.num, B1.extra_sign, 'Δb', B1.absolut],
                    ['c', C1.num, C1.extra_sign, 'Δc', C1.absolut],
                    ['b - c', B1_minus_C1.num, B1_minus_C1.extra_sign, 'Δ(b-c)', B1_minus_C1.absolut],
                    ['(b - c)^2', numerator.num, numerator.extra_sign, 'Δ((b-c)^2)', numerator.absolut],
                    ['2*a', A1_mul_2.num, A1_mul_2.extra_sign, 'Δ(2*a)', A1_mul_2.absolut],
                    ['2*a + b', denum.num, denum.extra_sign, 'Δ(2*a+b)', denum.absolut],
                    ['Z', Z.num, Z.extra_sign, 'ΔZ', Z.absolut]],
                    columns=["Операция", "Значение", "Запасная цифра", 'Абсолютная погрешность', 'Значение'])
print(df1)
# df1.to_csv('res2.csv', index=False)
print()


"""По способу границ"""
print("\n  По способу границ\n")

# Задаем нижние и верхние границы для чисел
LA1, UA1 = A1.num-A1.absolut, A1.num+A1.absolut
LB1, UB1 = B1.num-B1.absolut, B1.num+B1.absolut
LC1, UC1 = C1.num-C1.absolut, C1.num+C1.absolut

A1 = MaxMinNumbersBorder(LA1, UA1)
B1 = MaxMinNumbersBorder(LB1, UB1)
C1 = MaxMinNumbersBorder(LC1, UC1)

B1_minus_C1 = B1 - C1
numerator = B1_minus_C1 * B1_minus_C1
A1_mul_2 = A1 * 2
denum = B1.__sum__(A1_mul_2)
Z = numerator / denum

df1 = pd.DataFrame([['a', A1.lower_border.num, A1.upper_border.num],
                    ['b', B1.lower_border.num, B1.upper_border.num],
                    ['c', C1.lower_border.num, C1.upper_border.num],
                    ['b - c', B1_minus_C1.lower_border.num, B1_minus_C1.upper_border.num],
                    ['(b - c)^2', numerator.lower_border.num, numerator.upper_border.num],
                    ['2*a', A1_mul_2.lower_border.num, A1_mul_2.upper_border.num],
                    ['2*a + b', denum.lower_border.num, denum.upper_border.num],
                    ['Z', Z.lower_border.num, Z.upper_border.num]],
                    columns=["Операция", "НГ", "ВГ"])
print(df1)
# df1.to_csv('res3.csv', index=False)
print(Z)
print()
