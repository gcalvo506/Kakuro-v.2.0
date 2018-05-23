#Importa la libreria tkinter
from tkinter import *
from tkinter import messagebox


"Función que desarrolla el juego"
def juego():
    global tableroframe
    global nombre_jugador
    global matriz_jugadas
    global lista_btns
    global juegoraiz
    global btn_empezar
    global relojframe
    #Crea la raiz y le da algunas caracteristicas
    juegoraiz=Tk()
    juegoraiz.title("A Jugar!")
    juegoraiz.geometry("1920x700+0+0")
    juegoraiz.config(bg="purple1")

    #Crea el frame del tablero para jugar y le da algunas caracteristicas
    tableroframe=Frame(juegoraiz)
    tableroframe.place(x=50,y=50)
    tableroframe.config(bg='grey')
    
    #Crea las labels de las claves
    for a in range(0,9):
        for b in range(0,9):
            Label(tableroframe, bg='black', text='\\',font=('Console',15),
                  fg='white',width=5,height="1",bd='5',relief=GROOVE).grid(row=a,column=b)

    #Escoge las claves y botones necesarios para la partida
    datos_partida=escoger_partida()

    matriz_jugadas=[[0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0]]

    #Crea las listas para asignar a los botones y labels
    lista_btns=[["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                    ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                    ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                    ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                    ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                    ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                    ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                    ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                    ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"]]
        
    #Despliega el tablero con las claves y los botones correspondientes de las tuplas datos_partida
    for contenido in datos_partida:
        global matriz_jugadas2
        global lista_btns2
        global numero_select
        tipo=contenido[0]
        etiqueta=contenido[1]
        fila=contenido[2]
        columna=contenido[3]
        contbtn=contenido[4]
        etiqueta2=""
        copia_etiqueta=etiqueta
        if tipo==2:
            if matriz_jugadas[fila-1][columna-1]!=0:
                for a in matriz_jugadas[fila-1][columna-1]:
                    if a=="\\" or a in "1234567890":
                        etiqueta2+=a
                etiqueta=str(etiqueta)+etiqueta2
            else:
                etiqueta=str(etiqueta)+"\\#"
            matriz_jugadas[fila-1][columna-1]=etiqueta
            etiqueta2=""
            for b in etiqueta:
                if b=="\\" or b in "1234567890":
                    etiqueta2+=b
            Label(tableroframe, bg="black", fg="white", width="5", height="1", text=etiqueta2, justify="right",relief=GROOVE, font=('Console',15)).grid(row=fila-1, column=columna-1)
        if tipo==1:
            if matriz_jugadas[fila-1][columna-1]!=0:
                for a in matriz_jugadas[fila-1][columna-1]:
                    if a=="\\" or a in "1234567890":
                        etiqueta2+=a
                etiqueta=str(etiqueta)
                etiqueta=etiqueta2+etiqueta
            else:
                etiqueta=str(etiqueta)
                etiqueta="#\\"+etiqueta
            matriz_jugadas[fila-1][columna-1]=etiqueta
            etiqueta2=""
            for b in etiqueta:
                if b=="\\" or b in "1234567890":
                    etiqueta2+=b
            Label(tableroframe, bg="black", fg="white", width="5", height="1", text=etiqueta2, justify="left",relief=GROOVE, font=('Console',15)).grid(row=fila-1, column=columna-1)
        while contbtn>0:
            if tipo==1:
                columna+=1
            if tipo==2:
                fila+=1
            posicion=(fila,columna)
            a=fila-1
            z=columna-1
            lista_btns[a][z]=Button(tableroframe, width="5", height="1",state='disabled',command = lambda a=a, z=z: ing_matriz(a,z), font=('Console',15))
            lista_btns[a][z].grid(row=a, column=z)
            contbtn-=1
    for fila in range(0,9):
            num1=0
            num2=0
            for columna in range(0,9):
                if matriz_jugadas[fila][columna]!=0:
                    ind_var=True
                    for datosmatriz in matriz_jugadas[fila][columna]:
                        tamañotupla=len(matriz_jugadas[fila][columna])
                        if datosmatriz=="\\":
                            ind_var=False
                        if ind_var==True:
                            if datosmatriz in "1234567890":
                                datosmatriz=int(datosmatriz)
                                num1=(num1*10)+datosmatriz
                            if datosmatriz=="#":
                                num1=0
                        else:
                            if datosmatriz in "1234567890":
                                num2=num2*10+int(datosmatriz)
                            if datosmatriz=="#":
                                num2=0
                    matriz_jugadas[fila][columna]=(num1,num2)
                    num1=0
                    num2=0
    lista_btns2=lista_btns[:]
    matriz_jugadas2=matriz_jugadas[:]

    #Crea el frame de los botones numericos y le da algunas caracteristicas
    numerosframe=Frame(juegoraiz)
    numerosframe.place(x=950,y=100)

    #Crea los botones de los numeros
    btn1=Button(numerosframe, bg='grey', text='1', font=('Console',20),
                width=3, bd='2', relief=RAISED, activebackground='Red',
                command=lambda:ind_num(1)).grid(row=0,column=0)
    btn2=Button(numerosframe, bg='grey', text='2', font=('Console',20),
                width=3, bd='2', relief=RAISED, activebackground='Red',
                command=lambda:ind_num(2)).grid(row=1,column=0)
    btn3=Button(numerosframe, bg='grey', text='3', font=('Console',20),
                width=3, bd='2', relief=RAISED, activebackground='Red',
                command=lambda:ind_num(3)).grid(row=2,column=0)
    btn4=Button(numerosframe, bg='grey', text='4', font=('Console',20),
                width=3, bd='2', relief=RAISED, activebackground='Red',
                command=lambda:ind_num(4)).grid(row=3,column=0)
    btn5=Button(numerosframe, bg='grey', text='5', font=('Console',20),
                width=3, bd='2', relief=RAISED, activebackground='Red',
                command=lambda:ind_num(5)).grid(row=4,column=0)
    btn6=Button(numerosframe, bg='grey', text='6', font=('Console',20),
                width=3, bd='2', relief=RAISED, activebackground='Red',
                command=lambda:ind_num(6)).grid(row=5,column=0)
    btn7=Button(numerosframe, bg='grey', text='7', font=('Console',20),
                width=3, bd='2', relief=RAISED, activebackground='Red',
                command=lambda:ind_num(7)).grid(row=6,column=0)
    btn8=Button(numerosframe, bg='grey', text='8', font=('Console',20),
                width=3, bd='2', relief=RAISED, activebackground='Red',
                command=lambda:ind_num(8)).grid(row=7,column=0)
    btn9=Button(numerosframe, bg='grey', text='9', font=('Console',20),
                width=3, bd='2', relief=RAISED, activebackground='Red',
                command=lambda:ind_num(9)).grid(row=8,column=0)

    #Crea los botones especiales de juego
    btn_empezar=Button(juegoraiz, bg='steel blue', text='Iniciar\nJuego', font=('Console',20),command=lambda:iniciar_partida(),
                       width=7, bd='2', relief=RAISED).place(x=1060,y=100)
    btn_terminar=Button(juegoraiz, bg='steel blue', text='Terminar\nJuego', font=('Console',20),
                       width=7, bd='2', relief=RAISED).place(x=1200,y=100)
    btn_jugada=Button(juegoraiz, bg='steel blue', text='Deshacer\nJugada', font=('Console',20),command=lambda:borrar_jugada(),
                       width=7, bd='2', relief=RAISED).place(x=1060,y=200)
    btn_juego=Button(juegoraiz, bg='steel blue', text='Borrar\nJuego', font=('Console',20), command=lambda:borrar_juego(),
                       width=7, bd='2', relief=RAISED).place(x=1200,y=200)
    btn_guardar=Button(juegoraiz, bg='steel blue', text='Guardar\nJuego', font=('Console',20),command=lambda:guardar_partida(),
                       width=7, bd='2', relief=RAISED).place(x=1060,y=300)
    btn_cargar=Button(juegoraiz, bg='steel blue', text='Cargar\nJuego', font=('Console',20),
                       width=7, bd='2', relief=RAISED).place(x=1200,y=300)
    btn_rehace=Button(juegoraiz, bg='steel blue', text='Rehacer\nJugada', font=('Console',20),
                       width=7, bd='2', relief=RAISED,command=lambda:rehacer()).place(x=1130,y=400)

    #Crea el frame del controlador de tiempo y le da algunas caracteristicas
    relojframe=Frame(juegoraiz)
    relojframe.config(bg='white',bd='3',relief='solid')
    relojframe.place(x=120,y=450)
    relojlabel=Label(relojframe,text="00:00:00",font=("Console",20),bg="grey").grid(row=0,column=0)

    #Crea el entry para que el jugador digite su nombre y su etiqueta
    nombre_jugador=StringVar(juegoraiz)
    nombre_jgdr_etd=Entry(juegoraiz, textvariable=nombre_jugador,width=30,
                          bg='snow',justify='right').place(x=390,y=550)
    Label(juegoraiz,text='Nombre del Jugador:',fg='snow', bg='purple1',
          font=('Console',20) ).place(x=120,y=540)
    
        
            
    juegoraiz.mainloop()

    
