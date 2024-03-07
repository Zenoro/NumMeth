import math
import pandas as pd

def round_to_n_significant_figures(number:float, n:int) -> float:
    """
    Округления числа до n значащих цифр
    """
    if number == 0:
        return 0
    return round(number, -int(math.floor(math.log10(abs(number))) - (n-1)))


def find_significant_numbers(num) -> int:
    """
    Находит количество значащих цифр
    """
    strnum = str(num)
    for i in range(1, len(strnum.replace('.', ''))):
        if round_to_n_significant_figures(num, i) == num:
            break
    # how_many_nums_after_num = len(strnum[i+1:])
    how_many_nums_after_num = 0
    if (k:=int(num)) == 0:
        return i + how_many_nums_after_num
    else:
        return i + int(math.log10(k)) + 1 + how_many_nums_after_num


def count_correct_digits(num, d_num):
    thck_ctr, wd_ctr = 0, 0
    sign_num_ctr = find_significant_numbers(num)
    sign_num_ctr_in_float = sign_num_ctr if str(num).startswith('0') else sign_num_ctr - len(str(num).split('.')[0]) 
    for i in range(1, sign_num_ctr_in_float):
        if 1 * 10**(-i) >= d_num:
            wd_ctr += 1
        if 1/2 * 10 ** (-i) >=d_num:
            thck_ctr += 1
    return thck_ctr, wd_ctr

# print(round_to_n_significant_figures(0.0330, 2))
# print(find_significant_numbers(0.003300))
# print(count_correct_digits(7.33, 0.005))

df1 = pd.DataFrame([[1,'Bob', 'Builder'],
                  [2,'Sally', 'Baker'],
                  [3,'Scott', 'Candle Stick Maker']],
                  column=["Операция", "Значение", "Запасная цифра"])
print(df1)
# df1.to_csv("free.csv", index=False)
