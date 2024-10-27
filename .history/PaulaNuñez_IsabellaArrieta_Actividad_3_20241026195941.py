print("Bienvenidx")
print("Ingrese su Matriz Generadora")
n= input("Ingrese la longitud del código: ")
k= input("Ingrese el número de filas: ")
q= input("Ingrese la cardinalidad del alfabeto: ")
G1= [[0 for x in range(n)] for y in range(k)]
for i in range(k):
    for j in range(n):
        print("Ingrese el valor de la posición", i, j)
        G1[i][j]= input()