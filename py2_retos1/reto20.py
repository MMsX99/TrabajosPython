def bisiesto(a):
  if a%4 == 0:
    if a%100 == 0:
      if a%400 == 0:
        mensaje='el año es bisiesto'
      else: mensaje='el año no es bisiesto'
    else: mensaje='el año es bisiesto'
  else:mensaje='el año no es bisiesto'
  return mensaje
A=int(input('ingrese un año para saber si es bisiesto: '))
print(bisiesto(A))