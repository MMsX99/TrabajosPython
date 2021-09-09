import tkinter as Tk
from tkinter.font import BOLD
from tkinter import ttk
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

    def dibujo_tkinter(self):
        canvaslocal=self.canvaslocal
        capacidad = self.capacidad
        contenido = self.contenido
        x0 = self.x0
        y1 = self.y1
        x1 = self.x1
        y0 = self.y0
        alto = y1 - y0
        ancho = x1 - x0
        altura_liquido = int(alto * contenido / capacidad)
        name=self.name
        self.nivel_liquido=y1-altura_liquido
        self.rectangulo_capacidad=canvaslocal.create_rectangle(
            x0,
            y0,
            x1,
            y1,
            fill='black',
            #outline='green',
        )
        self.rectangulo_contenido=canvaslocal.create_rectangle(
            x0+3,
            y1-altura_liquido,
            x1-3,
            y1-2,
            fill='lightblue',
            #outline='green',
        )
        self.text_tanque=canvaslocal.create_text(x0+ancho/2, y0+alto/2, anchor=Tk.CENTER, text=name, font=('courier',20,BOLD), fill='red',justify='center')

    def adicionar(self, cantidad):
            self.contenido += cantidad
            if(self.contenido<0):
                self.contenido=0
            if(self.contenido>self.capacidad):
                self.contenido=self.capacidad
            self.dibujo_tkinter()

    def sustraer(self, cantidad):
        self.adicionar(-cantidad)

    def sustraer10(self):
        self.sustraer(10)

    def adicionar10(self):
        self.adicionar(10)
    
    
    def set_name(self, valor):
        self.name= valor


