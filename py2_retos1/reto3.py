a=int(input('ingrese un primer numero: '))
b=int(input('ingrese un segundo numero: '))
c=a+b
print('suma de los numeros: ',c)
c=a-b
print('resta de los numeros: ',a,'-',b,'=',c)
c=a*b
print('multiplicación de los numeros: ',c)
if b==0:
  print('no se puede dividir por cero')
else:
  c=a/b
  print('division de los numeros: ',a,'/',b,'=',c)
  c=a%b
  print('residuo de los numeros: ',a,'%',b,'=',c)