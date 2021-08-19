import matplotlib.pyplot as plt
Lprueba=[]
print("programa que calcula una lista de números y luego grafica la lista utilizando matplotlib")
n=int(input("ingrese el primer numero de la lista: "))
while(n != 1):
  Lprueba.append(n)
  if(n%2 == 0):
    n=n/2
  else:
    n=(n*3)+1
Lprueba.append(n)    
plt.plot(Lprueba)
plt.show()
