print("Bienvenidx")
print("Ingrese su Matriz Generadora")
n= input("Ingrese la longitud del código: ")
k= input("Ingrese el número de filas: ")
q= input("Ingrese la cardinalidad del alfabeto: ")
G1 = [[0 for x in range(int(n))] for y in range(int(k))]
G2 = [[0 for x in range(int(n))] for y in range(int(k))]

codewords = []
for i in range(int(k)):
    codeword = input(f"Ingrese el codeword {i+1} de longitud {n}: ")
    while len(codeword) != int(n):
        print(f"El codeword debe tener una longitud de {n}. Inténtelo de nuevo.")
        codeword = input(f"Ingrese el codeword {i+1} de longitud {n}: ")
    codewords.append(codeword)