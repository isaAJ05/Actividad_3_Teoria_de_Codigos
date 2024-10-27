import numpy as np
from itertools import product

def MatrizGeneradora(G, n, k, q): # parámetros de entrada: G, n, k, q
    for i in range(int(k)): # itera sobre el rango de k que es el número de filas
        codeword = input(f"Ingrese el codeword {i+1} de longitud {n}: ") # solicita el codeword
        # valida que el codeword tenga la longitud correcta y que pertenezca al q solicitado
        while len(codeword) != int(n) or not all(char in map(str, range(int(q))) for char in codeword): # mientras no cumpla con las condiciones
            if len(codeword) != int(n): # si la longitud no es la correcta
                print(f"El codeword debe tener una longitud de {n}. Inténtelo de nuevo.")
            elif not all(char in map(str, range(int(q))) for char in codeword): # si no pertenece al q solicitado
                print(f"El codeword debe contener solo caracteres en el rango 0 a {int(q)-1}. Inténtelo de nuevo.")
            codeword = input(f"Ingrese el codeword {i+1} de longitud {n}: ") # solicita nuevamente el codeword
        G.append([int(char) for char in codeword]) # agrega el codeword a la matriz generadora como una lista de enteros
    return np.array(G) # retorna la matriz generadora como una matriz de NumPy

def hallar_codewords(matriz, q, k): # Hallar los codewords a partir de la matriz generadora
    # Asegurarse de que la matriz es una matriz de NumPy
    if not isinstance(matriz, np.ndarray):
        matriz = np.array(matriz)
    
    v = list(range(q)) # Vector de 0 a q-1 para sacar las combinaciones lineales
    combinaciones = list(product(v, repeat=k)) # Combinaciones de los elementos de v

    codewords = []
    for U in combinaciones: # Multiplicar las combinaciones por la matriz generadora
        U = np.array(U) 
        codeword = np.dot(U, matriz) % q # Producto punto y módulo q para Fq
        codewords.append(codeword.tolist()) # Agregar a la lista de codewords
    return codewords

# Ejemplo de uso
print("Bienvenidx")
print("Porfavor ingrese los siguientes parametros para la matriz generadora G1 y G2")
n = int(input("\n ->Digite la longitud del código (n): "))
k = int(input(" ->Digite la dimensión del codigo (k): "))
q = int(input(" ->Digite la cardinalidad del alfabeto (q): "))
G1 = []
G2 =[] 
print("\n Ingrese la Matriz Generadora G1\n")
G1 = MatrizGeneradora(G1, n, k, q)
print("\n Ingrese la Matriz Generadora G2\n")
G2 = MatrizGeneradora(G2, n, k, q)
print("\n Codewords G1\n")
codewords_G1 = hallar_codewords(G1, q, k)
print(codewords_G1)
print("\n Codewords G2\n")
codewords_G2 = hallar_codewords(G2, q, k)
print(codewords_G2)