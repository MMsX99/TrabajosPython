import tkinter as Tk
from tkinter.constants import BOTTOM, FALSE, LEFT, NW, RIGHT, TOP, TRUE
from tkinter.font import BOLD

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
    textoSN1=canvaslocal.create_text(posXTextoSN1,posYTextoSN1, anchor=Tk.CENTER, text='SN1', fill='white', font=('courier',18))
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
    textoSN2=canvaslocal.create_text(posXTextoSN2,posYTextoSN2, anchor=Tk.CENTER, text='SN2', fill='white', font=('courier',18))
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
    textoSN3=canvaslocal.create_text(posXTextoSN3,posYTextoSN3, anchor=Tk.CENTER, text='Svacio', fill='white', font=('courier',12))
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
    cajaT_texto=canvaslocal.create_text(cajaT_texto_x, cajaT_texto_y, anchor=Tk.E, text='ST', fill='white', font=('courier',14))
    
    STlocal={
        "cajaST":cajaST,
        "cajaT":cajaT,
        "cajaT_registro":cajaT_registro,
        "cajaT_texto":cajaT_texto,
        "cajaT_registro_temperatura":canvaslocal.itemcget(cajaT_registro, 'text'),
    }
    return STlocal

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

mainWindow=Tk.Tk()
mainWindow.config(bg="blue")
mainWindow.title("Planta proceso quimco")
mainWindow.wm_title("Planta proceso quimico")
mainWindow.geometry("1200x615")

framePrincipal=Tk.Frame(mainWindow)
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

canvas.create_rectangle(101-88,430-110,219-88,510-110, fill='darkred')
botonInicio=Tk.Button(canvas,text='iniciar',font=('courier',18))
botonInicio.config(bg='darkred', activebackground='red', fg='yellow', bd=0)
botonInicio.place(x=102-88, y=431-110, width=219-101-1, height=510-430-1)

ecCaldera_estate=canvas.create_text(329-88, 355-110, anchor=Tk.N, text='caldera\nencendida', font=('courier',14,BOLD), fill='red', justify='center')

ecV1_estate=canvas.create_text(197-88, 290-110, anchor=Tk.E, text='(ON)', font=('courier',20,BOLD), fill='red')
ecV2_estate=canvas.create_text(458-88, 291-110, anchor=Tk.W, text='(OFF)', font=('courier',20,BOLD), fill='red')
ecV3_estate=canvas.create_text(456-88, 428-110, anchor=Tk.W, text='(OFF)', font=('courier',20,BOLD), fill='red')

#frame Sensores:
##E4E4E4 defualt color canvas
frameData=Tk.Frame(framePrincipal)
frameData.pack(side=RIGHT, fill='y')
frameData.config(bd=5)
frameData.config(relief="sunken")
canvasSensores=Tk.Canvas(frameData, width=200, height=300)
atributosCanvasSensores=canvasSensores.__getitem__('bg')
frameData.config(bg=atributosCanvasSensores)

#crear en canvas:
arg_S_Canvas=crearSensores(0,195, 90,30, canvas)
arg_ST_canvas=crearST(393,240,100,50,canvas)
arg_Stime_canvas=crearStime(19,409,200,60,canvas)
#crear en canvasSensores:
arg_S_canvasSensores=crearSensores(0,0, 125,25,canvasSensores)

coordsSN3=canvasSensores.coords(arg_S_canvasSensores['cajaSN3'])
arg_ST_canvasSensores=crearST(coordsSN3[0],coordsSN3[3]+15,100,30,canvasSensores)

coordsST=canvasSensores.coords(arg_ST_canvasSensores['cajaST'])
arg_Stime_canvasSen=crearStime(coordsST[0],coordsST[3]+15,150,30,canvasSensores)

eLabelTitle=Tk.Label(frameData,text='TABLA DE DATOS', font=('courier',20))
eLabelTitle.grid(row=0,column=0,)

eLabelTitle2=Tk.Label(frameData,text='VALUE', font=('courier',20))
eLabelTitle2.grid(row=0,column=1)

eLabelV1=Tk.Label(frameData,text='  V1: estado valvula 1',font=('courier',16))
eLabelV2=Tk.Label(frameData,text='  V2: estado valvula 2',font=('courier',16))
eLabelV3=Tk.Label(frameData,text='  V3: estado valvula 3',font=('courier',16))
eEstadoC=Tk.Label(frameData, text=' estado caldera ',font=('courier',16))

eLabelV1.grid(row=1,column=0)
eLabelV2.grid(row=2,column=0)
eLabelV3.grid(row=3,column=0)
eEstadoC.grid(row=4,column=0)

eValueV1=Tk.Label(frameData,text='ON',font=('courier',16))
eValueV2=Tk.Label(frameData,text='ON',font=('courier',16))
eValueV3=Tk.Label(frameData,text='ON',font=('courier',16))
eEstadoC_value=Tk.Label(frameData, text='encendida',font=('courier',16))

eValueV1.grid(row=1,column=1)
eValueV2.grid(row=2,column=1)
eValueV3.grid(row=3,column=1)
eEstadoC_value.grid(row=4,column=1)

canvasSensores.grid(column=3, row=5, rowspan=14)
canvasSensores_to_Data=[0,0]+[418,158]

eLabelSN1=Tk.Label(frameData,text="SN1, sensor de nivel 1 ",font=('courier',16))
eLabelSN2=Tk.Label(frameData,text="SN2, sensor de nivel 2",font=('courier',16))
eLabelSN3=Tk.Label(frameData,text="SN3, sensor de nivel 3",font=('courier',16))
eLabelST=Tk.Label(frameData,text="ST, sensor temperatura C",font=('courier',16))
eLabelStime=Tk.Label(frameData,text="Stime, temporizador",font=('courier',16))

eLabelSN1.grid(row=5,column=0)
eLabelSN2.grid(row=6,column=0)
eLabelSN3.grid(row=7,column=0)
eLabelST.grid(row=8,column=0)
eLabelStime.grid(row=9,column=0)

eValueSN1=Tk.Label(frameData,text="Lleno",font=('courier',16))
eValueSN2=Tk.Label(frameData,text="incompleto",font=('courier',16))
eValueSN3=Tk.Label(frameData,text="incompleto",font=('courier',16))
eT_value=Tk.Label(frameData,text="80 °C",font=('courier',16))
eStime_value=Tk.Label(frameData,text="0 sg",font=('courier',16))

eValueSN1.grid(row=5,column=1)
eValueSN2.grid(row=6,column=1)
eValueSN3.grid(row=7,column=1)
eT_value.grid(row=8,column=1)
eStime_value.grid(row=9,column=1)

mainWindow.mainloop()