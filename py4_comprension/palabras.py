A=['palabra','palabras','ciclo','lista']
print('lista:',A)

n=len(A)
C=[A[i] for i in range(n) if (A[i][-1])=='a']
print('palabras que terminan en "a": ',C)