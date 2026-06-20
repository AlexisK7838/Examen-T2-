lab = [
["F",1,1,1,0,1,1,1,1],
[-2,0,0,-1,0,1,0,1,0],
[1,1,0,1,1,1,0,1,0],
[0,1,0,-1,0,0,0,-1,0],
[1,1,1,1,1,1,1,1,0],
[-1,0,0,0,0,0,0,1,1],
[1,1,1,1,-1,1,1,1,0],
[1,0,0,1,0,1,0,1,0],
["I",1,-1,1,1,1,0,1,1]
]

camino = []

def buscar(f,c,vidas):

    if f < 0 or f > 8 or c < 0 or c > 8:
        return False

    if lab[f][c] == 0:
        return False

    if (f,c) in camino:
        return False

    valor = lab[f][c]

    if valor == -1:
        vidas -= 1
    elif valor == -2:
        vidas -= 2

    if vidas <= 0:
        return False

    camino.append((f,c))

    if f == 0 and c == 0:
        return True

    if (buscar(f-1,c,vidas) or
        buscar(f,c+1,vidas) or
        buscar(f+1,c,vidas) or
        buscar(f,c-1,vidas)):
        return True

    camino.pop()
    return False

if buscar(8,0,3):

    print("SALIDA ENCONTRADA\n")

    for i,p in enumerate(camino,1):
        print("Paso",i,"->",p)

    print("\nTotal de pasos:",len(camino))

else:
    print("No existe salida")