class Caldera(Tanque):
    def __init__(self, name, capacidad, contenido, x0, y0, x1, y1,temperatura,canvaslocal):
        super().__init__(name, capacidad, contenido, x0, y0, x1, y1,canvaslocal)
        self.temp_caldera=temperatura
        self.temp_inicio=temperatura
        self.start_time=time.time()
        
        alto = y1 - y0
        ancho = x1 - x0
        altura_liquido = int(alto * self.contenido /self.capacidad)
        self.name=name
        self.nivel_liquido=y1-altura_liquido
        self.fill_rect='black'
        self.rectangulo_capacidad=canvaslocal.create_rectangle(
            x0,
            y0,
            x1,
            y1,
            fill=self.fill_rect,
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
        self.fill_text='red'
        self.text_tanque=canvaslocal.create_text(x0+ancho/2, y0+alto/2, anchor=Tk.CENTER, text=name, font=('courier',20,BOLD), fill=self.fill_text,justify='center')

    def dibujo_tkinter(self):
        canvaslocal=self.canvaslocal
        capacidad = self.capacidad
        contenido = self.contenido
        x0 = self.x0
        y1 = self.y1
        x1 = self.x1
        y0 = self.y0
        alto = y1 - y0
        ancho = x1 - x0
        altura_liquido = int(alto * contenido / capacidad)
        name=self.name
        self.nivel_liquido=y1-altura_liquido
        self.rectangulo_capacidad=canvaslocal.create_rectangle(
            x0,
            y0,
            x1,
            y1,
            fill=self.fill_rect,
            #outline='green',
        )
        self.rectangulo_contenido=canvaslocal.create_rectangle(
            x0+3,
            y1-altura_liquido,
            x1-3,
            y1-2,
            fill='lightblue',
            #outline='green',
        )
        self.text_tanque=canvaslocal.create_text(x0+ancho/2, y0+alto/2, anchor=Tk.CENTER, text=name, font=('courier',20,BOLD), fill=self.fill_text,justify='center')


    def calcular_temp(self, tiempo_real):   
        

        tiempo_ecuacion=tiempo_real-self.start_time
        temp_inicio=self.temp_inicio
        temp_caldera=self.temp_caldera
        
        if(self.name=="C\napagada"):
            temp_caldera=30+(temp_inicio-30)*((math.e)**(-tiempo_ecuacion*0.2))
        else:
            temp_caldera=90+(temp_inicio-90)*((math.e)**(-tiempo_ecuacion*0.2))
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
    def dibujar(self):
        temperatura=self.temperatura
        canvaslocal=self.canvaslocal
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

        self.ledSN1=canvaslocal.create_oval(posXSN1+5,posYSN1+5-3, posXSN1+5+6+magnitudCirculoY,posY1LEDSN1+3, fill="red", outline='red')
        if(nivel_liquido >= nivel_sensor):
            self.ledSN1=canvaslocal.create_oval(posXSN1+5,posYSN1+5-3, posXSN1+5+6+magnitudCirculoY,posY1LEDSN1+3, fill="black", outline='red')

        posLEDSN1=canvaslocal.coords(self.ledSN1)
        posXTextoSN1=(posCajaSN1[2]-3)
        posYTextoSN1=posCajaSN1[1]+((posCajaSN1[3]-posCajaSN1[1])/2)
        self.textoSN1=canvaslocal.create_text(posXTextoSN1,posYTextoSN1, anchor=Tk.E, text='Snivel{}'.format(nombre), fill='white', font=('courier',12))
    
    
    def dibujar(self):
        canvaslocal=self.canvaslocal
        nombre=self.nombre
        nivel_sensor=self.nivel_sensor
        nivel_liquido=self.nivel_liquido
        posXSN1=self.x0
        posYSN1=self.y0
        amplitudX=self.ampX
        amplitudY=self.ampY
        self.cajaSN1=canvaslocal.create_rectangle(posXSN1,posYSN1,posXSN1+(amplitudX),posYSN1+(amplitudY) ,fill='black')
        posCajaSN1=canvaslocal.coords(self.cajaSN1)
        posX1LEDSN1=float(posXSN1+(((posCajaSN1[2])-posXSN1)/3))
        posY1LEDSN1=(posCajaSN1[3])-5
        magnitudCirculoY=posY1LEDSN1-(posYSN1+5)
        
        if(nivel_liquido < nivel_sensor):
            self.ledSN1=canvaslocal.create_oval(posXSN1+5,posYSN1+5-3, posXSN1+5+6+magnitudCirculoY,posY1LEDSN1+3, fill="red", outline='red')
        if(nivel_liquido >= nivel_sensor):
            self.ledSN1=canvaslocal.create_oval(posXSN1+5,posYSN1+5-3, posXSN1+5+6+magnitudCirculoY,posY1LEDSN1+3, fill="black", outline='red')
        
        posLEDSN1=canvaslocal.coords(self.ledSN1)
        posXTextoSN1=(posCajaSN1[2]-3)
        posYTextoSN1=posCajaSN1[1]+((posCajaSN1[3]-posCajaSN1[1])/2)
        self.textoSN1=canvaslocal.create_text(posXTextoSN1,posYTextoSN1, anchor=Tk.E, text='Snivel{}'.format(nombre), fill='white', font=('courier',12))
    
    def actualizar(self, nivel_liquido):
        self.nivel_liquido=nivel_liquido
        self.dibujar()


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
    
    def dibujar(self):
        canvaslocal=self.canvaslocal
        x0=self.x0
        y0=self.y0
        x1=self.x1
        y1=self.y1
        
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



def crearStime(pos_ST_X,pos_ST_Y, ampX, ampY, canvaslocal):
    posX=pos_ST_X
    posY=pos_ST_Y
    amplitudX=posX+ampX
    amplitudY=ampY
    cajaStime=canvaslocal.create_rectangle(posX, posY, amplitudX, posY+(amplitudY), fill='darkblue')

    posCajaStime=canvaslocal.coords(cajaStime)
    cajaTime_x1=posX+((posCajaStime[2]-posX)*2/3)
    cajaTime_y1=posCajaStime[3]-5
    cajaTime=canvaslocal.create_rectangle(posX+5, posY+5, cajaTime_x1, cajaTime_y1, fill='black')
    posCajaTime=canvaslocal.coords(cajaTime)
    cajaTime_registro_x=posCajaTime[0]+3
    cajaTime_registro_y=posCajaTime[1]+((posCajaTime[3]-posCajaTime[1])/2)
    cajaTime_registro=canvaslocal.create_text(cajaTime_registro_x,cajaTime_registro_y, anchor=Tk.W, text='time', fill='yellow', font=('courier',14))

    cajaTime_texto_x=(posCajaStime[2])-5
    cajaTime_texto_y=cajaTime_registro_y
    cajaTime_texto=canvaslocal.create_text(cajaTime_texto_x, cajaTime_texto_y, anchor=Tk.E, text='Temp', fill='white', font=('courier',14))
    
    STimelocal={
        "cajaST":cajaStime,
        "cajaT":cajaTime,
        "cajaT_registro":cajaTime_registro,
        "cajaT_texto":cajaTime_texto,
        "cajaT_registro_temperatura":canvaslocal.itemcget(cajaTime_registro, 'text'),
    }
    return STimelocal



def crearSensores(posXasignar, posYasignar, amplitud_rect_X, amplitud_rect_Y, canvaslocal):
    posXSN1=posXasignar
    posYSN1=posYasignar
    amplitudX=amplitud_rect_X
    amplitudY=amplitud_rect_Y
    cajaSN1=canvaslocal.create_rectangle(posXSN1,posYSN1,posXSN1+(amplitudX),posYSN1+(amplitudY) ,fill='black')
    posCajaSN1=canvaslocal.coords(cajaSN1)
    posX1LEDSN1=float(posXSN1+(((posCajaSN1[2])-posXSN1)/3))
    posY1LEDSN1=(posCajaSN1[3])-5
    ledSN1=canvaslocal.create_oval(posXSN1+10,posYSN1+5, posX1LEDSN1,posY1LEDSN1, fill="red", outline='darkred')
    posLEDSN1=canvaslocal.coords(ledSN1)
    posXTextoSN1=(posLEDSN1[2]+((posCajaSN1[2]-posXSN1)*2/3)/2)
    posYTextoSN1=posCajaSN1[1]+((posCajaSN1[3]-posCajaSN1[1])/2)
    textoSN1=canvaslocal.create_text(posXTextoSN1,posYTextoSN1, anchor=Tk.CENTER, text='SN1', fill='white', font=('courier',14))
    #SN2:
    posXSN2=posCajaSN1[0]
    posYSN2=posCajaSN1[3]+15
    cajaSN2=canvaslocal.create_rectangle(posXSN2,posYSN2,posXSN2+(amplitudX),posYSN2+(amplitudY) ,fill='black')
    posCajaSN2=canvaslocal.coords(cajaSN2)
    posX1LEDSN2=float(posXSN2+(((posCajaSN2[2])-posXSN2)/3))
    posY1LEDSN2=(posCajaSN2[3])-5
    ledSN2=canvaslocal.create_oval(posXSN2+10,posYSN2+5, posX1LEDSN2,posY1LEDSN2, fill="red", outline='darkred')
    posLEDSN2=canvaslocal.coords(ledSN2)
    posXTextoSN2=(posLEDSN2[2]+((posCajaSN2[2]-posXSN2)*2/3)/2)
    posYTextoSN2=posCajaSN2[1]+((posCajaSN2[3]-posCajaSN2[1])/2)
    textoSN2=canvaslocal.create_text(posXTextoSN2,posYTextoSN2, anchor=Tk.CENTER, text='SN2', fill='white', font=('courier',14))
        #SN3:
    posXSN3=posCajaSN1[0]
    posYSN3=posCajaSN2[3]+15
    cajaSN3=canvaslocal.create_rectangle(posXSN3,posYSN3,posXSN3+(amplitudX),posYSN3+(amplitudY) ,fill='black')
    posCajaSN3=canvaslocal.coords(cajaSN3)
    posX1LEDSN3=float(posXSN3+(((posCajaSN3[2])-posXSN3)/3))
    posY1LEDSN3=(posCajaSN3[3])-5
    ledSN3=canvaslocal.create_oval(posXSN3+10,posYSN3+5, posX1LEDSN3,posY1LEDSN3, fill="red", outline='darkred')
    posLEDSN3=canvaslocal.coords(ledSN3)
    posXTextoSN3=(posLEDSN3[2]+((posCajaSN3[2]-posXSN3)*2/3)/2)
    posYTextoSN3=posCajaSN3[1]+((posCajaSN3[3]-posCajaSN3[1])/2)
    textoSN3=canvaslocal.create_text(posXTextoSN3,posYTextoSN3, anchor=Tk.CENTER, text='Svacio', fill='white', font=('courier',10))
    sensoresCanvaslocal={
        'cajaSN1':cajaSN1,
        'cajaSN2':cajaSN2,
        'cajaSN3':cajaSN3,
        'ledSN1':ledSN1,
        'ledSN2':ledSN2,
        'ledSN3':ledSN3,
        'ledSN1_color':canvaslocal.itemcget(ledSN1,'fill'),
        'ledSN2_color':canvaslocal.itemcget(ledSN2,'fill'),
        'ledSN3_color':canvaslocal.itemcget(ledSN3,'fill'),
        'textoSN1':textoSN1,
        'textoSN2':textoSN2,
        'textoSN3':textoSN3,  
    }
    return sensoresCanvaslocal



def crearST(pos_ST_X,pos_ST_Y, ampX, ampY, canvaslocal):
    posX=pos_ST_X
    posY=pos_ST_Y
    amplitudX=posX+ampX
    amplitudY=ampY
    cajaST=canvaslocal.create_rectangle(posX, posY, amplitudX, posY+(amplitudY), fill='black')

    posCajaST=canvaslocal.coords(cajaST)
    cajaT_x1=posX+((posCajaST[2]-posX)*2/3)
    cajaT_y1=posCajaST[3]-5
    cajaT=canvaslocal.create_rectangle(posX+5, posY+5, cajaT_x1, cajaT_y1, fill='darkred')
    posCajaT=canvaslocal.coords(cajaT)
    cajaT_registro_x=posCajaT[0]+3
    cajaT_registro_y=posCajaT[1]+((posCajaT[3]-posCajaT[1])/2)
    cajaT_registro=canvaslocal.create_text(cajaT_registro_x,cajaT_registro_y, anchor=Tk.W, text='80°C', fill='yellow', font=('courier',14))

    cajaT_texto_x=(posCajaST[2])-5
    cajaT_texto_y=cajaT_registro_y
    cajaT_texto=canvaslocal.create_text(cajaT_texto_x, cajaT_texto_y, anchor=Tk.E, text='T', fill='white', font=('courier',14))
    
    STlocal={
        "cajaST":cajaST,
        "cajaT":cajaT,
        "cajaT_registro":cajaT_registro,
        "cajaT_texto":cajaT_texto,
        "cajaT_registro_temperatura":canvaslocal.itemcget(cajaT_registro, 'text'),
    }
    return STlocal

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
    
    #def dibujar(self):
     #   canvaslocal=self.canvaslocal
      #  estado=self.estado
       # if(estado=='abierta'):
        #    self.ecV1_estate=canvaslocal.create_text(x_texto, y_texto, anchor=Tk.W, text='(ON)', font=('courier',18,BOLD), fill='red')
         #   self.figura1=canvaslocal.create_line(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,fill='lightblue',width=4)
          #  self.figura2=canvaslocal.create_line(p18,p19,p20,p21,p22,p23,p24,p25,fill="lightblue",width=4)
        #else:
         #   self.ecV1_estate=canvaslocal.create_text(x_texto, y_texto, anchor=Tk.W, text='(OFF)', font=('courier',18,BOLD), fill='red')
          #  self.figura1=canvaslocal.create_line(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,fill='black',width=4)
           # self.figura2=canvaslocal.create_line(p18,p19,p20,p21,p22,p23,p24,p25,fill="black",width=4)
