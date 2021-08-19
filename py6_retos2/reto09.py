
lista=[]
vinicial=int(input('ingrese un valor inicial: '))
vfinal=int(input('ingrese un valor final: '))
vintervalo=int(input('ingrese el intervalo entre cada numero: '))
contador=0
for i in range(vinicial,vfinal+1,vintervalo):
  lista.append(i)
  contador=contador+i
print(lista)
print('la suma de los valores listados es: ', contador)
