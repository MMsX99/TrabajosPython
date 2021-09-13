
import tkinter as Tk
from tkinter.font import BOLD
from tkinter import StringVar 
from tkinter.constants import BOTH, BOTTOM, FALSE, HORIZONTAL, LEFT, RIGHT, TOP, TRUE, VERTICAL, X, Y
from tkinter.ttk import Frame
import math
import time

from classesCaldera import *

        

#sensorN2.actualizar(caldera.nivel_liquido)
#   sensorN1.actualizar(caldera.nivel_liquido)
#   sensorNvacio.actualizar(caldera.nivel_liquido)



#frame scrollbar:
root=Tk.Tk()
root.geometry("550x630")

main_frame=Frame(root)
main_frame.pack(anchor=Tk.NW)

########################

framePrincipal=Tk.Frame(main_frame)
framePrincipal.config(bg="black")
framePrincipal.config(bd=3)
framePrincipal.pack(anchor=Tk.NW)

#frame canvas:
frame1=Tk.Frame(framePrincipal)
frame1.config(bd=5, bg="white")
frame1.pack(side=LEFT)

canvas=Tk.Canvas(frame1, width=520, height=600)
canvas.pack(anchor=Tk.NW)
imgModelo=Tk.PhotoImage(file="plantaQuimicosModelo.gif")
imagenModelo=canvas.create_image(0,0, anchor=Tk.NW, image=imgModelo)



##E4E4E4 defualt color canvvas
#crear en canvas:
# OBJETOS #
valvula1=Valvula(109-70,180-2,canvas,"cerrada",131,154,132,159,135,162,141,164,141,170,179,160,179,171,141,158,141,164,207,194,197,177,189,170,179,167)
valvula2=Valvula(458-88, 291-110,canvas,"cerrada",337,159,334,164,332,166,325,167,325,162,286,174,286,161,325,176,325,167,261,194,270,178,281,169,286,167)
valvula3=Valvula(456-88, 428-110,canvas,"cerrada",284,309,285,314,290,321,290,321, 290,315,331,330,329,316,291,330,290,321, 361,349,352,337,346,331,330,323)

tanque1=Tanque('T1', 200,100, 68,54,180,138,canvas)
tanque2=Tanque('T2', 200,90, 291,56,400,143,canvas)
tanque3=Tanque('T3', 300,0, 301,365,483,453,canvas)
caldera=Caldera('C\napagada', 200, 0, 161,210,318,299,30,canvas)

sensor_T=Sensor_temperatura(caldera.temp_caldera,caldera.name,332,240,80,40,canvas)
temporizador=Temporizador(19,409,219,469,canvas)

sensorN2=Sensor_nivel('2',219,caldera.nivel_liquido,44,204,100,20,canvas)
sensorN1=Sensor_nivel('1',258,caldera.nivel_liquido,44,243,100,20,canvas)
sensorNvacio=Sensor_nivel('vacio',299,caldera.nivel_liquido,5,278,140,20,canvas)


#menu botones:
frame_menu_botones=Tk.Frame(canvas)
menuBotones=canvas.create_window(0,480, anchor=Tk.NW, width=520, height=120, window=frame_menu_botones)
frame_menu_botones.config(bd=3, bg='white')


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
        valvula1.actualizar_dibujo()
        

    else:
        valvula1.estado='abierta'
        label_boton_V1_string.set('valvula 1: abierta')
        label_boton_V1.config(text=label_boton_V1_string.get())
        valvula1.actualizar_dibujo()

def accion_boton_V2():
    
    if(valvula2.estado=='abierta'):
        valvula2.estado='cerrada'
        label_boton_V2.config(text='valvula 2: cerrada')
        valvula2.actualizar_dibujo()
    else:
        valvula2.estado='abierta'
        label_boton_V2.config(text='valvula 2: abierta')
        valvula2.actualizar_dibujo()

