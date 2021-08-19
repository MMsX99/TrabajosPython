#numero aleatorio entre 1 y 120
import random
numero=random.randrange(1,121)
random.seed()
print('numero entre 1 y 121 es: ')
print(numero)

if numero<10:
  print('el numero es menor a 10')
else:
  if numero<=50:
    print('el numero esta entre 10 y 50')
  else:
    if numero<=100:
      print('el numero esta entre 50 y 100')
    else:
     print('el numero es mayor de 100')