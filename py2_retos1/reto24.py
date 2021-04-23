def palindromo(p):
  size=int((len(p))/2)
  condicion=True
  for i in range(0,size,):
    if p[i]!=p[-1-i]:
      condicion=False
  return condicion

palabra=input('ingrese una palabra: ').lower()
if palindromo(palabra)==True:
  print(palabra,'es un palíndromo')
else: 
    print(palabra,'no es un palíndromo')