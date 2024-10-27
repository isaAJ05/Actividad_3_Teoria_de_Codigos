import numpy as np 
from itertools import product

i

#Funcion HallarCodewords
def hallar_codewords(matriz, q, k): # Hallar los codewords a partir de la matriz generadora
    # Asegurarse de que la matriz es una matriz de NumPy
    if not isinstance(matriz, np.ndarray):
        matriz = np.array(matriz)
    v = [] 
    for i in range(q): # Vector de 0 a q-1 para sacar las combinaciones lineales
        v.append(i)
    combinaciones = list(product(v, repeat=k)) # Combinaciones de los elementos de v

    codewords = []
    for U in combinaciones: # Multiplicar las combinaciones por la matriz generadora
        U = np.array(U) 
        codeword = np.dot(U, matriz) % q # Producto punto y módulo q para Fq
        codewords.append(codeword.tolist()) # Agregar a la lista de codewords
    return codewords

print("Bienvenidx")
print("Porfavor ingrese los siguientes parametros para la matriz generadora G1 y G2")
n= input(int("\n ->Digite la longitud del código (n): "))
k= input(int(" ->Digite la dimensión del codigo (k): "))
q= input(int(" ->Digite la cardinalidad del alfabeto (q): "))
G1 =[] 
G2 =[] 
print("\n Ingrese la Matriz Generadora G1\n")
MatrizGeneradora(G1, n, k, q)
print("\n Ingrese la Matriz Generadora G2\n")
MatrizGeneradora(G2, n, k, q)
print("\n Codewords G1\n")
hallar_codewords(G1, q, k)
print("\n Codewords G2\n")
hallar_codewords(G2, q, k)