import numpy as np
from art import *

def print_separator():
    print("---------------------------------------------------")

def singularity_integration(f, a, b, eps):
    from sympy import sympify, lambdify
    f = sympify(f)
    f = lambdify("x", f)
    
    def recurse(f, a, b, eps, I0=np.inf):
        N = 10

        m = (a+b) / 2
        h = (b-a) / (N-2)
        x = np.linspace(a, b, N)[1:-1]
        y = f(x)

        if not np.isfinite(y).all():
            I = 0
            for (x, y) in zip(x, y):
                if not np.isfinite(y):
                    I += recurse(f, a, x, eps)
                    a = x
            I += recurse(f, a, b, eps)
            return I

        I_l = np.sum(y[:len(x)//2]) * h
        I_r = np.sum(y[len(x)//2:]) * h
        I = I_l + I_r

        if abs(I0 - I) < eps:
            return I
        else:
            return recurse(f, a, m, eps, I_l) + recurse(f, m, b, eps, I_r)
    with np.errstate(divide='ignore'):
        return recurse(f, a, b, eps)


def improper_intergration():
    choice = int(input("1. 1/sqrt(x) \n2. 1/sqrt(1-x) \n3. 1/sqrt(abs(x)) \n4. log(x) \n5. Ввести свое уравнение \nВыберите уравнение: "))
    match(choice):
        case 1:
            equation = "1/sqrt(x)"
        case 2: 
            equation = "1/sqrt(1-x)"
        case 3:
            equation = "1/sqrt(abs(x))"
        case 4: 
            equation = "log(x)"
        case 5:
            equation = input("Введите уравнение: ")
        case _:
            exit("Ошибка: Неверный ввод")

    print_separator()
    
    try:
        a = float(input("Введите нижний предел интегрирования: "))
        b = float(input("Введите верхний предел интегрирования: "))
        epsilon = float(input("Введите точность вычисления: "))
    except:
        exit("Ошибка: Неверное значение данных")
    
    print_separator()
    tprint("Answer:")
    print(singularity_integration(equation, a, b, epsilon))

improper_intergration()

# ТОЧНЫЕ ОТВЕТЫ НА ИСХОДНЫЕ УРАВНЕНИЯ ДЛЯ НЕСОБСТВЕННЫХ ИНТЕГРАЛОВ
# 1. 2 [0; 1]
# 2. 2 [0; 1]
# 3. 4 [-1; 1]
# 4. -1 [0; 1]
