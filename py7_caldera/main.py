from os import name
from pathlib import Path
import tkinter as Tk
from tkinter.font import BOLD
from tkinter import Image, StringVar, ttk
from tkinter.constants import BOTH, BOTTOM, FALSE, HORIZONTAL, LEFT, RIGHT, TOP, TRUE, VERTICAL, X, Y
from tkinter.ttk import Frame
from tkinter import Button, Pack, ttk
import math
import time

from classesCaldera import *
from PIL import Image

class Controlador:
    def __init__(self):

        
        self.estado1=1
        self.estado2=2
        self.estado3=3
        self.estado4=4
        self.estado0=0

        self.estado_actual=1
        self.entradaGlobal=0
        self.salidaGlobal=0
        self.tempGlobal=0

    #label_boton_V1
    #label_boton_V2
    #label_boton_V3
    #label_boton_caldera

    #boton_V1
    #boton_V2
    #boton_V3
    #boton_caldera 
    #args: (self,canvas,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,el_sensor_T,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string)

    def apagar_caldera(self,c,sensorT,label_boton_caldera):
        c.set_name("C\napagada")
        c.fill_rect='black'
        c.fill_text='red'
        label_boton_caldera.config(text='Caldera: apagada')
        c.temp_inicio=c.temp_caldera
        c.start_time=time.time()
        c.dibujo_tkinter()
        sensorT.dibujar()
    def encender_caldera(self,c,sensorT,label_boton_caldera):
        c.set_name("C\nencendida")
        c.fill_rect='darkred'
        c.fill_text='yellow'
        label_boton_caldera.config(text='Caldera: encendida')
        c.temp_inicio=c.temp_caldera
        c.start_time=time.time()
        c.dibujo_tkinter()
        sensorT.dibujar()
        

    def cerrar_v1(self,canvaslocal,v1,label_boton_V1,label_boton_V1_string):
        v1.estado='cerrada'
        label_boton_V1_string.set('valvula1: cerrada')
        label_boton_V1.config(text=label_boton_V1_string.get())
        canvaslocal.itemconfig(v1.ecV1_estate,{"text":"(OFF)"})
        canvaslocal.itemconfig(v1.figura1,{"fill":"black"})
        canvaslocal.itemconfig(v1.figura2,{"fill":"black"})
    def cerrar_v2(self,canvaslocal,v2,label_boton_V2,):
        v2.estado='cerrada'
        label_boton_V2.config(text='valvula 2: cerrada')
        canvaslocal.itemconfig(v2.ecV1_estate,{"text":"(OFF)"})
        canvaslocal.itemconfig(v2.figura1,{"fill":"black"})
        canvaslocal.itemconfig(v2.figura2,{"fill":"black"})
    def cerrar_v3(self,canvaslocal,v3,label_boton_V3):
        v3.estado='cerrada'
        label_boton_V3.config(text='valvula 3: cerrada')
        canvaslocal.itemconfig(v3.ecV1_estate,{"text":"(OFF)"})
        canvaslocal.itemconfig(v3.figura1,{"fill":"black"})
        canvaslocal.itemconfig(v3.figura2,{"fill":"black"})

    def abrir_v1(self,canvas,v1,label_boton_V1,label_boton_V1_string):
        v1.estado='abierta'
        label_boton_V1_string.set('valvula 1: abierta')
        label_boton_V1.config(text=label_boton_V1_string.get())
        canvas.itemconfig(v1.ecV1_estate,{"text":"(ON)"})
        canvas.itemconfig(v1.figura1,{"fill":"lightblue"})
        canvas.itemconfig(v1.figura2,{"fill":"lightblue"})
    def abrir_v2(self,canvas,v2,label_boton_V2,):
        v2.estado='abierta'
        label_boton_V2.config(text='valvula 2: abierta')
        canvas.itemconfig(v2.ecV1_estate,{"text":"(ON)"})
        canvas.itemconfig(v2.figura1,{"fill":"lightblue"})
        canvas.itemconfig(v2.figura2,{"fill":"lightblue"})

    def abrir_v3(self,canvas,v3,label_boton_V3):
        v3.estado='abierta'
        label_boton_V3.config(text='valvula 3: abierta')
        canvas.itemconfig(v3.ecV1_estate,{"text":"(ON)"})
        canvas.itemconfig(v3.figura1,{"fill":"lightblue"})
        canvas.itemconfig(v3.figura2,{"fill":"lightblue"})
    

    def estado1_T1(self,canvas,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,el_sensor_T,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string):
        entradalocal=entrada
        salidalocal=salida

        v1.estado='cerrada'
        label_boton_V1_string.set('valvula1: cerrada')
        label_boton_V1.config(text=label_boton_V1_string.get())
        canvas.itemconfig(v1.ecV1_estate,{"text":"(OFF)"})
        canvas.itemconfig(v1.figura1,{"fill":"black"})
        canvas.itemconfig(v1.figura2,{"fill":"black"})

        v2.estado='cerrada'
        label_boton_V2.config(text='valvula 2: cerrada')
        canvas.itemconfig(v2.ecV1_estate,{"text":"(OFF)"})
        canvas.itemconfig(v2.figura1,{"fill":"black"})
        canvas.itemconfig(v2.figura2,{"fill":"black"})

        v3.estado='cerrada'
        label_boton_V3.config(text='valvula 3: cerrada')
        canvas.itemconfig(v3.ecV1_estate,{"text":"(OFF)"})
        canvas.itemconfig(v3.figura1,{"fill":"black"})
        canvas.itemconfig(v3.figura2,{"fill":"black"})

        
        if(c.name=="C\nencendida"):
            #c.name="C\napagada"
            c.set_name("C\napagada")
            c.fill_rect='black'
            c.fill_text='red'
            label_boton_caldera.config(text='Caldera: apagada')
            c.temp_inicio=c.temp_caldera
            c.start_time=time.time()
            c.dibujo_tkinter()
            el_sensor_T.dibujar()
        
        el_sensor_T.dibujar()
        el_temporizador.tiempo_cero=time.time()


        contenido_total=t1.contenido+t2.contenido
        if(t1.contenido<50):   
            print("No hay suficiente producto en T1 para llegar al nivel 1 en la caldera(almenos 50%)")
            entradalocal=0
            salidalocal=0
            return salidalocal
        else:
            if(contenido_total<92):
                print('No hay suficiente producto en T2 para realizar el proceso.')
                return salidalocal
            else:
                print('El proceso ha comenzado.')
                print('Abriendo valvula 1 hasta llenar nivel 1...')
                self.abrir_v1(canvas,v1,label_boton_V1,label_boton_V1_string)
                SN1.actualizar(c.nivel_liquido)
                while(SN1.nivel_liquido<SN1.nivel_sensor):
                    SN1.actualizar(c.nivel_liquido)
                    #####################################################################################################
                self.cerrar_v1(canvas,v1,label_boton_V1,label_boton_V1_string)
                print('nivel 1 de caldera alcanzado.')
                entradalocal=1
                return entradalocal

    def estado2_condicional(self,canvas,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,el_sensor_T,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string):
                entreadalocal=entrada
                salidalocal=salida
                print('Calentando producto por 5 segundos....') 
                self.encender_caldera(c,el_sensor_T,label_boton_caldera)

                def metodolocal():
                    self.tempGlobal=el_sensor_T.temperatura
                root.after(4900,metodolocal())
                root.after(100,self.apagar_caldera(c,el_sensor_T,label_boton_caldera))
                print('producto calentado por 5 sg,')
                if(self.tempGlobal<80):
                    print('la temperatura NO supero los 80 grados, vertiendo producto de T2...')
                    entreadalocal=0
                    return entreadalocal
                else:
                    print('la temperatura supero los 80 grados, producto terminado satisfactoriamente.')
                    entradalocal=1
                    return entradalocal

    
    def proceso_estados(self,canvas,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,el_sensor_T,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string):
        self.entradaGlobal=self.estado1_T1(canvas,entrada,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,el_sensor_T,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string)
        if(self.entradaGlobal==0):
            print('se culmino el ciclo en el estado 0')
          
        else:
            self.entradaGlobal=self.estado2_condicional(canvas,self.entradaGlobal,t1,t2,t3,SN1,SN2,SN3,v1,v2,v3,c,el_sensor_T,el_temporizador,salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string)
            print('se culmino el ciclo en el estado 3')
        
    

                

