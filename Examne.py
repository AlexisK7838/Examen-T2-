import random
def contar_multiplos(matriz, inicio, fin):
    if inicio == fin:
        contador = 0
        for numero in matriz[inicio]:
            if numero % 5 == 0 or numero % 7 == 0:
                contador += 1
        return contador
    medio = (inicio + fin) // 2
    iz= contar_multiplos(matriz, inicio, medio)
    de = contar_multiplos(matriz, medio + 1, fin)
    return iz + de
n = int(input("Digite tamaño de matriz a elaborar : "))
matriz = []
while n < 1 or n > 11:
    print("TAMAÑO MAXIMO DE DATOS MATRIZ 11X11")
    n = int(input("INGRESE DENUEVO EL TAMAÑO DE MAXIMO ACEPTABLE "))
for i in range(n):
    fila = []
    for j in range(n): #la llenará con números aleatorios entre 99 y 999
        fila.append(random.randint(99, 999))
    matriz.append(fila)
print("\nMATRIZ:\n")
for fila in matriz:
    print(*fila)
resultado = contar_multiplos(matriz, 0, n - 1)
print("\nCantidad de múltiplos de 5 o 7:", resultado)