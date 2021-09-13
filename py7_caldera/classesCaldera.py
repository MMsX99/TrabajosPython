import tkinter as Tk
from tkinter.font import BOLD
import math
import time

class Tanque:

    def __init__(self, name, capacidad, contenido, x0, y0, x1, y1,canvaslocal):
        self.capacidad = capacidad
        self.contenido = contenido
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.canvaslocal=canvaslocal
        alto = y1 - y0
        ancho = x1 - x0
        altura_liquido = int(alto * self.contenido /self.capacidad)
        self.name=name
        self.nivel_liquido=y1-altura_liquido
        self.rectangulo_capacidad=canvaslocal.create_rectangle(
            x0,
            y0,
            x1,
            y1,
            fill='black',
            #outline='green',
        )
        self.rectangulo_contenido= canvaslocal.create_rectangle(
            x0+3,
            y1-altura_liquido,
            x1-3,
            y1-2,
            fill='lightblue',
            #outline='green',
        )
        self.text_tanque=canvaslocal.create_text(x0+ancho/2, y0+alto/2, anchor=Tk.CENTER, text=name, font=('courier',20,BOLD), fill='red',justify='center')

    def actualizar_dibujo(self):
        canvaslocal=self.canvaslocal
        capacidad = self.capacidad
        contenido = self.contenido
        x0 = self.x0
        y1 = self.y1
        x1 = self.x1
        y0 = self.y0
        alto = y1 - y0
        altura_liquido = int(alto * contenido / capacidad)
        self.nivel_liquido=y1-altura_liquido

        canvaslocal.coords(self.rectangulo_contenido,x0+3,y1-altura_liquido,x1-3,y1-2)
        
    def adicionar(self, cantidad):
            self.contenido += cantidad
            if(self.contenido<0):
                self.contenido=0
            if(self.contenido>self.capacidad):
                self.contenido=self.capacidad
            self.actualizar_dibujo()

    def sustraer(self, cantidad):
        self.adicionar(-cantidad)

    def sustraer10(self):
        self.sustraer(10)

    def adicionar10(self):
        self.adicionar(10)
    
    def set_name(self, valor):
        self.name= valor


class Caldera(Tanque):
    def __init__(self, estado, capacidad, contenido, x0, y0, x1, y1,temperatura,canvaslocal):
        super().__init__(estado, capacidad, contenido, x0, y0, x1, y1,canvaslocal)
        self.temp_caldera=temperatura
        self.temp_inicio=temperatura
        self.start_time=time.time()
        self.estado=estado
        self.alto = y1 - y0
        self.ancho = x1 - x0
        self.fill_capacidad='black'
        if(self.estado=="C\nencendida"):
            self.fill_capacidad='darkred'
        self.altura_liquido = int(self.alto * self.contenido /self.capacidad)
        self.nivel_liquido=y1-self.altura_liquido
        
        self.rectangulo_capacidad=canvaslocal.create_rectangle(
            x0,
            y0,
            x1,
            y1,
            fill=self.fill_capacidad,
            #outline='green',
        )
        self.rectangulo_contenido= canvaslocal.create_rectangle(
            x0+3,
            y1-self.altura_liquido,
            x1-3,
            y1-2,
            fill='lightblue',
            #outline='green',
        )
        self.fill_text='red'
        if(self.estado=='C\nencendida'):
            self.fill_text='yellow'
        self.text_tanque=canvaslocal.create_text(x0+self.ancho/2, y0+self.alto/2, anchor=Tk.CENTER, text=estado, font=('courier',20,BOLD), fill=self.fill_text,justify='center')

    def actualizar_dibujo(self):
        canvaslocal=self.canvaslocal
        capacidad = self.capacidad
        contenido = self.contenido
        estado=self.estado
        x0 = self.x0
        y1 = self.y1
        x1 = self.x1
        y0 = self.y0
        alto = y1 - y0
        altura_liquido = int(alto * contenido / capacidad)
        
        self.nivel_liquido=y1-altura_liquido
        
        if(estado=='C\nencendida'):
            self.fill_capacidad='darkred'
            self.fill_text='yellow'
        else: 
            self.fill_capacidad='black'
            self.fill_text='red'
        fill_capacidad=self.fill_capacidad
        fill_text=self.fill_text
        
        canvaslocal.itemconfig(self.rectangulo_capacidad,{"fill":fill_capacidad})
        canvaslocal.coords(self.rectangulo_contenido, x0+3,y1-altura_liquido,x1-3,y1-2)
        canvaslocal.itemconfig(self.text_tanque,{"text":estado})
        canvaslocal.itemconfig(self.text_tanque, {"fill":fill_text})
        
    def calcular_temp(self, tiempo_real):   
        tiempo_ecuacion=tiempo_real-self.start_time
        temp_inicio=self.temp_inicio
        temp_caldera=self.temp_caldera
        
        if(self.estado=="C\napagada"):
            temp_caldera=30+(temp_inicio-30)*((math.e)**(-tiempo_ecuacion*0.0025))
        else:
            temp_caldera=92+(temp_inicio-92)*((math.e)**(-tiempo_ecuacion*0.25))
        self.temp_caldera=temp_caldera
        


