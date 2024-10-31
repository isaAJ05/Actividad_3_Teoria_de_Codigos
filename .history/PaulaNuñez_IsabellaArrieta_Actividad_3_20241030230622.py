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
    # Formatear los codewords para que se vea de la forma de un codigo lineal
    formateadito_codewords = ','.join(f'({"".join(map(str, cw))})' for cw in codewords)

    return formateadito_codewords

def encontrar_ciclos(perm): #perm es una lista que representa una permutación de índices
    n = len(perm) # Longitud de la permutación
    visitado = [False] * n  # Lista para marcar los elementos que ya han sido visitados
    ciclos = []  # Lista para almacenar los ciclos encontrados
    for i in range(n):
        if not visitado[i]:  # Si el elemento no ha sido visitado
            ciclo = []  # Lista para almacenar el ciclo actual
            x = i
            while not visitado[x]:  # Mientras el elemento no haya sido visitado
                visitado[x] = True  # Marcar el elemento como visitado
                ciclo.append(x + 1)  # Agregar el elemento al ciclo, ajustando para que arranque desde 1
                x = perm[x]  # Moverse al siguiente elemento en la permutación
            if len(ciclo) > 1:  # Si el ciclo tiene más de un elemento
                ciclos.append(ciclo)  # Agregar el ciclo a la lista de ciclos

    return ciclos # Retorna lista de ciclos, donde cada ciclo es una lista de índices ajustados para que arranquen desde 1

def permutaciones(G1, G2, q):  # longitud de la matriz generadora
    n = G1.shape[1]  # longitud de la matriz generadora
    operaciones = []  # Lista para almacenar las operaciones necesarias para convertir G1 en G2
    for perm in permutations(range(n)):  # Iterar sobre todas las permutaciones posibles de las columnas
        G1_permutada = G1[:, perm]  # Aplicar la permutación a las columnas de G1
        for escalares in product(range(1, q), repeat=n):  # Iterar sobre todos los escalares posibles
            G1_escalada= np.mod(G1_permutada * escalares, q)
            if np.array_equal(G1_escalada, G2):  # Verificar si la matriz permutada es igual a G2
                es_equivalente= True
                ciclos = encontrar_ciclos(perm)  # Encontrar los ciclos en la permutación
                # Convertir los ciclos en una cadena en notación cíclica
                intercambios = ''.join(f'({"".join(map(str, ciclo))})' for ciclo in ciclos)
                
                for col, escalar in enumerate(escalares):
                    if escalar != 1:
                        operaciones.append(f"\nMultiplicación por un escalar: columna {col+1} multiplicada por {escalar}")
                if intercambios or operaciones:  # Si hay permutación o operaciones con escalares, imprimirlos.
                            if intercambios:
                                print("\nPermutación entre posiciones:", intercambios)
                            for operacion in operaciones:
                                print(operacion)
                            # Codewords
                            codewords_G1 = hallar_codewords(Generadora1, q, k)
                            print(f'C1={{{codewords_G1}}}')
                            codewords_G2 = hallar_codewords(Generadora2, q, k)
                            print(f'C2={{{codewords_G2}}}')
                            return es_equivalente        
            else:
                es_equivalente= False # Para cuestiones de validación
    return es_equivalente  # PARA VALIDACIÓN: Retorna False si no se encontró ninguna permutación que haga equivalentes las matrices



# Programa principal - Pide los datos y llama a las funciones necesarias.
print("Bienvenidx")
print("Porfavor ingrese los siguientes parametros para la matriz generadora G1 y G2")
n = int(input("->Digite la longitud del código (n): "))
k = int(input("->Digite la dimensión del codigo (k): "))
q = int(input("->Digite la cardinalidad del alfabeto (q): "))
G1 = []
G2 =[]
print("\nIngrese la Matriz Generadora G1")
Generadora1 = MatrizGeneradora(G1, n, k, q)
print("\nMatriz G1:")
print(Generadora1)
print("\nIngrese la Matriz Generadora G2")
Generadora2 = MatrizGeneradora(G2, n, k, q)
print("\nMatriz G2:")
print(Generadora2)
if permutaciones(Generadora1, Generadora2,q):
    print()
    print("\n Las matrices generadoras no pertenecen a codigos equivalentes. Por favor, intente de nuevo")