"Función que borra la jugada anterior que realizó el jugador"
def borrar_jugada():
    global matriz_jugadas
    global lista_btns
    global lista_jugadas
    global lista_btns2
    global ind_iniciado
    global jugadas_borradas
    global etiquetas_borradas
    if ind_iniciado== False:
        messagebox.showinfo("Advertencia","No se ha iniciado el juego.")
    if len(lista_jugadas)>0:
        fila,columna=lista_jugadas[-1]
        etiquetas_borradas+=[matriz_jugadas[fila][columna]]
        matriz_jugadas[fila][columna]=0
        lista_btns[fila][columna].configure(text='')
        lista_btns2=lista_btns[:]
        matriz_jugadas2=matriz_jugadas[:]
        jugadas_borradas+=[lista_jugadas[-1]]     
        del lista_jugadas[-1]
    else:
        messagebox.showinfo("Advertencia","No hay jugada para borrar.")

"Función que rehace las jugadas deshechas"
def rehacer():
    global matriz_jugadas
    global lista_btns
    global lista_jugadas
    global lista_btns2
    global ind_iniciado
    global jugadas_borradas
    global etiquetas_borradas
    if ind_iniciado==False:
        messagebox.showinfo("Advertencia","No se ha iniciado el juego.")
    if len(jugadas_borradas)>0:
        fila,columna=jugadas_borradas[-1]
        matriz_jugadas[fila][columna]=etiquetas_borradas[-1]
        lista_btns[fila][columna].configure(text=str(etiquetas_borradas[-1]))
        lista_btns2=lista_btns[:]
        matriz_jugadas2=matriz_jugadas[:]
        lista_jugadas+=[jugadas_borradas[-1]]
        del jugadas_borradas[-1]
        del etiquetas_borradas[-1]
    else:
        messagebox.showinfo("Advertencia","No hay jugada para rehacer.")

