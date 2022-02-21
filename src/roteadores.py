import heapq
import random

# ler numero de vertices e arestas
n, m = input().split()
n = int(n)
m = int(m)

# inicializando o heap como uma lista vazia
H = []
# criando n listas vazias de vizinhos para cada nó 0 -> n-1
n_out = [[]*n for i in range(m)]

# ler as m arestas do grafo
for j in range(m):
    # ler aresta de a para b com custo
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    # acrescentando o b na lista de vizinhos do a
    n_out[a].append((b, c))
    # acrescentando o a na lista de vizinhos do b
    n_out[b].append((a, c))

# escolhenddo uma raiz aleatoria qualquer entre 0 e n-1
raiz = random.randint(0, n-1)

# iniciando o heap com as candidatas, pegando todas as arestas que partem do nó raiz
for (x, c) in n_out[raiz]:
    # inserindo no H uma aresta de custo c que vai de raiz até x
    heapq.heappush(H, (c, raiz, x))

marcados = [raiz]  # lista de nós marcados
arv_ger_min = []  # arvore geradora minima inicializada vazia
n_aresta = 0  # número de arestas 0 inicialmente
custo = 0  # custo 0 por enquanto

# verificando as n_arestas que foram marcadas
while n_aresta < n-1:
    while True:
        (c, a, b) = heapq.heappop(H)
        # se b não tiver marcado para,
        # se b tiver marcado vai para próxima aresta com custo mínimo
        if b not in marcados:
            break
    marcados.append(b)
    print(a, b) # imprimindo as arestas
    print(marcados) # imprimindo os marcados até o momento
    custo += c
    arv_ger_min.append((a, b))
    n_aresta += 1

    # pega os vizinhos de b que não estejam marcados ainda
    for (x, c) in n_out[b]:
        if x not in marcados:
            heapq.heappush(H, (c, b, x))

print("\n")
print("Custo Total:", custo)
print("Árvore Geradora Mínima:", arv_ger_min)