#sensorN2.actualizar(caldera.nivel_liquido)
#   sensorN1.actualizar(caldera.nivel_liquido)
#   sensorNvacio.actualizar(caldera.nivel_liquido)

        






#frame scrollbar:
root=Tk.Tk()
root.geometry("720x630")

main_frame=Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas=Tk.Canvas(main_frame)
my_canvas.pack(side=TOP,fill=BOTH,expand=1)

my_scrollbar=ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
my_scrollbar.pack(side=BOTTOM, fill=X)
my_canvas.configure(xscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox(all)))

second_frame=Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor='nw')

########################

framePrincipal=Tk.Frame(second_frame)
framePrincipal.config(bg="white")
framePrincipal.config(bd=5)
framePrincipal.pack(anchor=Tk.NW)

#frame canvas:
frame1=Tk.Frame(framePrincipal)
frame1.config(bg="white")
frame1.pack(side=LEFT,fill='y')

canvas=Tk.Canvas(frame1, width=520, height=600)
canvas.pack(anchor=Tk.NW)
imgModelo=Tk.PhotoImage(file="plantaQuimicosModelo.gif")
imagenModelo=canvas.create_image(0,0, anchor=Tk.NW, image=imgModelo)

      #labels:






valvula1=Valvula(109-70,180-2,canvas,"cerrada",131,154,132,159,135,162,141,164,141,170,179,160,179,171,141,158,141,164,207,194,197,177,189,170,179,167)
valvula2=Valvula(458-88, 291-110,canvas,"cerrada",337,159,334,164,332,166,325,167,325,162,286,174,286,161,325,176,325,167,261,194,270,178,281,169,286,167)
valvula3=Valvula(456-88, 428-110,canvas,"cerrada",284,309,285,314,290,321,290,321, 290,315,331,330,329,316,291,330,290,321, 361,349,352,337,346,331,330,323)
#frame Sensores:
##E4E4E4 defualt color canvas
frameData=Tk.Frame(framePrincipal)
frameData.pack(side=RIGHT, fill='y')
frameData.config(bd=5)
frameData.config(relief="sunken")
canvasSensores=Tk.Canvas(frameData, width=200, height=300)
bgCanvasSensores=canvasSensores.__getitem__('bg')
frameData.config(bg=bgCanvasSensores)


