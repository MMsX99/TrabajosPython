import random
N=random.randrange(2,10,2)
A=[]
B=[]
for i in range(0,N):
  A.append(random.randint(1,9))
for i in range(0,N):
  B.append(random.randint(1,9))
print('listas:')
print('A=',A)
print('B=',B)
N=N//2
C=[(((A[i+1])**2)*B[2*i])+B[(N)+i] for i in range(N)]
print('lista C: ',C)