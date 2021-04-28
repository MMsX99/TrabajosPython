import random
def sumatoria(a,b):
  nc=int(len(a)//2)
  C=[]
  res=0
  for i in range(0,nc):
    res=(((a[i+1])**2)*b[2*i])+b[nc+i]
    C.append(res)
  return C

N=int(input('ingrese el numero de elementos de la lista C: '))
A=[]
B=[]
for i in range(0,N*2):
  A.append(random.randint(1,9))
for i in range(0,N*2):
  B.append(random.randint(1,9))
print('listas:')
print('A=',A)
print('B=',B)
print('resultado, lista c:',sumatoria(A,B))
