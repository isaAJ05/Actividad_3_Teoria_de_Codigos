# Subrutina: MatrizGeneradora
def MatrizGeneradora(G1, n, k, q): #parametros de entrada: G1, n, k, q
    for i in range(int(k)): #
        codewords = []
        codeword = input(f"Ingrese el codeword {i+1} de longitud {n}: ")
        while len(codeword) != int(n) or not all(char in map(str, range(int(q))) for char in codeword):
            if len(codeword) != int(n):
                print(f"El codeword debe tener una longitud de {n}. Inténtelo de nuevo.")
            elif not all(char in map(str, range(int(q))) for char in codeword):
                print(f"El codeword debe contener solo caracteres en el rango 0 a {int(q)-1}. Inténtelo de nuevo.")
            codeword = input(f"Ingrese el codeword {i+1} de longitud {n}: ")
        codewords.append(codeword)
        G1.append(codewords)


print("Bienvenidx")
print("Ingrese los parametros correspondientes")
n= input("\n ->Ingrese la longitud del código: ")
k= input(" ->Ingrese el número de filas: ")
q= input(" ->Ingrese la cardinalidad del alfabeto: ")
G1 =[] 
G2 =[] 
print("\n Ingrese la Matriz Generadora G1\n")
MatrizGeneradora(G1, n, k, q)
print(G1)
print("\n Ingrese la Matriz Generadora G2\n")
MatrizGeneradora(G2, n, k, q)
print(G2)