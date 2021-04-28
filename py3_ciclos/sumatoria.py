import random
def sumatoria(a,b,c):
  n=int(len(a))
  sum=0
  for i in range(0,n):
    sum=sum+(a[i]*b[i])+c[i]
  sum=sum+(n**2)
  return sum
  
N=int(input('ingrese el numero de elementos en cada lista: '))
A=[]
B=[]
C=[]
for i in range(0,N):
  A.append(random.randint(1,9))
for i in range(0,N):
  B.append(random.randint(1,9))
for i in range(0,N):
  C.append(random.randint(1,9))
print('listas:')
print('A=',A)
print('B=',B)
print('C=',C)
print('resultado sumatoria:',sumatoria(A,B,C))
print(sumatoria((2,4),(4,8),(3,5)))