import numpy as np 
from itertools import product,permutations

# Funcion MatrizGeneradora
def MatrizGeneradora(G, n, k, q):
    # parámetros de entrada: G1, n, k, q
    for i in range(k):  # itera sobre el rango de k que es el número de filas
        lista = []  #para cada vector
        generador = input(f"Ingrese el vector generador {i+1} de longitud {n}: ")  # solicita el vector generador
        # valida que el vector generador tenga la longitud correcta y que pertenezca al q solicitado
        while len(generador) != n or not all(char in map(str, range(q)) for char in generador):  # mientras no cumpla con las condiciones
            if len(generador) != n:  # si la longitud no es la correcta
                print(f"El vector generador debe tener una longitud de {n}. Inténtelo de nuevo.")
            elif not all(char in map(str, range((q))) for char in generador):  # si no pertenece al q solicitado
                print(f"El vector generador debe contener solo caracteres en el rango 0 a {q-1}. Inténtelo de nuevo.")
            generador = input(f"Ingrese el vector generador {i+1} de longitud {n}: ")  # solicita nuevamente el vector
        G.append([int(char) for char in generador]) # agrega el vector generador a la matriz generadora como una lista de enteros
    return np.array(G) # retorna la matriz generadora como una matriz de NumPy

#Funcion HallarCodewords
def hallar_codewords(matriz, q, k): # Hallar los codewords a partir de la matriz generadora
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

def verificar_permutacion(G1, G2):
    n = G1.shape[1]
    for perm in permutations(range(n)):
        G1_permutada = G1[:, perm]
        if np.array_equal(G1_permutada, G2):
            return True, perm
    return False, None

print("Bienvenidx")
print("Porfavor ingrese los siguientes parametros para la matriz generadora G1 y G2")
n = int(input("->Digite la longitud del código (n): "))
k = int(input(" ->Digite la dimensión del codigo (k): "))
q = int(input(" ->Digite la cardinalidad del alfabeto (q): "))
G1 = []
G2 =[] 
print("\nIngrese la Matriz Generadora G1")
G1 = MatrizGeneradora(G1, n, k, q)
print("\nIngrese la Matriz Generadora G2")
G2 = MatrizGeneradora(G2, n, k, q)
print("\nMatriz G1:")
print(G1)
print("\nMatriz G2:")
print(G2)
print("\n Codewords G1")
codewords_G1 = hallar_codewords(G1, q, k)
print("→ C1= ", codewords_G1)
print("\n Codewords G2")
codewords_G2 = hallar_codewords(G2, q, k)
print("→ C2= ", codewords_G2)

equivalentes, permutacion = verificar_permutacion(G1, G2)
if equivalentes:
    print("\nLas matrices generadoras son equivalentes mediante la permutación de columnas:", permutacion)
else:
    print("\nLas matrices generadoras no son equivalentes mediante permutaciones de columnas.")