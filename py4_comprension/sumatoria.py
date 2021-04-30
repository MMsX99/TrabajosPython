import random
N=random.randint(1,5)
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

sumatoria=sum(((A[i]*B[i])+C[i] for i in range(N)))+N**2
print('resultado sumatoria: ',sumatoria)