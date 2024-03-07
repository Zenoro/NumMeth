import math
from types import FunctionType


def lst_num(num):
    """
    Вернуть последнюю цифру числа
    """
    return int(str(num)[-1])


def round_to_n_significant_figures(number, n) -> float:
    """
    Округления числа до n значащих цифр
    """
    if number == 0:
        return 0
    return round(number, -int(math.floor(math.log10(abs(number))) - (n-1)))


def find_significant_numbers(num):
    """
    Находит количество значащих цифр
    """
    for i in range(1, len(str(num).replace('.', '')) + 1):
        temp = round_to_n_significant_figures(num, i)
        if temp == num:
            break
    # if (k:=int(num)) == 0:
    return i
    # else:
        # return i + int(math.log10(k))


def count_correct_digits(num, d_num):
    """
    Подсчёт верных цифр после запятой
    """
    thck_ctr, wd_ctr = 0, 0
    sign_num_ctr = find_significant_numbers(num)
    # or len(str(num).split('.')[0]) == 1
    sign_num_ctr_in_float = sign_num_ctr if str(num).startswith('0') else sign_num_ctr - len(str(num).split('.')[0]) 
    for i in range(1, sign_num_ctr_in_float + 2):
        if 1 * 10**(-i) >= d_num:
            wd_ctr += 1
        if 1/2 * 10 ** (-i) >=d_num:
            thck_ctr += 1
        else:
            break
    return thck_ctr, wd_ctr


class Counting_Number:
    """
    Правила подсчета цифр
    """
    def __init__(self, num, zapas=0) -> None:
        self.num = num
        self.extra_sign = zapas
        self.prec_len = 0
        if len(k:=str(num).split('.')) > 1:
            self.prec_len = len(k[1])
        if self.extra_sign:
            self.prec_len -= 1

    def __mul__(self, other):
        if not isinstance(other, Counting_Number):
            res = round(self.num*other, self.prec_len+1)
        else:
            res = round(self.num * other.num, 
                        min(self.prec_len, other.prec_len) + 1)
        return Counting_Number(res, lst_num(res))

    def __add__(self, other):
        if not isinstance(other, Counting_Number):
            raise ValueError
        else:
            res = round(self.num + other.num,
                        min(self.prec_len, other.prec_len) + 1)
            return Counting_Number(res, lst_num(res))
            
    def __sub__(self, other):
        if not isinstance(other, Counting_Number):
            raise ValueError
        else:
            res = round(self.num - other.num,
                        min(self.prec_len, other.prec_len) + 1)
            return Counting_Number(res, lst_num(res))

    def __truediv__(self, other):
        if not isinstance(other, Counting_Number):
            if isinstance(other, float) or isinstance(other, int): 
                res = round(self.num / other, self.prec_len+1)
            else:
                raise ValueError
        else:
            res = round(self.num / other.num,
                        min(self.prec_len, other.prec_len) + 1)
        return Counting_Number(res, lst_num(res))
    
    def functional(self, ff:FunctionType):
        res_of_function = round(ff(self.num), self.prec_len + 1)
        return Counting_Number(res_of_function, lst_num(res_of_function))

    def __str__(self) -> str:
        num, extra_num = self.num, self.extra_sign
        return f"{num=}, {extra_num=}"


class AbsoluteBordersNumber(Counting_Number):
    """
    Метод строгого учета границ абсолютных погрешностей
    """
    def __init__(self, num, absol=0.0, zapas=0.0):
        super().__init__(num, zapas)
        if not absol:
            self.absolut = float('0.' + '0' * self.prec_len + '5')
        else:
            self.absolut = absol

    def __mul__(self, othr):
        if not isinstance(othr, AbsoluteBordersNumber):
            if isinstance(othr, int) or isinstance(othr, float):
                res = self.num * othr
                mul_absolut = self.absolut * othr
            else:
                raise ValueError
        else:
            mul_absolut = othr.num * self.absolut + self.num * othr.absolut
            res = self.num * othr.num
        res = round(res, count_correct_digits(res, mul_absolut)[0] + 1)
        return AbsoluteBordersNumber(res, mul_absolut, lst_num(res))

    def __add__(self, othr):
        if not isinstance(othr, AbsoluteBordersNumber):
            raise ValueError
        else:
            res = self.num + othr.num
            add_absolut = othr.absolut + self.absolut
            correctnums = count_correct_digits(res, add_absolut)[0]
            res = round(res, correctnums + 1)
            return AbsoluteBordersNumber(res, add_absolut, lst_num(res))
    
    def __sub__(self, othr):
        if not isinstance(othr, AbsoluteBordersNumber):
            raise ValueError
        else:
            res = self.num - othr.num
            sub_absolut = othr.absolut + self.absolut
            correctnums = count_correct_digits(res, sub_absolut)[0]
            res = round(res, correctnums + 1)
            return AbsoluteBordersNumber(res, sub_absolut, lst_num(res))
    
    def __truediv__(self, othr):
        if not isinstance(othr, AbsoluteBordersNumber):
            raise ValueError
        else:
            res = self.num / othr.num
            div_absolut = (self.num*othr.absolut + othr.num*self.absolut) / (othr.num ** 2)
            correctnums = count_correct_digits(res, div_absolut)[0]
            res = round(res, correctnums + 1)
            return AbsoluteBordersNumber(res, div_absolut, lst_num(res))

    def functional(self, ff:FunctionType, df:FunctionType):
            res_of_function = round(ff(self.num), self.prec_len + 1)
            absoluteerror = df(self.num) * self.absolut
            return AbsoluteBordersNumber(res_of_function, absoluteerror, lst_num(res_of_function))

    def __str__(self):
        fst = super().__str__()
        absolute = self.absolut
        return fst + f", {absolute=}"


class MaxMinNumbersBorder(Counting_Number):
    """
    По способу границ
    """
    def __init__(self, lb, ub):
        if isinstance(lb, MaxMinNumbersBorder) or isinstance(ub, Counting_Number):
            self.lower_border = lb
            self.upper_border = ub
        else:
            self.lower_border = Counting_Number(lb)
            self.upper_border = Counting_Number(ub)

    def __sum__(self, othr):
        if not isinstance(othr, MaxMinNumbersBorder):
            raise ValueError
        else:
            res_lower = self.lower_border + othr.lower_border
            res_upper = self.upper_border + othr.upper_border
        return MaxMinNumbersBorder(res_lower, res_upper)

    def __mul__(self, othr):
        if not isinstance(othr, MaxMinNumbersBorder):
            res_lower = self.lower_border * othr
            res_upper = self.upper_border * othr
        else:
            res_lower = self.lower_border * othr.lower_border
            res_upper = self.upper_border * othr.upper_border
        return MaxMinNumbersBorder(res_lower, res_upper)

    def __sub__(self, othr):
        if not isinstance(othr, MaxMinNumbersBorder):
            raise ValueError
        else:
            res_lower = self.lower_border - othr.upper_border
            res_upper = self.upper_border - othr.lower_border
            return MaxMinNumbersBorder(res_lower, res_upper)
        
    def __truediv__(self, othr):
        if not isinstance(othr, MaxMinNumbersBorder):
            res_lower = self.lower_border / othr
            res_upper = self.upper_border / othr
        else:
            res_lower = self.lower_border / othr.upper_border
            res_upper = self.upper_border / self.lower_border
        return MaxMinNumbersBorder(res_lower, res_upper)
    
    def __str__(self):
        lwr = str(self.lower_border.num)
        upr = str(self.upper_border.num)
        return ' < '.join([lwr, 'Z', upr])