class Sensor_temperatura:
    def __init__(self, temperatura, estado_caldera, x0, y0, ampX, ampY,canvaslocal):
        self.temperatura=temperatura
        self.estado_caldera=estado_caldera
        self.x0=x0
        self.y0=y0
        self.ampX=ampX
        self.ampY=ampY
        self.canvaslocal=canvaslocal
        
        posX=self.x0
        posY=self.y0
        amplitudX=posX+self.ampX
        amplitudY=self.ampY
        self.cajaST=canvaslocal.create_rectangle(posX, posY, amplitudX, posY+(amplitudY), fill='black')

        posCajaST=canvaslocal.coords(self.cajaST)
        cajaT_x1=posX+((posCajaST[2]-posX)*2/3)
        cajaT_y1=posCajaST[3]-5
        self.cajaT=canvaslocal.create_rectangle(posX+5, posY+5, cajaT_x1, cajaT_y1, fill='darkred')
        posCajaT=canvaslocal.coords(self.cajaT)
        cajaT_registro_x=posCajaT[0]+3
        cajaT_registro_y=posCajaT[1]+((posCajaT[3]-posCajaT[1])/2)
        self.cajaT_registro=canvaslocal.create_text(cajaT_registro_x,cajaT_registro_y, anchor=Tk.W, text='{}°C'.format(int(temperatura)), fill='yellow', font=('courier',14))

        cajaT_texto_x=(posCajaST[2])-5
        cajaT_texto_y=cajaT_registro_y
        self.cajaT_texto=canvaslocal.create_text(cajaT_texto_x, cajaT_texto_y, anchor=Tk.E, text='T', fill='white', font=('courier',14))
    
    def actualizar_dibujo(self):
        temperatura=self.temperatura
        canvaslocal=self.canvaslocal
    
        canvaslocal.itemconfig(self.cajaT_registro,{"text":'{}°C'.format(int(temperatura))})
class Sensor_nivel:
    def __init__(self,nombre,nivel_sensor,nivel_liquido,x0,y0,ampX,ampY,canvaslocal):
        
        self.nombre=nombre
        self.nivel_sensor=nivel_sensor
        self.nivel_liquido=nivel_liquido
        self.x0=x0
        self.y0=y0
        self.ampX=ampX
        self.ampY=ampY
        self.canvaslocal=canvaslocal
        
        posXSN1=self.x0
        posYSN1=self.y0
        amplitudX=self.ampX
        amplitudY=self.ampY
        self.cajaSN1=canvaslocal.create_rectangle(posXSN1,posYSN1,posXSN1+(amplitudX),posYSN1+(amplitudY) ,fill='black')
        posCajaSN1=canvaslocal.coords(self.cajaSN1)
        posX1LEDSN1=float(posXSN1+(((posCajaSN1[2])-posXSN1)/3))
        posY1LEDSN1=(posCajaSN1[3])-5
        magnitudCirculoY=posY1LEDSN1-(posYSN1+5)

        self.ledSN1=canvaslocal.create_oval(posXSN1+5,posYSN1+5-3, posXSN1+5+6+magnitudCirculoY,posY1LEDSN1+3, fill="black", outline='red')
        if(nivel_liquido >= nivel_sensor):
            self.ledSN1=canvaslocal.create_oval(posXSN1+5,posYSN1+5-3, posXSN1+5+6+magnitudCirculoY,posY1LEDSN1+3, fill="black", outline='red')

        posLEDSN1=canvaslocal.coords(self.ledSN1)
        posXTextoSN1=(posCajaSN1[2]-3)
        posYTextoSN1=posCajaSN1[1]+((posCajaSN1[3]-posCajaSN1[1])/2)
        self.textoSN1=canvaslocal.create_text(posXTextoSN1,posYTextoSN1, anchor=Tk.E, text='Snivel{}'.format(nombre), fill='white', font=('courier',12))
    
    
    def actualizar_dibujo(self):
        canvaslocal=self.canvaslocal
        nivel_sensor=self.nivel_sensor
        nivel_liquido=self.nivel_liquido

        if(nivel_liquido >= nivel_sensor):
            canvaslocal.itemconfig(self.ledSN1,{"fill":'black'})
        else: 
            canvaslocal.itemconfig(self.ledSN1,{"fill":'red'})

    def actualizar_sensor(self, nivel_liquido):
        self.nivel_liquido=nivel_liquido
        self.actualizar_dibujo()


