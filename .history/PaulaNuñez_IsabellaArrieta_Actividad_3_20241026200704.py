print("Bienvenidx")
print("Ingrese los parametros correspondientes")
n= input("Ingrese la longitud del código: ")
k= input("Ingrese el número de filas: ")
q= input("Ingrese la cardinalidad del alfabeto: ")

G1 =[] 
G2 =[] 
print("Ingrese la Matriz Generadora G1")
def MatrizGeneradora(G1):
for i in range(int(k)):
    codeword = []
    codeword = input(f"Ingrese el codeword {i+1} de longitud {n}: ")
    while len(codeword) != int(n):
        print(f"El codeword debe tener una longitud de {n}. Inténtelo de nuevo.")
        codeword = input(f"Ingrese el codeword {i+1} de longitud {n}: ")
    G1.append(codeword)