#Ingrid Vazquez 240090 Atividad 4 Secuencia Fibonacci
#Secuencia de Fibonacci: Genera los primeros N términos de la secuencia de Fibonacci. 
# La secuencia comienza con 0 y 1, y cada término posterior es la suma de los dos términos anteriores. 
# Por ejemplo, si N es 8, la secuencia sería: 0, 1, 1, 2, 3, 5, 8, 13.
n=int(input("Agregue el numero para hacer una secuencia fibonacci "))
secuencia = []
a, b = 0, 1 
for _ in range(n):
        secuencia.append(a)  
        a, b = b, a + b     
print(f" El numero {n} su secuencia de Fibonacci es: {secuencia}")

