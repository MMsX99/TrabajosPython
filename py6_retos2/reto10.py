#Calcular cuantos granos de trigo tendríamos que utilizar si por cada casilla de un tablero de ajedrez pusiéramos un grano en la primera casilla, dos en la segunda, cuatro en la tercera, y así doblando hasta la última.
print('Calcular cuantos granos de trigo tendríamos que utilizar si por cada casilla de un tablero de ajedrez pusiéramos un grano en la primera casilla, dos en la segunda, cuatro en la tercera, y así doblando hasta la última.')
granos=0
#lista=[]
for i in range(0,64):
  granos=granos+(2**i)
  #lista.append(2**i)
#print(lista)
print('el resultado es: ', granos)
