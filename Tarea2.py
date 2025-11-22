import estructura
from lista import *
from random import *
from funcional import *

#Funciones para crear y validar estructuras

#(a) Item: nombre(str) peso(int) valor(int)
estructura.crear("Item","nombre peso valor")

#(b) Bolsillo: orientacion(str) lista(Item)
estructura.crear("Bolsillo","orientacion listaItem")

#(c) Mochila: pesoMaximo(int) lista(Bolsillo)
estructura.crear("Mochila","pesoMaximo listaBolsillo")

#(c') Cosas para los ejemplos
item1 = Item("rubi", 4, 5)
item2 = Item("oro", 1, 3)
item3 = Item("cristal", 2, 2)
listaEjemplo1 = lista(item1, listaVacia)
listaEjemplo2 = lista(item2, lista(item3, listaVacia))
bolsillo1 = Bolsillo("izq", listaEjemplo1)
bolsillo2 = Bolsillo("der", listaEjemplo2)
listaEjemploBV = lista(Bolsillo("izq", listaVacia), listaVacia)
listaEjemploB = lista(bolsillo1, lista(bolsillo2, listaVacia))
mochilaEjemplo = Mochila(25, listaEjemploB)
mochilaEjemplo2 = Mochila(1, listaEjemploB)

#(d) esItem: Item -> bool
#Recibe un parametro I y entrega True si corresponde
#a un Item valido o False en caso contrario.
#Ejemplo: esItem(item1) entrega True
def esItem(I):
	if type(I) != Item:
		return False
	if type(I.nombre) != str or type(I.peso) != int or type(I.valor) != int:
		return False
	return True
#Test
assert esItem(item1)
assert esItem(item2)

#(e) esBolsillo: Bolsillo -> bool
#Recibe un parametro B y entrega True si corresponde
#a un Bolsillo valido o False en caso contrario.
#Ejemplo: esBolsillo(bolsillo1) entrega True
def esBolsillo(B):
	if type(B) != Bolsillo:
		return False
	if type(B.orientacion) != str or type(B.orientacion) != str or esLista(B.listaItem) == False:
		return False
	else:   return True
#Test
assert esBolsillo(bolsillo1)
assert esBolsillo(bolsillo2)

#(f) esMochila: Mochila -> bool
#Recibe un parametro M y entrega True si corresponde
#a una Mochila valida o False en caso contrario.
#Ejemplo: esMochila(mochilaEjemplo) entrega True
def esMochila(M):
	if type(M) != Mochila:
		return False
	if type(M.pesoMaximo) != int or not(esLista(M.listaBolsillo)):
		return False
	return True
#Test
assert esMochila(mochilaEjemplo)
assert not esMochila(Mochila("cinco", 1234))

#(g) crearItem: str int -> Item
#Recibe un string y un entero y entrega un Item con el nombre dado 
#y su peso y valor generados aleatoriamente.
#Ejemplo: crearItem("tarea", 25) entrega Item("tarea", int(randint(1, 25/3), int(randint(1, 25/4))
def crearItem(nombre, pesoMaximo):
	assert type(nombre) == str
	peso = int(randint(1, pesoMaximo/3))
	valor = int(randint(1, pesoMaximo/4))
	return Item(nombre, peso, valor)
#Test
itemI = crearItem("tarea", 25)
assert itemI.nombre == "tarea"
assert 1 <= itemI.peso <= 8
assert 1 <= itemI.valor <= 6
itemII = crearItem("tarea2", 20)
assert itemII.nombre == "tarea2"
assert 1 <= itemII.peso <= 6
assert 1 <= itemII.valor <= 5

#(h) crearBolsillos: int int -> lista(Bolsillo)
#Recibe dos enteros que representan la cantidad de bolsillos que se quieren crear
#y entrega una lista de bolsillos con i bolsillos izquierdos y d bolsillos derechos.
#Ejemplo: crearBolsillos(1, 0) entrega lista(Bolsillo("izq", listaVacia), listaVacia)
def crearBolsillos(i, d):
        assert type(i) == int and type(d) == int
        assert i >= 0 and d >= 0
        BolsilloIzquierdo = Bolsillo("izq", listaVacia)
        BolsilloDerecho = Bolsillo("der", listaVacia)     
        if i == 0 and d == 0:
                return listaVacia
        elif i != 0:
                return lista(BolsilloIzquierdo, crearBolsillos(i-1,d))
        elif d != 0:
                return lista(BolsilloDerecho, crearBolsillos(i,d-1))
