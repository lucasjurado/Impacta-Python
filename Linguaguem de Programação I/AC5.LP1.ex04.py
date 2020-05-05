vlr = input().split()
N = int(vlr[0])
K = int(vlr[1])

lista = []
for i in range(N):
  nome = input()
  lista.append( nome )

lista.sort()

print(lista[K-1])