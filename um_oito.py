
'''   matriz = [[x[0], x[1], x[2]], [y[0], y[1], y[2]], [z[1], z[2], z[3]]]   '''
'''
matriz = [[],[],[]]
for i in range(3):
    x = int(input("digite : "))
    matriz[0].append(x)

for i in range(3):
    x = int(input("digite : "))
    matriz[1].append(x)
    
for i in range(3):
    x = int(input("digite : "))
    matriz[2].append(x)
'''

matriz_teste = [[3, 4, 7], [5, 8, 6], [2, 1, 0]]

def encontrar_indice_zero(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                return i,j

testes_matriz = []
testes_matriz.append(matriz_teste)

def movimento_possivel(x, y):
    ''' 0 = esquerda || 1 = direita || 2 = cima || 3 = baixo '''
    if x == 0:
        if y == 0:
            return [x, y+1, 'direita'], [x+1, y, 'baixo']
        elif y == 1:
           return [x , y-1, 'esquerda'], [x, y+1, 'direita'], [x+1, y, 'baixo'] 
        elif y == 2:
            return [x , y-1, 'esquerda'], [x+1, y, 'baixo']
    elif x == 1:
        if y == 0:
            return [x, y+1, 'direita'], [x-1, y, 'cima'], [x+1, y, 'baixo']
        elif y == 1:
           return [x , y-1, 'esquerda'], [x, y+1, 'direita'], [x-1, y, 'cima'] ,[x+1, y, 'baixo'] 
        elif y == 2:
            return [x , y-1, 'esquerda'], [x-1, y, 'cima'] ,[x+1, y, 'baixo']
    elif x ==2 :
        if y == 0:
            return [x, y+1, 'direita'], [x-1, y, 'cima']
        elif y == 1:
           return [x , y-1, 'esquerda'], [x, y+1, 'direita'], [x-1, y, 'cima']
        elif y == 2:
            return [x , y-1, 'esquerda'], [x-1, y, 'cima']



def criar_estado(matriz):
    return movimento_possivel(encontrar_indice_zero(matriz)[0], encontrar_indice_zero(matriz)[1])



def mover(matriz, x, y):
    zero = encontrar_indice_zero(matriz)
    value = matriz[x][y]
    
    matriz[zero[0]].pop(zero[1])
    matriz[x].pop(y)
    
    matriz[x].insert(y, 0)
    matriz[zero[0]].insert(zero[1], value)
    testes_matriz.append(matriz)
    return matriz
'''
print('',matriz_teste[0],'\n',matriz_teste[1],'\n',matriz_teste[2],'\n')
mover(matriz_teste, criar_estado(matriz_teste)[0][0], criar_estado(matriz_teste)[0][1])

print('',matriz_teste[0],'\n',matriz_teste[1],'\n',matriz_teste[2],'\n')'''



'''for i in range(len(criar_estado(matriz_teste))):
    x = len(testes_matriz)-1
    print(testes_matriz[i])
    mover(testes_matriz[x], criar_estado(testes_matriz[x])[i][0], criar_estado(testes_matriz[x])[i][1])

'''
x = len(testes_matriz)-1
mover(testes_matriz[x], criar_estado(testes_matriz[x])[0][0], criar_estado(testes_matriz[x])[0][1])
print(testes_matriz)







            

        
'''
    0 1 2
0 [ 1 2 3 ] m[0][012]
1 [ 4 6 7 ] m[1][012]
2 [ 5 8 0 ] m[2][012]

'''