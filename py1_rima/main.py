print('programa para encontrar rimas en el archivo palabras500.csv')
archivo = open('palabras500.csv', encoding="utf-8")
lineas = archivo.readlines()
archivo.close()

def rimas(caracteres):
  tamaño = len(caracteres)
  contador=0

  for i in lineas:
    if i[-tamaño-1:-1] == caracteres:
      print(i)
      contador = contador+1
  return contador
  
cadena = input('escriba los caracteres de la rima: ')
print('--------------------------------------------------------')
c=rimas(cadena)
print('--------------------------------------------------------')
print('se encontraron',c,'palabras que riman.')