#Test
assert crearBolsillos(1, 0) == lista(Bolsillo("izq", listaVacia), listaVacia)
assert crearBolsillos(0, 0) == listaVacia

#(i) crearMochila: int lista(Bolsillo) -> Mochila
#Recibe un entero que representa el peso maximo que soportara
#la mochila y una lista de Bolsillos, entrega una mochila.
#Ejemplo: crearMochila(25, listaEjemploB) entrega Mochila(25, listaEjemploB)
def crearMochila(pesoMax, Lbolsillos):
	assert type(pesoMax) == int
	return Mochila(pesoMax, Lbolsillos)
#Test
assert crearMochila(25, listaEjemploB) == Mochila(25, listaEjemploB)
assert crearMochila(1, listaEjemploB) == Mochila(1, listaEjemploB)

#Funciones que operan con las estructuras

#(a) contarBolsillos: lista(Bolsillo) -> int
#Recibe una lista de Bolsillos y entrega la cantidad
#total de Bolsillos que hay en la lista.
#Ejemplo: contarBolsillos(listaEjemploB) entrega 2
def contarBolsillos(listaBolsillos):
	assert esLista(listaBolsillos) == True
	return largo(listaBolsillos)
#Test
assert contarBolsillos(listaEjemploB) == 2
assert contarBolsillos(listaVacia) == 0

#(b) filtrarBolsillosPorOrientacion: lista(Bolsillo) str -> lista(Bolsillo)
#Dada una lista de Bolsillos y una orientacion, devuelve una lista con
#todos los Bolsillos que poseen la orientacion dada.
#Ejemplo: filtrarBolsillosPorOrientacion(listaEjemploB, "izq") entrega bolsillo1
def filtrarBolsillosPorOrientacion(listaBolsillos, orientacion):
	assert esLista(listaBolsillos) == True and (orientacion == "izq" or orientacion == "der")
	return filtro(lambda x: x.orientacion == orientacion, listaBolsillos)
#Test
assert filtrarBolsillosPorOrientacion(listaEjemploB, "izq") == lista(bolsillo1, listaVacia)
assert filtrarBolsillosPorOrientacion(listaEjemploB, "der") == lista(bolsillo2, listaVacia)

#(c) sumarItems: lista(Item) str -> int
#Recibe una lista de Items y el string "p" o "v". En caso "p", entrega el peso
#total de los Items. En caso "v", entrega el valor total de los Items.
#Ejemplo: sumarItems(listaEjemplo2, "p") entrega 3
def sumarItems(listaItems, tipo):
	assert esLista(listaItems) == True and (tipo == "p" or tipo == "v")
	if listaItems == listaVacia:    return 0
	elif tipo == "p":
		listaPesoItems = mapa(lambda x: x.peso, listaItems)
		return fold(lambda x, y: x + y, 0, listaPesoItems)
	elif tipo == "v":
		listaValorItems = mapa(lambda x: x.valor, listaItems)
		return fold(lambda x, y: x + y, 0, listaValorItems)
#Test
assert sumarItems(listaEjemplo2, "p") == 3
assert sumarItems(listaEjemplo2, "v") == 5

#(d) sumarTotalBolsillos: lista(Bolsillo) str -> int
#Dado una lista de bolsillos y un string "p" o "v", retorna la suma de 
#todos los pesos o valores de los items que estan en la lista de bolsillos.
#Ejemplo: sumarTotalBolsillos(listaEjemploB, "p") entrega 7
def sumarTotalBolsillos(listaBolsillos, t):
	assert esLista(listaBolsillos) == True and (t == "p" or t == "v")
	listaDeListaItems = mapa(lambda x: x.listaItem, listaBolsillos)
	if listaDeListaItems == listaVacia:
		return 0
	else:
		return sumarItems(cabeza(listaDeListaItems), t) + sumarTotalBolsillos(cola(listaBolsillos), t)
