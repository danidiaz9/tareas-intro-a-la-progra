from math import *
from random import *
from cerca import *
epsilon=0.000001

#FUNCIONES AUXILIARES

#(a)distancia: float float float float -> float
#Recibe dos puntos (x1,y1) y (x2,y2), calcula y
#entrega la distancia euclidiana entre ambos.
#Ejemplo: distancia(2.0, 0.0, 6.0, 4.0) entrega 5.0
def distancia(x1, y1, x2, y2):
	ejeX = x2-x1
	ejeY = y2-y1
	d = sqrt(ejeX**2 + ejeY**2)
	return round(d, 2)
#Test 
assert cerca(distancia(3.0, 0.0, 6.0, 4.0),5.0,epsilon)
assert cerca(distancia(2.0, 0.0, 14.0, 5.0),13.0,epsilon)
assert cerca(distancia(2.0, 0.0, 26.0, 7.0),25.0,epsilon)

#(b)numeroAleatorio: float float -> float
#Entrega un real aleatorio en el intervalo
#[a,b], con a < b.
#Ejemplo: numeroAleatorio(2, 6) <= 6
def numeroAleatorio(a, b):
	numero = a + (b-a)*uniform(0,1)
	return numero
#Test
assert 2 <= numeroAleatorio(2, 6) <= 6
assert 5 <= numeroAleatorio(5, 8) <= 8
assert 9 <= numeroAleatorio(9, 15) <= 15

#(c)contiguo: float float float float -> bool
#Entrega True o False, si el punto (x1, y1) se
#encuentra a una distancia <= a 2.0 del punto (x2, y2).
#Ejemplo: contiguo(2.0, 0.0, 6.0, 4.0) entrega False
def contiguo(x1, y1, x2, y2):
	if distancia(x1, y1, x2, y2) <= 2.0:
		return True
	else:
		return False
#Test
assert contiguo(2.0, 0.0, 6.0, 4.0)==False
assert contiguo(2.0, 0.0, 14.0, 5.0)==False
assert contiguo(2.0, 0.0, 26.0, 7.0)==False

#(d)distanciaAlCentro: float float -> float
#Recibe coordenadas del punto (x, y) y calcula su 
#distancia al centro de la circunferencia de radio 50.
#Ejemplo: distanciaAlCentro(6.0, 4.0) entrega 7.21
def distanciaAlCentro(x, y):
	d = sqrt(x**2 + y**2)
	return round(d, 2)  # int(10.43*10)/10
#Test 
assert cerca(distanciaAlCentro(6.0, 4.0),7.21,epsilon)
assert cerca(distanciaAlCentro(14.0, 5.0),14.87,epsilon)
assert cerca(distanciaAlCentro(26.0, 7.0),26.93,epsilon)

#(e)fueraLimites: float float -> bool
#Verifica si el punto (x, y) esta fuera o no de la
#circunferencia de radio 50.0, entrega True o False
#segun corresponda.
#Ejemplo:
def fueraLimites(x, y):
	if (x**2 + y**2) > (50.0**2):
		return True
	else:
		return False
#Test
assert fueraLimites(6.0, 4.0)==False
assert fueraLimites(14.0, 5.0)==False
assert fueraLimites(26.0, 7.0)==False

#FUNCIONES PRINCIPALES

#preguntaTesoro: None -> None
#Se encarga de preguntar al usuario por coordenadas
#para colocar el tesoro inicial.
#Ejemplo preguntaTesoro() y comienzan las preguntas
def preguntaTesoro():
	xt = input("Ingrese coordenada X del tesoro")
	yt = input("Ingrese coordenada Y del tesoro")
	if fueraLimites(xt, yt)==True:
		print "Coordenadas no-validas, vuelva a ingresar datos!"
		return preguntaTesoro()
	else:
		return cicloJuego(0.0, 0.0, xt, yt)

#cicloJuego: float float float float -> None
#Recibe las coordenadas actuales de nuestros
#protagonistas y el tesoro.
#Ejemplo:cicloJuego(xp=0.0, yp=0.0, xt, yt) desarrolla
#el juego mediante indicaciones
def cicloJuego(xp, yp, xt, yt):
	distanceT = distancia(xp, yp, xt, yt)
	print "Estas a "+str(distanceT)+" metros del tesoro"
	distanceP = distanciaAlCentro(xp, yp)
	print "Estas a "+str(distanceP)+" metros del centro de la dimension"
	direc = raw_input("Direccion?")
	dist = input("Distancia?")
	if direc=="arriba":
		yp = yp + dist
	if direc=="abajo":
		yp = -yp + dist
	if direc=="derecha":
		xp = xp + dist
	if direc=="izquierda":
		xp = -xp + dist	
	if fueraLimites (xp, yp)==True: 
		print "Estas a "+str(distanceT)+" metros del tesoro"
		print "Estas a "+str(distanciaAlCentro(xp,yp))+" metros del centro de la dimension"
		print "Has salido de la zona segura de la dimension! Bird Person los ha salvado"
		Newxt = numeroAleatorio(-50.0, 50.0)
		Newyt = numeroAleatorio(-(sqrt(50**2 - Newxt**2)), (sqrt(50**2 - Newxt**2)))
		return cicloJuego(0.0, 0.0, Newxt, Newyt)
	elif contiguo(xp, yp, xt,yt)==True:
		print "Has encontrado el tesoro!"
		seguirJugando = raw_input("Deseas jugar en otra dimension? [si|no]")
		if seguirJugando=="si":
			Newxt = numeroAleatorio(-50.0, 50.0)
			Newyt = numeroAleatorio(-(sqrt(50**2 - Newxt**2)), (sqrt(50**2 - Newxt**2)))
			return cicloJuego(0.0, 0.0, Newxt, Newyt)
		elif seguirJugando=="no":
			print "Rick & Morty le agradecen su ayuda!"
			return None
	else:
		return cicloJuego(xp, yp, xt, yt)

#iniciarJuego: None -> None
#Muestra mensaje de bienvenida.
#Ejemplo: iniciarJuego() muestra mensaje
def iniciarJuego():
	print "Hora de Buscar Tesoros Interdimensionales!"
	return preguntaTesoro()

#FIN#
iniciarJuego()
