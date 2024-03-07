"""
Лабораторная работа №1
Решение прямой и обратной задач теории погрешности.
"""

import math as mh
from decimal import Decimal

"""Изначальная функция"""
func = lambda a, b, t: (a**2 + b**3) / mh.cos(t)


"""Производные для нахождения допустимых погрешностей аргументов"""
def func_da(a: float, t: float)->float:
    return abs(2*a/mh.cos(t))

def func_db(b: float , t: float)->float:
    return abs(3*(b**2)/mh.cos(t))

def func_dt(a: float, b: float , t: float)->float:
    return abs((((a**2)+(b**3))*mh.sin(t))/(mh.cos(t))**2)


def error_rate(a: float, b: float , t: float, m: int)->float:
    ans = str(func(a, b, t))
    if ans[0]!="0":
        print("Прямая задача")
        
        # ДАНО
        absol_a, absol_b, absol_t = 0.02, 0.01, 0.0001

        # Поиск относительных погрешностей
        delta_a = absol_a/a
        delta_b = absol_b/b
        print("δa =", delta_a)
        print("δb =", delta_b)

        # подсчет абсолютной погрешности аргументов
        squered_absol_a = Decimal(2*delta_a*a**2)
        cube_absol_b = Decimal(3*delta_b*b**3)
        
        # подсчет абсолютной погрешности числителя
        absol_head_sum= squered_absol_a + cube_absol_b
        print("Δa^2+Δb^3 =", Decimal(absol_head_sum))

        # подсчет относительной погрешности числителя
        delta_head = absol_head_sum/(Decimal(a**2+b**3))
        print("δ(a^2+b^3) =", Decimal(delta_head))

        # подсчет абсолютной и относительной погрешности знаменателя
        absol_cosT = mh.sin(t) * absol_t
        print("Δcos(t) =", Decimal(absol_cosT))
        delta_cosT = Decimal(absol_cosT/mh.cos(t))
        print("δcos(t) =", Decimal(delta_cosT))

        # подсчет значения функции
        print("F =", func(a,b,t))
        # подсчет относительной погрешности функции
        print("δF =", (delta_F:=delta_head+delta_cosT))
        # подсчет значения функции
        print('ΔF =', Decimal(func(a,b,t)) * delta_F)
        print("----------------------------------------------")
        print("Обратная задача")
        print("F =", ans)
        print("ΔF =", 0.5*10**(-1*len(ans[:m+1].split(".")[-1])))
        print("F' =", eval(str(ans)[:m+1]))

        # Вывод допустимых погрешностей аргументов
        FF = 0.5*10**(-1*len(ans[:m+1].split(".")[-1]))
        print("Δa =", Decimal(FF / (3*func_da(a, t))))
        print("Δb =", Decimal(FF / (3*func_db(b, t))))
        print("Δt =", Decimal(FF / (3*func_dt(a, b, t))))
        return 0


error_rate(28.3, 7.45, 0.7854, 5)