"Función que borra todas las jugadas"   
def borrar_juego():
    global matriz_jugadas
    global lista_btns
    global lista_jugadas
    global lista_btns2
    global ind_iniciado
    if ind_iniciado==False:
        messagebox.showinfo("Advertencia","No se ha iniciado el juego.")
    else:
        continuar=messagebox.askquestion("Advertencia","Seguro que desea borrar TODAS las jugadas?")
        if continuar=="no":
            pass
        else:
            while len(lista_jugadas)>0:
                fila,columna=lista_jugadas[-1]
                matriz_jugadas[fila][columna]=0
                lista_btns[fila][columna].configure(text='')
                lista_btns2=lista_btns[:]
                matriz_jugadas2=matriz_jugadas[:]
                del lista_jugadas[-1]
        
"Funcion que ingresa los #'s a la matriz"
def ing_matriz(a,z):
    global lista_btns
    global numero_select
    global matriz_jugadas
    global vara
    global varz
    global lista_jugadas
    if numero_select=="":
        messagebox.showinfo("Advertencia","No se ha seleccionado el número a ingresar.")
        return
    ind_presencia=False
    ind_var=True
    tupla=0
    tupla2=0
    tupla3=0
    tupla4=0
    ub_tup1=0
    ub_tup2=0
    ub_tup3=0
    ub_tup4=0
    for num2 in range(8,-1,-1):
        if isinstance(matriz_jugadas[a][num2],tuple):
            if matriz_jugadas[a][num2][1]!=0:
                tupla2=matriz_jugadas[a][num2]
                ub_tup2=num2
                break
    for num in range(0,9):
        if isinstance(matriz_jugadas[a][num],tuple):
            tupla=matriz_jugadas[a][num]
            ub_tup=num
            break
    if tupla==tupla2:
        for num in range(8,-1,-1):
            if isinstance(matriz_jugadas[a][num],tuple):
                tupla2=matriz_jugadas[a][num]
                ub_tup2=num2
                break
    if z>ub_tup2 and ub_tup2>ub_tup1:
        for pos in range(ub_tup2,9):
            if matriz_jugadas[a][pos]==numero_select:
                messagebox.showinfo("Error", "No se puede repetir el número en la fila.")
                ind_presencia=True
                break
    elif ub_tup1==ub_tup2:
        for datos_lista in matriz_jugadas[a]:
            if datos_lista==numero_select:
                messagebox.showinfo("Error", "No se puede repetir el número en la fila.")
                ind_presencia=True
                break
    elif ub_tup1<z<ub_tup2:
        for datos_lista in (ub_tup1,ub_tup2):
            if matriz_jugadas[a][datos_lista]==numero_select:
                messagebox.showinfo("Error", "No se puede repetir el número en la fila.")
                ind_presencia=True
                break
    tupla=0
    tupla2=0
    ub_tup=0
    ub_tup2=0
    for num2 in range(8,-1,-1):
        if isinstance(matriz_jugadas[num2][z],tuple):
            if matriz_jugadas[num2][z][0]!=0:
                tupla2=matriz_jugadas[num2][z]
                ub_tup=num
                break
        for num in range(0,9):
            if isinstance(matriz_jugadas[num][z],tuple):
                tupla=matriz_jugadas[num][z]
                ub_tup1=num
                break
        if tupla==tupla2:
            for num in range(8,-1,-1):
                if isinstance(matriz_jugadas[num][z],tuple):
                    tupla2=matriz_jugadas[num][z]
                    ub_tup2=num2
                    break
        #print(a,ub_tup2,ub_tup1)
        if a>ub_tup2 and ub_tup2>ub_tup1:
            for pos in range(ub_tup2,9):
                if matriz_jugadas[pos][z]==numero_select:
                    messagebox.showinfo("Error", "No se puede repetir el número en la columna. IF #1")
                    ind_presencia=True
                    break
        elif ub_tup1==ub_tup2:
            for pos in range(0,ub_tup2):
                if matriz_jugadas[pos][z]==numero_select:
                    messagebox.showinfo("Error", "No se puede repetir el número en la columna. IF #2")
                    ind_presencia=True
                    break
        elif ub_tup1<z<ub_tup2:
            for dato in range(ub_tup1,ub_tup2):
                if matriz_jugadas[pos][z]==numero_select:
                    messagebox.showinfo("Error", "No se puede repetir el número en la columna.IF #3")
                    ind_presencia=True
                    break
    if ind_presencia==False:
        vara=a
        varz=z
        lista_btns[a][z].configure(text=str(numero_select))
        matriz_jugadas[a][z]=numero_select
        lista_jugadas=lista_jugadas+[[vara,varz]]




