# UNIVERSIDADE DE VASSOURAS - MARICÁ
# PROFESSOR: MÁRCIO GARRIDO
# ESTUDANTES: FÁBIO LIMA, HYGOR RASEC, VICTOR BERNARDO
# 30/03/2023
# PROJETO 04

# Tendo em vista o conjunto de elementos abaixo, criar um algoritmo que seja capaz de determinar a posição de cada elemento e printar as de forma ascendente os valores, assim como printar separadamente posições atuais. N ofinal imprimir de forma gráfica a notação Big'O do seu resultado.

# // Entrada

# elementos = [[a,b,c,d],[q,i,n,m],[f,e,h,j],[p,o,l,g]]

# // Saída

# [a,b,c,d,e,f,g,h,i,j,l,m,n,o,p,q]
# [0:0,0:1,0:2,0:3,2:1,2:0,3:3,2:2,1:1,2:3,3:2,1:3,1:2,3:1,3:0,1:0]

import time
import matplotlib.pyplot as plt

def func_ordenar(elementos):
    valores = []
    posicao_dict = {}

    for i in range(len(elementos)):
        for j in range(len(elementos[i])):
            valores.append(elementos[i][j])
            posicao_dict[elementos[i][j]] = f'{i}:{j}'
    ordenando_dict = sorted(posicao_dict.items())
    lista_pra_dict = dict(ordenando_dict)
    valores_do_dict = lista_pra_dict.values()
    return list(valores_do_dict), valores

elementos = [['a','b','c','d'],['q','i','n','m'],['f','e','h','j'],['p','o','l','g']]

valores_final, valores = func_ordenar(elementos)

print(sorted(valores))
print(valores_final)

tamanho_matriz = []
tempo_execucao = []

for e in range(1, 101):
    
    start_for = time.perf_counter()
    
    valores = []
    posicao_dict = {}
    
    elementos = [['a','b','c','d'],['q','i','n','m'],['f','e','h','j'],['p','o','l','g']]
    elementos = elementos * e

    func_ordenar(elementos)

    end_for = time.perf_counter()

    microsegundos = (end_for-start_for) * 10**6
    
    tamanho_matriz.append(e)
    tempo_execucao.append(microsegundos)

plt.plot(tamanho_matriz, tempo_execucao, label="Função func_ordenar()")
plt.xlabel('Tamanho da matriz')
plt.ylabel('Tempo de execução (micro segundos)')
plt.legend()
plt.show()