#copia1 sensores:
#crear en canvas:


tanque1=Tanque('T1', 200,100, 68,54,180,138,canvas)
tanque2=Tanque('T2', 200,100, 291,56,400,143,canvas)
tanque3=Tanque('T3', 200,0, 301,365,483,453,canvas)
caldera=Caldera('C\napagada', 300, 0, 161,210,318,299,30,canvas)

sensor_T=Sensor_temperatura(caldera.temp_caldera,caldera.name,332,240,80,40,canvas)
temporizador=Temporizador(19,409,219,469,canvas)

sensorN2=Sensor_nivel('2',219,caldera.nivel_liquido,44,204,100,20,canvas)
sensorN1=Sensor_nivel('1',258,caldera.nivel_liquido,44,243,100,20,canvas)
sensorNvacio=Sensor_nivel('vacio',299,caldera.nivel_liquido,5,278,140,20,canvas)



#menu botones:
frame_menu_botones=Tk.Frame(canvas)
menuBotones=canvas.create_window(0,480, anchor=Tk.NW, width=520, height=120, window=frame_menu_botones)
frame_menu_botones.config()

label_boton_V1_string=StringVar(frame_menu_botones)
label_boton_V2_string=StringVar(frame_menu_botones)
label_boton_V3_string=StringVar(frame_menu_botones)
label_boton_caldera_string=StringVar(frame_menu_botones)
label_boton_V1_string.set("valvula 1: cerrada")
label_boton_V2_string.set('valvula 2: cerrada')
label_boton_V3_string.set('valvula 3: cerrada')
label_boton_caldera_string.set('Caldera: apagada')



