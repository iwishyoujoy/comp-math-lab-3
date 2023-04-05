from math import *
from art import *

def print_separator():
    print("---------------------------------------------------")

def rectangular_integration(f, a, b, eps, n, method):
    h = (b-a)/n
    x = [a + i*h for i in range(n+1)]
    if method == 1:
        s = sum([eval(f)*h for f in [f.replace("x", str(x[i])) for i in range(n)]])
    elif method == 2:
        s = sum([eval(f)*h for f in [f.replace("x", str(x[i+1])) for i in range(n)]])
    elif method == 3:
        s = sum([eval(f)*h for f in [f.replace("x", str((x[i]+x[i+1])/2)) for i in range(n)]])
    else:
        return None
    while True:
        t = s
        n *= 2
        h /= 2
        x = [a + i*h for i in range(n+1)]
        if method == 1:
            s = sum([eval(f)*h for f in [f.replace("x", str(x[i])) for i in range(n)]])
        elif method == 2:
            s = sum([eval(f)*h for f in [f.replace("x", str(x[i+1])) for i in range(n)]])
        elif method == 3:
            s = sum([eval(f)*h for f in [f.replace("x", str((x[i]+x[i+1])/2)) for i in range(n)]])
        if abs(s-t) <= eps:
            return s

def trapezoidal_integration(f, a, b, eps, n):
    h = (b-a)/n
    x = [a + i*h for i in range(n+1)]
    s = sum([eval(f)*(h) for f in [f.replace("x", str(x[i])) for i in range(1, n)]])
    s += (h/2)*(eval(f.replace("x", str(x[0]))) + eval(f.replace("x", str(x[n]))))
    while True:
        t = s
        n *= 2
        h /= 2
        x = [a + i*h for i in range(n+1)]
        s = sum([eval(f)*(h) for f in [f.replace("x", str(x[i])) for i in range(1, n)]])
        s += h/2*(eval(f.replace("x", str(x[0]))) + eval(f.replace("x", str(x[n]))))
        if abs(s-t) <= eps:
            return s
        
def simpson_integration(f, a, b, eps, n):
    h = (b-a)/n
    x = [a + i*h for i in range(n+1)]
    s = (h/3)*(eval(f.replace("x", str(a))) + eval(f.replace("x", str(b))))
    s += sum([((h/3)*2)*eval(f.replace("x", str(x[i]))) for i in range(1, n, 2)])
    s += sum([((h/3)*4)*eval(f.replace("x", str(x[i]))) for i in range(2, n-1, 2)])
    while True:
        t = s
        n *= 2
        h /= 2
        x = [a + i*h for i in range(n+1)]
        s = (h/3)*(eval(f.replace("x", str(a))) + eval(f.replace("x", str(b))))
        s += sum([((h/3)*2)*eval(f.replace("x", str(x[i]))) for i in range(1, n, 2)])
        s += sum([((h/3)*4)*eval(f.replace("x", str(x[i]))) for i in range(2, n-1, 2)])
        if abs(s-t) <= eps:
            return s
        
def main():
    choice = int(input("1. 4*x**3 - 3*x**2 + 5*x - 20 \n2. x**3 - 3*x**2 + 6*x - 19 \n3. x**3 - 5*x**2 + 3*x - 16 \n4. 2*x**3 - 4*x**2 + 6*x - 25 \n5. -2*x**3 - 5*x**2 + 7*x - 13 \n6. Ввести свое уравнение \nВыберите уравнение: "))
    match(choice):
        case 1:
            equation = "4*x**3 - 3*x**2 + 5*x - 20"
        case 2: 
            equation = "x**3 - 3*x**2 + 6*x - 19"
        case 3:
            equation = "x**3- 5*x**2 +3*x - 16"
        case 4: 
            equation = "2*x**3 - 4*x**2 + 6*x - 25"
        case 5:
            equation = "-2*x**3 - 5*x**2 + 7*x - 13"
        case 6:
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

    #начальное значение числа разбиения интервала 
    n = 4
    
    method = int(input("Выберите метод: 1 - метод прямоугольников, 2 - метод трапеций, 3 - метод Симпсона: "))
    match(method):
        case 1:
            rectangle_method = int(input("Выберите модификацию: 1 - левые, 2 - правые, 3 - средние: "))
            result = rectangular_integration(equation, a, b, epsilon, n, rectangle_method)
        case 2:
            result = trapezoidal_integration(equation, a, b, epsilon, n)
        case 3:
            result = simpson_integration(equation, a, b, epsilon, n)
        case _:
            exit("Ошибка: Неверный метод")
    
    print_separator()
    tprint("Answer:")
    print(result)

main()


# ТОЧНЫЕ ОТВЕТЫ НА ИСХОДНЫЕ УРАВНЕНИЯ
# 1. 174 [2; 4]
# 2. 2 [2; 4]
# 3. -47.333 [2; 4]
# 4. -40.667 [0; 2]
# 5. -81.333 [1; 3]