"Función que escoge los datos de una partida para su despliegue"
def escoger_partida():
    import random
    global contenido
    abrir_config=open("kakuro2018configuración.dat",'r')
    dificultad=abrir_config.readline()
    dificultad=eval(dificultad)
    dificultad=dificultad[0]
    abrir_partidas = open("kakuro2018partidas.txt",'r')
    cont=0
    if dificultad=="1 Neurona" or dificultad=="Multinivel":
        while cont!=1:
            contenido=abrir_partidas.readline()
            cont+=1
    elif dificultad=="2 Neuronas":
        while cont!=2:
            contenido=abrir_partidas.readline()
            cont+=1
    elif dificultad=="3 Neuronas":
        while cont!=3:
            contenido=abrir_partidas.readline()
            cont+=1
    contenido=eval(contenido)
    contenido=random.choice(contenido)
    abrir_partidas.close()
    return contenido


"Función que habilita los botones del tablero"
def iniciar_partida():
    import threading
    global lista_btns
    global ind_iniciado
    global btn_empezar    
    for a in range(0,9):
        for b in range(0,9):
            if lista_btns[a][b]!='#/#':
                lista_btns[a][b].config(state='normal')
    ind_iniciado=True
    funcreloj=threading.Thread(name='Hilo_Reloj',target=iniciar_tiempo)
    funcreloj.start()
    
