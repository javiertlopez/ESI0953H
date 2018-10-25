import numpy as np
#arreglo de listas
matriz_pegs = np.array([["Pegs"],["Red"],["white"],["Blue"]])
print(matriz_pegs)
pegs = input("ingresa la cantidad de pegs:")
matriz_pegs[0,0] = int(pegs) #pegs
matriz_pegs[1,0] = int(0) #red
matriz_pegs[2,0] = int(0) #white
matriz_pegs[3,0] = int(0) #blue
print(matriz_pegs)
distribucion = int(pegs)/3
distribucion_mid = int(distribucion)*(2)

i = 0
j = 1
while j != 0:
    if i <= distribucion:
         peg = i
         matriz_pegs[1,0] = peg 
         i += 1
    if i > distribucion and i <= distribucion_mid:
         peg = i-int(distribucion)
         matriz_pegs[2,0] = peg 
         i += 1
    print(i)
    if i > distribucion_mid:
         peg = i-int(distribucion_mid)
         matriz_pegs[3,0] = peg
         i += 1
    if i > int(pegs):
        matriz_pegs[0,0] = 0
        i = 0
        j = 0
   
print(matriz_pegs)
suma = int(matriz_pegs[1,0]) + int(matriz_pegs[2,0]) + int(matriz_pegs[3,0])

if int(suma) < int(pegs):
    print("Sobra:", int(pegs)-int(suma), "peg.")

