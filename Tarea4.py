# -*- coding: cp1252 -*-
from Tkinter import *

# ----- Inicio Clase Generador -----
# campos:
# __nombre:         str
# __costo :         int
# __genera:         int
# __cantidad:       int
# __instanciaMiner: Miner
# __labelInformacion: Label
# __BotonComprar:   Button
class Generador:

    def __init__(self, nombre, costo, genera, claseminer):
        self.nombre = nombre
        self.costo = costo
        self.genera = genera
        self.miner = claseminer
        self.actuales = 0
        self.boton = None
        self.etiqueta = None
        

    #minar: Generador -> int
    #Retorna cantidad de Kalaxian Crystals generados en un segundo.
    def minar(self):
        return self.genera*self.actuales

    #mostrar: Generador -> str
    #Retorna string con las caracteristicas de este generador.
    def mostrar(self):
        return self.nombre +"(Costo: KC$"+str(self.costo)+", Genera: "+str(self.genera)+"KC$/s): "+str(self.actuales)

    #packGenerador: Generador TKwindow -> TKwindow
    #Dada una Ventana v, crea la interfaz gráfica.
    def packGenerador(self,v):
        marco = Frame(v)
        self.boton = Button(marco, text="Comprar", command=self.comprar)
        self.etiqueta = Label(marco, text=self.mostrar())
        marco.pack()
        self.boton.pack(side=RIGHT)
        self.etiqueta.pack(side=LEFT)
        
    #actualizar: Generador -> None
    #Actualiza el texto del Label de informacion, con los datos actuales que posee este generador.
    def actualizar(self):
        self.etiqueta.config(text=self.mostrar())

    #comprar: Generador -> None
    #Compra un generador y actualiza el Label de informacion.
    def comprar(self):
        if self.miner.puede_gastar(self.costo):
            self.miner.gasta(self.costo)
            self.actuales += 1
            self.actualizar()

    #desactivar: Generador -> None
    #desactiva el boton de este generador, impidiendo que se puedan seguir comprando mas generadores.
    def desactivar(self):
        self.boton.config(state=DISABLED)



# ----- Fin Clase Generador -----

# ----- Inicio Clase Miner -----
# campos:
# __ventana:     TKwindow   
# __recursos:    int
# __tiempo:      int
# __labelInfo:   Label
# __generadores: list(Generador)
# __botonClick:  Button
class Miner:

    def __init__(self,ventana):
        self.__ventana = ventana
        self.__recursos = 10
        self.__tiempo = 0
        self.transcurrido = Label(self.__ventana)
        self.__generadores = []
        self.boton = None
        self.construir_interfaz()

    #construir_interfaz: Miner -> TKwindow
    #Construye la interfaz grafica.
    def construir_interfaz(self):
        self.actualizar()
        self.__generadores.append(Generador("Jerry", 8, 1, self))
        self.__generadores.append(Generador("Butter-Robot", 20, 3, self))
        self.__generadores.append(Generador("Meeseek", 75, 15, self))
        self.__generadores.append(Generador("Excavadora de Neutrinos", 250, 60, self))
        self.__generadores.append(Generador("Microverse", 1000, 250, self))
        self.boton = Button(self.__ventana, text="Generar 1 recurso", command=self.genera1)
        self.transcurrido.pack() 
        for generador in self.__generadores:
            generador.packGenerador(self.__ventana)
        self.boton.pack()
              
    #puede_gastar: Miner int -> bool
    #Retorna True si hay más de n recursos.
    def puede_gastar(self,n):
        return self.__recursos >= n

    #gasta: Miner int -> None
    #Gasta n recursos, descontando esa cantidad de los recursos actuales.
    def gasta(self,n):
        self.__recursos -= n
    
    #genera1: Miner -> None
    #Genera 1 recurso.
    def genera1(self):
        self.__recursos += 1
    
    #actualizar: Miner -> None
    #Actualiza el texto de informacion mostrado en el segundo Label de la ventana.
    def actualizar(self):
        self.transcurrido.config(text="Tiempo: "+str(self.__tiempo)+"s - KC$: "+str(self.__recursos))


    # step: None -> None
    # Se encarga de recolectar los recursos de los generadores
    # y aumentar el contador de tiempo, invocandose a si misma
    # repetidamente hasta que pasen 60 segundos.
    def step(self):
        # incrementa el contador de tiempo
        self.__tiempo += 1

        # Obtiene recursos de los generadores
        for generador in self.__generadores:
            self.__recursos += generador.minar()

        # Actualiza la etiqueta de información
        self.actualizar()

        # Si el tiempo es menor a 60s, entonces continua
        # si no, desactiva los botones, dando termino al juego
        if self.__tiempo < 60:
            self.__ventana.after(1000, self.step)
        else:
            for generador in self.__generadores:
                generador.desactivar()



# ----- Fin Clase Miner -----
#
# Ejecución del programa
ventana = Tk()
ventana.wm_title('R&M Kalaxian Miner')
ventana.minsize(480,180)
ventana.maxsize(480,180)

miner = Miner(ventana)
ventana.after(1000, miner.step)

ventana.mainloop()