class Temporizador:
    def __init__(self,x0,y0,x1,y1,canvaslocal):
        self.timpoActual=0
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.tiempo_cero=time.time()
        self.timer=time.time()
        self.canvaslocal=canvaslocal
       
        posX=x0
        posY=y0
        amplitudX=x1
        amplitudY=y1
        self.cajaStime=canvaslocal.create_rectangle(posX, posY, x1, y1, fill='darkblue')
        posCajaStime=canvaslocal.coords(self.cajaStime)
        cajaTime_x1=posX+((posCajaStime[2]-posX)*2/3)
        cajaTime_y1=posCajaStime[3]-5

        self.cajaTime=canvaslocal.create_rectangle(posX+5, posY+5, cajaTime_x1, cajaTime_y1, fill='black')
        posCajaTime=canvaslocal.coords(self.cajaTime)
        cajaTime_registro_x=posCajaTime[0]+3
        cajaTime_registro_y=posCajaTime[1]+((posCajaTime[3]-posCajaTime[1])/2)

        self.cajaTime_registro=canvaslocal.create_text(cajaTime_registro_x,cajaTime_registro_y, anchor=Tk.W, text="{} sg".format(int(self.timer)), fill='yellow', font=('courier',14))
        cajaTime_texto_x=(posCajaStime[2])-5
        cajaTime_texto_y=cajaTime_registro_y
        self.cajaTime_texto=canvaslocal.create_text(cajaTime_texto_x, cajaTime_texto_y, anchor=Tk.E, text='Temp', fill='white', font=('courier',14))
    
    def actualizar_dibujo(self):
        canvaslocal=self.canvaslocal        
        timer=self.timer
        canvaslocal.itemconfig(self.cajaTime_registro, {"text":"{} sg".format(int(timer))})

class Valvula:
    def __init__(self,x_texto,y_texto,canvaslocal,estado,p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25):
        
        self.canvaslocal=canvaslocal
        self.estado=estado
        if(estado=='abierta'):
            self.ecV1_estate=canvaslocal.create_text(x_texto, y_texto, anchor=Tk.W, text='(ON)', font=('courier',18,BOLD), fill='red')
            self.figura1=canvaslocal.create_line(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,fill='lightblue',width=4)
            self.figura2=canvaslocal.create_line(p18,p19,p20,p21,p22,p23,p24,p25,fill="lightblue",width=4)
        else:
            self.ecV1_estate=canvaslocal.create_text(x_texto, y_texto, anchor=Tk.W, text='(OFF)', font=('courier',18,BOLD), fill='red')
            self.figura1=canvaslocal.create_line(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,fill='black',width=4)
            self.figura2=canvaslocal.create_line(p18,p19,p20,p21,p22,p23,p24,p25,fill="black",width=4)
        
    def actualizar_dibujo(self):
        canvaslocal=self.canvaslocal
        estado=self.estado
        if(estado=='abierta'):
            canvaslocal.itemconfig(self.ecV1_estate, {"text":'(ON)'})
            canvaslocal.itemconfig(self.figura1, {"fill":"lightblue"})
            canvaslocal.itemconfig(self.figura2, {"fill":"lightblue"})
        else:
            canvaslocal.itemconfig(self.ecV1_estate, {"text":'(OFF)'})
            canvaslocal.itemconfig(self.figura1, {"fill":"black"})
            canvaslocal.itemconfig(self.figura2, {"fill":"black"})