#Test
assert sumarTotalBolsillos(listaEjemploB, "p") == 7
assert sumarTotalBolsillos(listaEjemploB, "v") == 10

#(e) agregarItem: lista(Bolsillo) Item int -> lista(Bolsillo)
#Recibe una lista de Bolsillos, un Item y un entero. Entrega una lista de
#Bolsillos, en donde se agregó el Item al n-esimo Bolsillo de la lista.
#Ejemplo: agregarItem(listaEjemploBV, item1, 1) entrega lista(Bolsillo("izq", lista(Item("rubi", 4, 5), listaVacia)), listaVacia)
def agregarItem(listaBolsillos, I, n, c=1):
	assert esLista(listaBolsillos) == True and esItem(I) == True and n >= 1
	bolsilloActual = cabeza(listaBolsillos)
	if n == c:
		nuevaL = lista(I, bolsilloActual.listaItem)
		return lista(Bolsillo(bolsilloActual.orientacion, nuevaL), cola(listaBolsillos))
	else:
		return lista(bolsilloActual, agregarItem(cola(listaBolsillos), I, n, c+1))
#Test
assert agregarItem(listaEjemploBV, item1, 1) == lista(Bolsillo("izq", lista(Item("rubi", 4, 5), listaVacia)), listaVacia)
assert agregarItem(listaEjemploBV, item2, 1) == lista(Bolsillo("izq", lista(Item("oro", 1, 3), listaVacia)), listaVacia)
		
#(f) listarItems: lista(Item) -> str
#Recibe una lista de Items, y entrega un string
#con todos los Items presentes en la lista.
#Ejemplo: listarItems(listaEjemplo1) entrega "rubi(4Kg 5UF)"
def listarItems(listaItems):
	assert esLista(listaItems) == True
	if listaItems == listaVacia:
		return ""
	else:
		itemActual = cabeza(listaItems)
		return (str(itemActual.nombre)+"("+str(itemActual.peso)+"Kg"+" "+str(itemActual.valor)+"UF)"+" "+str(listarItems(cola(listaItems)))).strip()
#Test
assert listarItems(listaEjemplo1) == "rubi(4Kg 5UF)"
assert listarItems(listaEjemplo2) == "oro(1Kg 3UF) cristal(2Kg 2UF)"

#(g') mostrarLBolsillo: lista(Bolsillo) -> None
#Recibe una lista de Bolsillo y muestra su contenido
def mostrarLBolsillo(listaBolsillos, n=1):
	assert esLista(listaBolsillos) == True
	if listaBolsillos == listaVacia:
		return ""
	else:
		bolsilloActual = cabeza(listaBolsillos)
		if bolsilloActual == listaVacia:
			print ""
		else:
			print "Bolsillo"+str(n)+"("+bolsilloActual.orientacion+")"+":"+" "+listarItems(bolsilloActual.listaItem)
			mostrarLBolsillo(cola(listaBolsillos), n+1)

#(g) mostrarBolsillos: Mochila -> None
#Recibe una Mochila y muestra en pantalla el contenido de la mochila.
def mostrarBolsillos(M):
	assert esMochila(M) == True
	listaBolsillos = M.listaBolsillo
	mostrarLBolsillo(listaBolsillos)
	
#(h) balanceada: Mochila -> bool
#Recibe una Mochila y entrega True si está balanceada y False si no.
#Ejemplo: balanceada(mochilaEjemplo) entrega True
def balanceada(M):
	assert esMochila(M) == True
	listaBolsillos = M.listaBolsillo
	Izquierdos = filtrarBolsillosPorOrientacion(listaBolsillos, "izq")	
	Derechos = filtrarBolsillosPorOrientacion(listaBolsillos, "der")
	pesoIzquierdos = sumarTotalBolsillos(Izquierdos, "p")
	pesoDerechos = sumarTotalBolsillos(Derechos, "p")
	if abs(pesoIzquierdos - pesoDerechos) >  int(M.pesoMaximo*0.25):
		return False
	else:
		return True
