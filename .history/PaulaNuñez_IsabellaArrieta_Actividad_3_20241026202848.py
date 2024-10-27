
# Funcion MatrizGeneradora

def MatrizGeneradora(G1, n, k, q): #parametros de entrada: G1, n, k, q
    for i in range(int(k)): #itera sobre el rango de k que es el numero de filas
        codewords = [] #lista para almacenar los codewords
        codeword = input(f"Ingrese el codeword {i+1} de longitud {n}: ") #solicita el codeword
        #valida que el codeword tenga la longitud correcta y que pertenezca al q solicitado
        while len(codeword) != int(n) or not all(char in map(str, range(int(q))) for char in codeword): #mientras no cumpla con las condiciones
            if len(codeword) != int(n): #si la longitud no es la correcta
                print(f"El codeword debe tener una longitud de {n}. Inténtelo de nuevo.")
            elif not all(char in map(str, range(int(q))) for char in codeword): #si no pertenece al q solicitado
                print(f"El codeword debe contener solo caracteres en el rango 0 a {int(q)-1}. Inténtelo de nuevo.")
            codeword = input(f"Ingrese el codeword {i+1} de longitud {n}: ")#solicita nuevamente el codeword
        codewords.append(codeword)#agrega el codeword a la lista
        G1.append(codewords)#agrega la lista de codewords a la matriz generadora

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

print("Bienvenidx")
print("Porfavor ingrese los siguientes parametros para la matriz generadora G1 y G2")
n= input("\n ->Digite la longitud del código (n): ")
k= input(" ->Digite la dimensión del codigo (k): ")
q= input(" ->Digite la cardinalidad del alfabeto (q): ")
G1 =[] 
G2 =[] 
print("\n Ingrese la Matriz Generadora G1\n")
MatrizGeneradora(G1, n, k, q)
print(G1)
print("\n Ingrese la Matriz Generadora G2\n")
MatrizGeneradora(G2, n, k, q)
print(G2)