class Controlador:
    #estado 0, se requerien condiciones diferentes, salir del procesoQ
    #estado1-1, inicializar variables,verificar contenido en t1 y t2, x=0 ir a estado 0(final),
    #                                                                   X=1 ir a estado 1-2
    #estado1-2, retirar contenido en caldera y t3 (x=0 ir a mismo estado 1-2 ,
    #                                               X=1 se retiro contenido ir a estado 2-1) 
    #estado2-1, abrir t1 para llenar tanque hasta N1 (x=0 ir a mismo estado 2-1,
    #                                                  x=1 se lleno nivel 1 ir a estado 2-2
    # estado2-2, calentar por 5 segundos, (x=0 repetir estado 2-2 
    #                                      x=1 se llego a 5 segundos, ir a estado 2-3
    #estado 2-3, condicional, x=1 si la temperatura es mayor a 80 ir a estado 3 
    #                         X=0 si la temperatura es menor a 80 ir a estado 4  
    #estado 4 agregar producto de t2 hasta llegar al nivel 2(x=0 no se ha llenado ir a estado 4,
    #                                                        x=1 se lleno ir a estado 5)
    #estado 5 dejar calentar hasta que llegue a los 80 grados(x=0 temperatura no alcanzada ir a estado 5, 
    #                                                          x=1 ir a estado 3)
    #estado 3-1:vertir producto en T3(x=0 no se ha vertido completament ir a estado 3-1
    #                                x=1 finalizar proceso
    
    
    def __init__(self):
        self.estado0=0
        self.estado1_1=11
        self.estado1_2=12
        self.estado2_1=21
        self.estado2_2=22
        self.estado2_3=23
        self.estado3_1=31
        self.estado4=4
        self.estado5=5
        
        self.estado_controlador=False
        self.estado_actual=11
        self.entrada=0
        self.salida=0
        self.tiempoprueba=0
        self.tempGlobal=0


    def apagar_caldera(self,c,sensorT,label_boton_caldera):
       if(c.estado=="C\nencendida"):
            c.estado="C\napagada"
            label_boton_caldera.config(text='Caldera: apagada')
            c.temp_inicio=c.temp_caldera
            c.start_time=time.time()
            c.actualizar_dibujo()
            sensorT.actualizar_dibujo()
    def encender_caldera(self,c,sensorT,label_boton_caldera):
        if(c.estado=="C\napagada"):
            c.estado="C\nencendida"
            label_boton_caldera.config(text='Caldera: encendida')
            c.temp_inicio=c.temp_caldera
            c.start_time=time.time()
            c.actualizar_dibujo()
            sensorT.actualizar_dibujo()
        

    def cerrar_v1(self,canvaslocal,v1,label_boton_V1,label_boton_V1_string):
        if(v1.estado=='abierta'):
            v1.estado='cerrada'
            label_boton_V1_string.set('valvula1: cerrada')
            label_boton_V1.config(text=label_boton_V1_string.get())
        v1.actualizar_dibujo()
    def cerrar_v2(self,canvaslocal,v2,label_boton_V2):
        if(v2.estado=='abierta'):
            v2.estado='cerrada'
            label_boton_V2.config(text='valvula 2: cerrada')
            v2.actualizar_dibujo()
    def cerrar_v3(self,canvaslocal,v3,label_boton_V3):
        if(v3.estado=='abierta'):
            v3.estado='cerrada'
            label_boton_V3.config(text='valvula 3: cerrada')
            v3.actualizar_dibujo()

    def abrir_v1(self,canvaslocal,v1,label_boton_V1,label_boton_V1_string):
        if(v1.estado=='cerrada'):
            v1.estado='abierta'
            label_boton_V1_string.set('valvula 1: abierta')
            label_boton_V1.config(text=label_boton_V1_string.get())
            v1.actualizar_dibujo()
    def abrir_v2(self,canvaslocal,v2,label_boton_V2,):
        if(v2.estado=='cerrada'):
            v2.estado='abierta'
            label_boton_V2.config(text='valvula 2: abierta')
            v2.actualizar_dibujo()
    def abrir_v3(self,canvaslocal,v3,label_boton_V3):
        if(v3.estado=='cerrada'):
            v3.estado='abierta'
            label_boton_V3.config(text='valvula 3: abierta')
            v3.actualizar_dibujo()
    def vaciar_t3(self,t3,ventana):
        if(t3.contenido!=0):
            t3.sustraer10()
            ventana.after(500, self.vaciar_t3(t3,ventana))