#Test
assert balanceada(mochilaEjemplo) == True
assert balanceada(mochilaEjemplo2) == False

#Funciones Interactivas Principales

#iniciarPrograma: None -> None
#muestra un mensaje inicial, pregunta al usuario(a) por el peso maximo de la mochila y
#la cantidad de bolsillos izquierdos y derechos que tendra.
def iniciarPrograma():
	print "Rick & Morty Homecoming: hora de llenar la mochila y volver a casa."
	pesoMax = input("Ingrese peso maximo de la mochila: ")
	derechos = input("Ingrese cantidad de bolsillos derechos: ")
	izquierdos = input("Ingrese cantidad de bolsillos izquierdos: ")
	assert type(pesoMax) == int and pesoMax >= 10
	assert type(izquierdos) == int and izquierdos >= 1
	assert type(derechos) == int and derechos >=1
	M = Mochila(pesoMax, crearBolsillos(izquierdos, derechos))
	return cicloPrincipal(M)

#cicloPrincipal: Mochila -> None
#Se encarga de mostrar un mensaje dando a conocer las 3
#acciones que podemos realizar sobre la mochila,
def cicloPrincipal(M):
	print "Acciones disponibles:"
	print "1- Agregar Item a la mochila"
	print "2- Listar elementos de la mochila"
	print "3- Atravesar portal"
	numAccion = input("Ingrese N de accion: ")
	if numAccion == 1:
		nombreItem = raw_input("Ingrese nombre del item: ")
		pesoMaximo = M.pesoMaximo
		nuevoItem = crearItem(nombreItem, pesoMaximo)
		print "De acuerdo a la IGN, este item tiene: "
		print str(nuevoItem.peso)+"kg de peso y "+str(nuevoItem.valor)+"UF de valor"
		respUser = raw_input("Ingresar este item a la mochila? ")
		if respUser == "Si":
			nbItem = input("Ingrese bolsillo al cual se ingresara el item("+"1-"+str(contarBolsillos(M.listaBolsillo))+"): ")
			nuevaM = Mochila(M.pesoMaximo, agregarItem(M.listaBolsillo, nuevoItem, nbItem, c=1))
			if balanceada(nuevaM) == False:
				print "Item agregado, pero la mochila ha quedado desbalanceada y ha explotado."
				print "Todos han muerto, fin del programa :("
				return None
			else:
				print "Item agregado exitosamente"
				print ""
				return cicloPrincipal(nuevaM)
		elif respUser == "no":
			print "Item no agregado"
			return cicloPrincipal(M)
	elif numAccion == 2:
		mostrarBolsillos(M)
		izquierdos = filtrarBolsillosPorOrientacion(M.listaBolsillo, "izq")	
		derechos = filtrarBolsillosPorOrientacion(M.listaBolsillo, "der")
		print "Peso Total:"+""+str(sumarTotalBolsillos(M.listaBolsillo, "p"))+"Kg"
		print "Felicidad Total:"+" "+str(sumarTotalBolsillos(M.listaBolsillo, "v"))+"UF"
		print "Balance(izq-der):"+" "+str(sumarTotalBolsillos(izquierdos, "p"))+"Kg"+" "+"-"+" "+str(sumarTotalBolsillos(derechos, "p"))+"Kg"
		print ""
		return cicloPrincipal(M)
	elif numAccion == 3:
		print "Hora de atravesar el portal..."
		if sumarTotalBolsillos(M.listaBolsillo, "v") <= 23:
			print "Han llegado sanos y salvos a casa, congrats ;D"
			print "Felicidad Total:"+" "+str(sumarTotalBolsillos(M.listaBolsillo, "v"))+"UF"
			return None
		else:
			print "Han sido interceptados por la Federacion Intergalactica por superar el limite de Unidades de Felicidad permitidas"
			print "La mochila ha sido requizada y nuestros heroes terminan en una prision intergalactica"
			return None

#FIN
iniciarPrograma()