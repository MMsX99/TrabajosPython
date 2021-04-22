def calcMasaCorporal(p,a):
  alturametros=float(a/100)
  masacorporal=float(p/(alturametros**2))
  return masacorporal
print('calculo de masa corporal[Body mass index].')
peso=float(input('ingrese peso en kilogramos: '))
altura=float(input('ingrese altura en centimetros: '))
print('masa corporal es: ',calcMasaCorporal(peso,altura),'[BMI]')