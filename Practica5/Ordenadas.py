#Ingrid Vazquez 240090

def f(x):
    return x**3 + 1
x = 0
while x <= 30:
    y = f(x)
    if y % 2 == 0:
        print(f"Abscisa: {x}, Ordenada: {y}")
    x += 1