label_boton_V1=Tk.Label(frame_menu_botones, text=label_boton_V1_string.get(),font=('courier',12))
label_boton_V2=Tk.Label(frame_menu_botones, text='valvula 2: cerrada', font=('courier',12))
label_boton_V3=Tk.Label(frame_menu_botones, text='valvula 3: cerrada', font=('courier',12))
label_boton_caldera=Tk.Label(frame_menu_botones, text='Caldera: apagada', font=('courier',12))


def accion_boton_V1():

    if(valvula1.estado=='abierta'):
        valvula1.estado='cerrada'
        label_boton_V1_string.set('valvula1: cerrada')
        label_boton_V1.config(text=label_boton_V1_string.get())
        canvas.itemconfig(valvula1.ecV1_estate,{"text":"(OFF)"})
        canvas.itemconfig(valvula1.figura1,{"fill":"black"})
        canvas.itemconfig(valvula1.figura2,{"fill":"black"})

    else:
        valvula1.estado='abierta'
        label_boton_V1_string.set('valvula 1: abierta')
        label_boton_V1.config(text=label_boton_V1_string.get())
        canvas.itemconfig(valvula1.ecV1_estate,{"text":"(ON)"})
        canvas.itemconfig(valvula1.figura1,{"fill":"lightblue"})
        canvas.itemconfig(valvula1.figura2,{"fill":"lightblue"})

def accion_boton_V2():
    
    if(valvula2.estado=='abierta'):
        valvula2.estado='cerrada'
        label_boton_V2.config(text='valvula 2: cerrada')
        canvas.itemconfig(valvula2.ecV1_estate,{"text":"(OFF)"})
        canvas.itemconfig(valvula2.figura1,{"fill":"black"})
        canvas.itemconfig(valvula2.figura2,{"fill":"black"})
    else:
        valvula2.estado='abierta'
        label_boton_V2.config(text='valvula 2: abierta')
        canvas.itemconfig(valvula2.ecV1_estate,{"text":"(ON)"})
        canvas.itemconfig(valvula2.figura1,{"fill":"lightblue"})
        canvas.itemconfig(valvula2.figura2,{"fill":"lightblue"})

def accion_boton_V3():
    if(valvula3.estado=='abierta'):
        valvula3.estado='cerrada'
        label_boton_V3.config(text='valvula 3: cerrada')
        canvas.itemconfig(valvula3.ecV1_estate,{"text":"(OFF)"})
        canvas.itemconfig(valvula3.figura1,{"fill":"black"})
        canvas.itemconfig(valvula3.figura2,{"fill":"black"})
    else:
        valvula3.estado='abierta'
        label_boton_V3.config(text='valvula 3: abierta')
        canvas.itemconfig(valvula3.ecV1_estate,{"text":"(ON)"})
        canvas.itemconfig(valvula3.figura1,{"fill":"lightblue"})
        canvas.itemconfig(valvula3.figura2,{"fill":"lightblue"})

def accion_boton_Caldera():
    if(caldera.name=="C\nencendida"):
        label_boton_caldera.config(text='Caldera: apagada')
        caldera.set_name("C\napagada")
        caldera.fill_rect='black'
        caldera.fill_text='red'
        caldera.temp_inicio=caldera.temp_caldera
        caldera.start_time=time.time()
        caldera.dibujo_tkinter()
        sensor_T.dibujar
          
    else:
        label_boton_caldera.config(text='Caldera: encendida')
        caldera.set_name("C\nencendida")
        caldera.fill_rect='darkred'
        caldera.fill_text='yellow'
        caldera.temp_inicio=caldera.temp_caldera
        caldera.start_time=time.time()
        caldera.dibujo_tkinter()
        sensor_T.dibujar
        
        
    