def accion_boton_V3():
    if(valvula3.estado=='abierta'):
        valvula3.estado='cerrada'
        label_boton_V3.config(text='valvula 3: cerrada')
        valvula3.actualizar_dibujo()
    else:
        valvula3.estado='abierta'
        label_boton_V3.config(text='valvula 3: abierta')
        valvula3.actualizar_dibujo()

def accion_boton_Caldera():
    if(caldera.estado=="C\nencendida"):
        label_boton_caldera.config(text='Caldera: apagada')
        caldera.estado="C\napagada"
        caldera.temp_inicio=caldera.temp_caldera
        caldera.start_time=time.time()
        caldera.actualizar_dibujo()
        sensor_T.actualizar_dibujo()
          
    else:
        label_boton_caldera.config(text='Caldera: encendida')
        caldera.estado="C\nencendida"
        caldera.temp_inicio=caldera.temp_caldera
        caldera.start_time=time.time()
        caldera.actualizar_dibujo()
        sensor_T.actualizar_dibujo()
        
        
    
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


# CICLOS y metodos:

#def motion(event):
#    x, y = event.x, event.y
#    print('{}, {}'.format(x, y))
#root.bind('<Motion>', motion)

def accion_T1():
    tanque1.adicionar10()
def accion_T2():
    tanque2.adicionar10()
def accion_T3():
    tanque3.sustraer10()
boton_T1=Tk.Button(frame_menu_botones, text='adicionar a T1',font=('courier',9), command=accion_T1)
boton_T2=Tk.Button(frame_menu_botones, text='adicionar a T2',font=('courier',9), command=accion_T2)
boton_T3=Tk.Button(frame_menu_botones, text='sustraer a T3',font=('courier',9), command=accion_T3)
boton_T1.grid(row=0,column=3)
boton_T2.grid(row=1,column=3)
boton_T3.grid(row=2,column=3)

def act_tiempo_and_reg_temp():
    t_real=time.time()
    caldera.calcular_temp(t_real)
    sensor_T.temperatura=caldera.temp_caldera
    sensor_T.actualizar_dibujo()

    temporizador.timer=time.time()-temporizador.tiempo_cero
    temporizador.actualizar_dibujo()
   
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
            tanque1.sustraer(2)
            caldera.adicionar(2)
    if(valvula2.estado=='abierta'):
        if(tanque2.contenido!=0 and caldera.contenido!=caldera.capacidad):
            tanque2.sustraer(2)
            caldera.adicionar(2)
    if(valvula3.estado=='abierta'):
        if(caldera.contenido!=0 and tanque3.contenido!=tanque3.capacidad):
            tanque3.adicionar(4)
            caldera.sustraer(4)
    sensorN2.actualizar_sensor(caldera.nivel_liquido)
    sensorN1.actualizar_sensor(caldera.nivel_liquido)
    sensorNvacio.actualizar_sensor(caldera.nivel_liquido)
    root.after(500,fisicaValvulas)
fisicaValvulas()

controlador=Controlador()

def accion_botonI():
    controlador.estado_controlador=True
    controlador.ejecutar_proceso(canvas,controlador.entrada,tanque1,tanque2,tanque3,sensorN1,sensorN2,sensorNvacio,valvula1,valvula2,valvula3,caldera,sensor_T,temporizador,controlador.salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,root)


def accion_botonInicio1():
    controlador.estado_controlador=True
    controlador.proceso_control(canvas,controlador.entrada,tanque1,tanque2,tanque3,sensorN1,sensorN2,sensorNvacio,valvula1,valvula2,valvula3,caldera,sensor_T,temporizador,controlador.salida,label_boton_caldera,label_boton_V1,label_boton_V2,label_boton_V3,label_boton_V1_string,root)
    if(controlador.estado_controlador==True):
        
        root.after(500, accion_botonInicio1)

botonInicio=Tk.Button(canvas,text='iniciar',font=('courier',18) ,command=accion_botonInicio1)
botonInicio.config( activebackground='green', bd=10, font=('courier',18,BOLD))
botonInicio.place(x=102-88, y=431-110, width=219-101-1, height=510-430-1)


root.mainloop()