#####################
####################
    def estado1_1p(self,canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana):
        entradalocal=self.entrada
        print('Controlador activado.')
        if(t1.contenido<t1.capacidad/2):   
            
            entradalocal=0
            self.estado_actual=self.estado0
            return entradalocal
        elif(t2.contenido< t2.capacidad*43/100):
                
                entradalocal=1
                self.estado_actual=self.estado0
                return entradalocal
        else:
            self.cerrar_v1(canvaslocal,v1,label_boton_V1,label_boton_V1_string)
            self.cerrar_v2(canvaslocal,v2,label_boton_V2)
            self.cerrar_v3(canvaslocal,v3,label_boton_V3)
        
            self.apagar_caldera(c,sensorT,label_boton_caldera)        
            el_temporizador.tiempo_cero=time.time()
            el_temporizador.actualizar_dibujo()
            entradalocal=1
            self.estado_actual=self.estado1_2
            
            return entradalocal
    
    def estado1_2p(self,canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana):
        entradalocal=self.entrada
        if(entradalocal==1):
            print('vaciando tanque T3 y la caldera para iniciar proceso...')
            self.abrir_v3(canvaslocal,v3,label_boton_V3)

        entradalocal=0
        t3.sustraer10()
        if(c.contenido==0 and t3.contenido==0):
            print('Tanque 3 y caldera vacios.')
            self.cerrar_v3(canvaslocal,v3,label_boton_V3)
            entradalocal=1
            self.estado_actual=self.estado2_1
            return entradalocal
        else:
            return entradalocal

    def estado2_1p(self,canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana):
        entradalocal=self.entrada
        if(entradalocal==1):
            print('El proceso ha comenzado.')
            print('vertiendo producto de T1 hasta llenar nivel 1...')
            self.abrir_v1(canvaslocal,v1,label_boton_V1,label_boton_V1_string)
        entradalocal=0
        if(SN1.nivel_liquido<SN1.nivel_sensor):
            print('Nivel 1 alcanzado.')
            self.cerrar_v1(canvaslocal,v1,label_boton_V1,label_boton_V1_string)
            entradalocal=1
            self.estado_actual=self.estado2_2
            return entradalocal
        else:
            return entradalocal
    
    def estado2_2p(self,canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana):
        entradalocal=self.entrada
        if(entradalocal==1):
            print('Calentando producto por 5 segundos...')
            self.encender_caldera(c,sensorT,label_boton_caldera)
            self.tiempoprueba=time.time()
        entradalocal=0
        tiempoTranscurrido=time.time()
        tiempoTranscurrido=tiempoTranscurrido-self.tiempoprueba
        if(tiempoTranscurrido >= 5):
            print('Producto calentado.')
            self.apagar_caldera(c,sensorT,label_boton_caldera)
            entradalocal=1
            self.estado_actual=self.estado2_3
            return entradalocal
        else:
            return entradalocal

    def estado2_3p(self,canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana):
        entradalocal=self.entrada
        if(sensorT.temperatura>=80):
                print('La temperatura supero los 80 grados, producto terminado satisfactoriamente.')
                self.estado_actual=self.estado3_1
                return entradalocal
        else:
                print('La temperatura NO supero los 80 grados, se vertira producto de tanque T2 hasta llenar nivel 2.')
                self.estado_actual=self.estado4
                return entradalocal

    def estado3_1p(self,canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana):
        entradalocal=self.entrada
        if(entradalocal==1):
            print("Vertiendo producto terminado en tanque T3...")
            self.abrir_v3(canvaslocal,v3,label_boton_V3)
        entradalocal=0
        if(c.contenido==0):
            print("Producto almacenado en tanque T3.")
            print("Proceso controlaado terminado.")
            self.cerrar_v3(canvaslocal,v3,label_boton_V3)
            
            print('controlador desactivado.')
            self.estado_controlador=False
            entradalocal=0
            self.estado_actual=11
            return entradalocal

        else:
            return entradalocal

    def estado4p(self,canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana):
        entradalocal=self.entrada
        #1
        if(entradalocal==1):
            print("Vertiendo producto de tanque T2 hasta llenar Nivel 2... ")
            self.abrir_v2(canvaslocal,v2,label_boton_V2)
        
        entradalocal=0
        if(SN2.nivel_liquido < SN2.nivel_sensor):
            print("Nivel 2 alcanzado.")
            self.cerrar_v2(canvaslocal,v2,label_boton_V2)
            entradalocal=1
            self.estado_actual=self.estado5
            return entradalocal
        else:
            return entradalocal

    def estado5p(self,canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana):
        entradalocal=self.entrada
        if(entradalocal==1):
            print("calentando producto hasta alcanzar los 80 grados...")
            self.encender_caldera(c,sensorT,label_boton_caldera)
        entradalocal=0
        if(sensorT.temperatura >= 80):
            print("la temperatura alcanzo los 80 grados, producto terminado satisfactoriamente.")
            self.apagar_caldera(c,sensorT,label_boton_caldera)
            entradalocal=1
            self.estado_actual=self.estado3_1
            return entradalocal
        else:
            return entradalocal
      
    def estado0p(self,canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana):  
        entradalocal=self.entrada
        print('controlador desactivado.')
        if(entradalocal==0):
            print("No hay suficiente producto en T1 empezar el proceso(almenos 50%).")
        else:
            print('No hay suficiente producto en T2 para realizar el proceso(almenos 43%).')
        self.estado_controlador=False
        entradalocal=0
        self.estado_actual=11
        return entradalocal

    def proceso_control(self,canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana):

        if(self.estado_actual==0):
            self.entrada=self.estado0p(canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana)
        elif(self.estado_actual==11):
            self.entrada=self.estado1_1p(canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana)
        elif(self.estado_actual==12):
            self.entrada=self.estado1_2p(canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana)
        elif(self.estado_actual==21):
            self.entrada=self.estado2_1p(canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana)
        elif(self.estado_actual==22):
            self.entrada=self.estado2_2p(canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana)
        elif(self.estado_actual==23):
            self.entrada=self.estado2_3p(canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana)
        elif(self.estado_actual==31):
            self.entrada=self.estado3_1p(canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana)
        elif(self.estado_actual==4):
            self.entrada=self.estado4p(canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana)
        elif(self.estado_actual==5):
            self.entrada=self.estado5p(canvaslocal,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,sensorT,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,ventana)
        

    def ejecutar_proceso(self,canvaslocal,entradaE,t1E,t2E,t3E,SN1E,SN2E,SN3E,v1E,v2E,v3E,cE,sensorTE,el_temporizadorE,salidaE,label_boton_calderaE,label_boton_V1E,label_boton_V2E,label_boton_V3E,label_boton_V1_stringE,ventanaE):

        self.proceso_control(canvaslocal,entradaE,t1E,t2E,t3E,SN1E,SN2E,SN3E,v1E,v2E,v3E,cE,sensorTE,el_temporizadorE,salidaE,label_boton_calderaE,label_boton_V1E,label_boton_V2E,label_boton_V3E,label_boton_V1_stringE,ventanaE)
        if(self.estado_controlador==True):
            ventanaE.after(500, self.ejecutar_proceso(canvaslocal,entradaE,t1E,t2E,t3E,SN1E,SN2E,SN3E,v1E,v2E,v3E,cE,sensorTE,el_temporizadorE,salidaE,label_boton_calderaE,label_boton_V1E,label_boton_V2E,label_boton_V3E,label_boton_V1_stringE,ventanaE))
        

            