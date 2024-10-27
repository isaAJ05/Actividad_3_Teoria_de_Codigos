print("Bienvenidx")
print("Ingrese su Matriz Generadora")
n= input("Ingrese la longitud del código: ")
k= input("Ingrese el número de filas: ")
q= input("Ingrese la cardinalidad del alfabeto: ")
for i in range(k):
    for j in range(n):
        print("Ingrese el valor de la posición", i, j)
        matriz[i][j]= input()