"Función que inicia el tiempo"
def iniciar_tiempo():
    global tiempo_total
    abrir_config=open("kakuro2018configuración.dat",'r')
    tiempo_contador=abrir_config.readline()
    tiempo_contador=eval(tiempo_contador)
    timer=tiempo_contador[2]
    tiempo_contador=tiempo_contador[1]
    if tiempo_contador=="Timer":
        reloj(tiempo_contador,timer)
    else:
        timer=0
        reloj(tiempo_contador,timer)
        return
    
"Función que lleva el tiempo de juego"
def reloj(ind_tiempo,cont):
    global juegoraiz
    global relojframe
    import time
    listanums=['1','2','3','4','5','6','7','8','9','0']
    copy_cont=cont
    if ind_tiempo=="Sí":
        cont=0
        while cont<=10799:
            time.sleep(1)
            cont+=1
            horas=cont//3600
            cont=cont%3600
            mins=cont//60
            seg=cont%60
            if str(horas) in listanums:
                horas="0"+str(horas)
            else:
                horas=str(horas)
            if str(mins) in listanums:
                mins="0"+str(mins)
            else:
                mins=str(mins)
            if str(seg) in listanums:
                seg="0"+str(seg)
            else:
                seg=str(seg)
            tiempo_var=horas+":"+mins+":"+seg
            Label(relojframe,text=tiempo_var,font=('Console',20),bg="grey").grid(row=0,column=0)
        messagebox.showinfo("Tiempo","Se ha terminado el tiempo permitido.")
    elif ind_tiempo=="No":
        pass
    else:
        while cont>0:
            time.sleep(1)
            cont-=1
            horas=cont//3600
            cont=cont%3600
            mins=cont//60
            seg=cont%60
            if str(horas) in listanums:
                horas="0"+str(horas)
            else:
                horas=str(horas)
            if str(mins) in listanums:
                mins="0"+str(mins)
            else:
                mins=str(mins)
            if str(seg) in listanums:
                seg="0"+str(seg)
            else:
                seg=str(seg)
            tiempo_var=horas+":"+mins+":"+seg
            print(tiempo_var)
        continuar=messagebox.askquestion("Tiempo","Se ha terminado el tiempo permitido. Desea continuar jugando?")
        if continuar=="no":
            juegoraiz.destroy()

"Función que solicita al usuario donde desea que se inicie el Timer"
def caso_timer():
    global horas
    global dig1minutos
    global dig2minutos
    global dig2segundos
    global dig1segundos
    timerraiz=Tk()
    timerraiz.geometry("550x500+100+100")
    timerraiz.title("Configuración del Timer")
    timerraiz.config(bg="red")
    lista_dig1=["0",
                "1",
                "2",
                "3",
                "4",
                "5"]
    lista_dig2=["0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9"]
    lista_horas=["00",
                 "01",
                 "02"]
    #Controla las horas del timer
    Label(timerraiz,text="Seleccione las horas que desea:",font=("Console",10),bg="red").place(x=15,y=15)
    horas=StringVar()
    btn_horas=OptionMenu(timerraiz,horas,*lista_horas).place(x=220,y=15)

    #Controla los minutos del timer
    Label(timerraiz,text="Seleccione los minutos que desea:",font=("Console",10),bg="red").place(x=15,y=70)
    dig1minutos=StringVar()
    btn_dig1minutos=OptionMenu(timerraiz,dig1minutos,*lista_dig1).place(x=225,y=70)
    dig2minutos=StringVar()
    btn_dig2minutos=OptionMenu(timerraiz,dig2minutos,*lista_dig2).place(x=275,y=70)

    #Controla los segundos del timer
    Label(timerraiz,text="Seleccione los segundos que desea:",font=("Console",10),bg="red").place(x=15,y=125)
    dig1segundos=StringVar()
    btn_dig1segundos=OptionMenu(timerraiz,dig1segundos,*lista_dig1).place(x=235,y=125)
    dig2segundos=StringVar()
    btn_dig2segundos=OptionMenu(timerraiz,dig2segundos,*lista_dig2).place(x=285,y=125)

    #Boton que guarda la configuración del Timer
    btn_aceptar=Button(timerraiz,text="Aceptar",command=lambda:aceptar_timer()).place(x=200,y=200)