boton_V1=Tk.Button(frame_menu_botones, text='cambiar estado',font=('courier',9), command=accion_boton_V1)
boton_V2=Tk.Button(frame_menu_botones, text='cambiar estado',font=('courier',9), command=accion_boton_V2)
boton_V3=Tk.Button(frame_menu_botones, text='cambiar estado',font=('courier',9), command=accion_boton_V3)
boton_caldera=Tk.Button(frame_menu_botones, text='cambiar estado',font=('courier',9), command=accion_boton_Caldera)

label_boton_V1.grid(row=0, column=0)
label_boton_V2.grid(row=1, column=0)
label_boton_V3.grid(row=2, column=0)
label_boton_caldera.grid(row=3, column=0)

boton_V1.grid(row=0, column=1)
boton_V2.grid(row=1, column=1)
boton_V3.grid(row=2, column=1)
boton_caldera.grid(row=3, column=1)







#crear en canvasSensores:
#frame Data:












boton_T1=Tk.Button(frame_menu_botones, text='adicionar a T1',font=('courier',9), command=tanque1.adicionar10())
boton_T2=Tk.Button(frame_menu_botones, text='adicionar a T2',font=('courier',9), command=tanque2.adicionar10())
boton_T3=Tk.Button(frame_menu_botones, text='sustraer a T3',font=('courier',9), command=tanque3.sustraer10())
boton_T1.grid(row=0,column=3)
boton_T2.grid(row=1,column=3)
boton_T3.grid(row=2,column=3)
#def motion(event):
#    x, y = event.x, event.y
#    print('{}, {}'.format(x, y))
#root.bind('<Motion>', motion)




def act_tiempo_and_reg_temp():
    t_real=time.time()
    caldera.calcular_temp(t_real)
    sensor_T.temperatura=caldera.temp_caldera
    sensor_T.dibujar()

    temporizador.timer=time.time()-temporizador.tiempo_cero
    temporizador.dibujar()
   
    root.after(1000,act_tiempo_and_reg_temp)

act_tiempo_and_reg_temp()

#def actualizar_tiempo():
#    temporizador.timer=time.time()-temporizador.tiempo_cero
#    temporizador.dibujar()
#    root.after(1000,actualizar_tiempo)
#actualizar_tiempo()

def fisicaValvulas():
    if(valvula1.estado=='abierta'):
        if(tanque1.contenido!=0 and caldera.contenido!=caldera.capacidad):
            tanque1.sustraer(1)
            caldera.adicionar(1)
    if(valvula2.estado=='abierta'):
        if(tanque2.contenido!=0 and caldera.contenido!=caldera.capacidad):
            tanque2.sustraer(1)
            caldera.adicionar(1)
    if(valvula3.estado=='abierta'):
        if(caldera.contenido!=0 and tanque3.contenido!=tanque3.capacidad):
            tanque3.adicionar(3)
            caldera.sustraer(3)
    sensorN2.actualizar(caldera.nivel_liquido)
    sensorN1.actualizar(caldera.nivel_liquido)
    sensorNvacio.actualizar(caldera.nivel_liquido)
    root.after(200,fisicaValvulas)
fisicaValvulas()
maquina_estado=Controlador()

def accion_botonInico():
    maquina_estado.proceso_estados(canvas,0,tanque1,tanque2,tanque3,sensorN1,sensorN2,sensorNvacio,valvula1,valvula2,valvula3,caldera,sensor_T,temporizador,0,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string)

botonInicio=Tk.Button(canvas,text='iniciar',font=('courier',18), command=accion_botonInico)
botonInicio.config( activebackground='green', bd=10, font=('courier',18,BOLD))
botonInicio.place(x=102-88, y=431-110, width=219-101-1, height=510-430-1)

root.mainloop()