def aceptar_timer():
    global horas
    global dig1minutos
    global dig2minutos
    global dig2segundos
    global dig1segundos
    global tiempo_total
    horas=horas.get()
    minutos=dig1minutos.get()+dig2minutos.get()
    segundos=dig1segundos.get()+dig2segundos.get()
    if horas=="":
        horas="0"
    if minutos=="":
        minutos="0"
    if segundos=="":
        segundos="0"
    tiempo_total=int(horas)*3600+int(minutos)*60+int(segundos)
        
    
    

"Función que extrae la bandera del número, que después será asigada a los botones del tablero"
def ind_num(num):
    global numero_select
    global num_select
    if num==1:
        numero_select=1
    elif num==2:
        numero_select=2
    elif num==3:
        numero_select=3
    elif num==4:
        numero_select=4
    elif num==5:
        numero_select=5
    elif num==6:
        numero_select=6
    elif num==7:
        numero_select=7
    elif num==8:
        numero_select=8
    elif num==9:
        numero_select=9
    num_select.set(numero_select)
    
"Función que guarda la partida en curso"
def guardar_partida():
    global matriz_jugadas
    global lista_btns
    global contenido
    global juegoraiz
    strcontenido=str(contenido)
    strmatriz=str(matriz_jugadas)
    strbtns=str(lista_btns)
    borra=open('kakuro2018juegoactual.dat','w')
    borra.close()
    f=open('kakuro2018juegoactual.dat','a')
    f.write(strcontenido+'\n'+strmatriz+'\n'+strbtns)
    f.close()
    continuar=messagebox.askquestion("Advertencia","Desea continuar con la partida?")
    if continuar=="no":
        juegoraiz.destroy()
        
        

"Función que despliega la pantalla de configuración, donde el usuario seleccionará la dificultad y la forma en que se mida el tiempo"    
def configuracion():
    global dificultad
    global tiempo
    global menu_tiempo
    global menu_dificultad
    #Crea la raiz y le da algunas caracteristicas
    confraiz=Tk()
    confraiz.geometry("550x500+100+100")
    confraiz.title("Opciones")

    #Crea el frame y le da algunas caracteristicas
    confframe=Frame(confraiz)
    confframe.pack()
    confframe.config(bg="red")
    confframe.config(width="550",height="500")

    #Lista de niveles de dificultad
    niveles=["1 Neurona",
             "2 Neuronas",
             "3 Neuronas",
             "Multinivel"]

    #Lista de opciones para controlar el tiempo
    reloj=["Sí",
           "No",
           "Timer"]

    #Crea las etiquetas del frame
    Label(confframe,text="Opciones",
          bg="red",fg="white",font=("Times",40)).place(x=175,y=25)
    Label(confframe, text="Seleccione la dificultad:", bg="red",
          font=("Arial",15)).place(x=75,y=125)
    Label(confframe, text="Reloj:", bg="red",
          font=("Arial",15)).place(x=75,y=200)

    #Crea el menú de selección de dificultad
    dificultad=StringVar(confframe)
    menu_dificultad=OptionMenu(confframe,dificultad,*niveles).place(x=290,y=125)

    #Crea el menú de selección de controlador del tiempo
    tiempo=StringVar(confframe)
    menu_tiempo=OptionMenu(confframe,tiempo,*reloj).place(x=135,y=200)

    #Crea el boton encargado de guardar los datos de configuracion
    Button(confframe,text="Guardar",font=("Arial",15),command=lambda:guardar_conf()).place(x=200,y=300)
    
    confraiz.mainloop()

"Función guardar_conf, que guarda los datos de la pantalla 'Opciones' en un archivo de texto, que se usarán a la hora de jugar"
def guardar_conf():
    global dificultad
    global tiempo
    nivel=dificultad.get()
    reloj=tiempo.get()
    f=open("kakuro2018configuración.dat","w")
    if nivel=="1 Neurona" and reloj=='Sí':
        f.write("['1 Neurona','Sí','0']")
    elif nivel=="1 Neurona" and reloj=='No':
        f.write("['1 Neurona','No','0']")
    elif nivel=="1 Neurona" and reloj=='Timer':
        f.write("['1 Neurona','Timer','0']")
    elif nivel=="2 Neuronas" and reloj=='Sí':
        f.write("['2 Neuronas','Sí','0']")
    elif nivel=="2 Neuronas" and reloj=='No':
        f.write("['2 Neuronas','No','0']")
    elif nivel=="2 Neuronas" and reloj=='Timer':
        f.write("['2 Neuronas','Timer','0']")
    elif nivel=="3 Neuronas" and reloj=='Sí':
        f.write("['3 Neuronas','Sí','0']")
    elif nivel=="3 Neuronas" and reloj=='No':
        f.write("['3 Neuronas','No','0']")
    elif nivel=="Multinivel" and reloj=='Sí':
        f.write("['Multinivel','Sí','0']")
    elif nivel=="Multinivel" and reloj=='No':
        f.write("['Multinivel','No','0']")
    elif nivel=="1 Neurona" and reloj=='Timer':
        f.write("['Multinivel','Timer','0']")
    else:
        f.write("['3 Neuronas','Timer']")
    f.close()

"Función acerca, que muestra información sobre el programa"
def acerca():
    #Crea la raiz y le da algunas características básicas
    acerca=Tk()
    acerca.title("Acerca de")
    acerca.geometry("600x240+100+100")
    acerca.resizable(False,False)
    acerca.config(bg="blue")
    #Crea las etiquetas que se muestran en la raíz acerca
    Label(acerca,text="Nombre del Programa: Kakuro v2.0.py",
          bg="blue",fg="white",font=("Times",25),justify="left").place(x=10,y=10)
    Label(acerca,text="Autor: Gerald Calvo P.",
          bg="blue",fg="white",font=("Times",25),justify="left").place(x=10,y=130)
    Label(acerca,text="Versión: 1.0.",
          bg="blue",fg="white",font=("Times",25),justify="left").place(x=10,y=70)
    Label(acerca,text="Fecha de Creación: 13/04/2018.",
          bg="blue",fg="white",font=("Times",25),justify="left").place(x=10,y=190)



    acerca.mainloop()

"Función salir, que cierra el programa"
def salir():
    menuraiz.destroy()

"Función ayuda, que abre el manual de usuario del programa"
def ayuda():
    import os
    os.startfile("manual_de_usuario_kakuro.pdf")


#Programa Principal
#Crea la matriz que vaya guardando las jugadas
matriz_jugadas2=[]

#Crea las listas para asignar a los botones y labels
lista_btns2=[]

#Crea la etiqueta que llevaran los botones
numero_select=''

#Crea la lista de jugadas que se hayan realizado en la partida
lista_jugadas=[]

#Variable que indica si el juego se ha iniciado
ind_iniciado=False

#Variables usadas para guardar las jugadas que se han borrado
etiquetas_borradas=[]
jugadas_borradas=[]

#Crea la raiz y le da algunas características básicas
menuraiz=Tk()
menuraiz.title("Menú Principal")
menuraiz.config(bg="green")
menuraiz.resizable(False,False)

num_select=StringVar()

#Crea el frame y le da algunas características básicas
menuframe=Frame()
menuframe.pack()
menuframe.config(bg="red")
menuframe.config(width="550",height="500")


#Crea el mensaje del menú principal
Label(menuframe,text="Kakuro",\
      bg="red",fg="white",font=("Times",40)).place(x=215,y=25)

#Crea los botones del menú principal
Button(menuframe,text="Jugar",font=("Arial",15),command=juego,
       width=33).place(x=100, y=150)
Button(menuframe,text="Configuración",font=("Arial",15),
       command=configuracion,width=33).place(x=100, y=206)
Button(menuframe,text="Ayuda",font=("Arial",15),width=33,\
       command=ayuda).place(x=100, y=262)
Button(menuframe,text="Acerca de",font=("Arial",15),width=33,\
       command=acerca).place(x=100, y=318)
Button(menuframe,text="Salir", font=("Arial",15),width=33,\
       command=salir).place(x=100, y=374)

#Mantiene el menú principal abierto
menuraiz.mainloop()
