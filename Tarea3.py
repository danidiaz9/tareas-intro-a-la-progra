alfabeto = ' 1234567890abcdefghijklmnopqrstuvwxyz'

#Funciones de mensajeria

#(a) posicionAlfa: str -> int
#Recibe string que representa un caracter
#entrega posicion del caracter en el alfabeto.
#Ejemplo: posicionAlfa("j") entrega 20
def posicionAlfa(S):
	assert type(S) == str
	posicion = alfabeto.index(S)
	return posicion
#Test
assert posicionAlfa("j") == 20
assert posicionAlfa("8") == 8

#(b) posicionEscalera: str int int int -> str
#Recibe texto y 3 enteros: n, i y j .Primero convierte el string en escaleras de n peldaños
#retorna el caracter en la escalera i, habiendo bajado j peldaños.
#Ejemplo: posicionEscalera("muy secreto", 3, 2, 2) entrega "s"
def posicionEscalera(texto, n, i, j):
	assert type(texto) == str
	assert type(n) == int
	assert type(i) == int
	assert type(j) == int
	ListaTexto = list(texto)
	LargoTexto = len(list(texto))
	posiC = ListaTexto[(LargoTexto/n)*(i-1)+(j-1)]
	return posiC

#Test
assert posicionEscalera("muy secreto", 3, 2, 2) == "s"
assert posicionEscalera("hola", 2, 1, 2) == "o"

#(c) crearLlave: str str -> str
#Recibe string  que representa un mensaje y un string que representa la llave original
#entrega string con la llave repetida cíclicamente hasta tener el largo del mensaje.
#Ejemplo: crearLlave("muy secreto", "gato") entrega "gatogatogat"
def crearLlave(msg, llave):
	assert type(msg) == str and type(llave) == str
	repeticiones = 1
	while len(msg) > len(llave):
		repeticiones += 1
		llave = llave*repeticiones
		resto = (len(llave) - len(msg))
	return llave[:-resto]
#Test
assert crearLlave("muy secreto", "gato") == "gatogatogat"
assert crearLlave("realmente secreto", "hola") == "holaholaholaholah"

#(d) agregarRuido: str str -> str
#Recibe string msg que representa un mensaje y string que representará el ruido
#entrega como resultado el mensaje al cual se le agrego el ruido.
#Ejemplo: agregarRuido("muy secreto", "gato") entrega "muy gatosecrgatoeto"
def agregarRuido(msg, ruido):
	assert type(msg) == str and type(ruido) == str
	assert len(ruido) <= len(msg)/2
	LmsgResto = []
	ListaTexto = list(msg)
	ListaRuido = list(ruido)
	LargoR = len(ruido)
	ContadorR = 0	
	CantidadR = len(ListaTexto)/len(ListaRuido)
	while ContadorR < CantidadR:
		for i in range(LargoR):
			LmsgResto.append(ListaTexto.pop(0))
		for i in range(LargoR):
			LmsgResto.append(ListaRuido[i])
		ContadorR += 1
	return "".join(LmsgResto + ListaTexto)
#Test
assert agregarRuido("muy secreto", "gato") == "muy gatosecrgatoeto"
assert agregarRuido("realmente secreto", "hola") == "realholamentholae seholacretholao"

#(e) encriptarEscalera: str int -> str
#Recibe string que representa un mensaje y entero que representa los peldaños
#entrega que representa el mensaje encriptado de acuerdo al algoritmo de Escalera.
#Ejemplo: encriptarEscalera("muy secreto", 3) entrega "m ctusroyeem"
def encriptarEscalera(msg, n):
	assert type(msg) == str and type(n) == int
	ListaMsg = list(msg)
	LargoMsg = len(list(msg))
	Encriptado = []
	i = 0
	j = 0
	if (LargoMsg % n) == 0:
		while j < n:
			i = 0
			while i < (LargoMsg/n):
				caracter = ListaMsg[(n)*(i)+(j)]
				Encriptado.append(caracter)
				i += 1
			j += 1
		return "".join(Encriptado)
	else:
		for c in range(n - (LargoMsg%n)):
			ListaMsg.append(ListaMsg[c])
		msgfix = "".join(ListaMsg)
		return encriptarEscalera(msgfix, n)
#Test
assert encriptarEscalera("muy secreto", 3) == "m ctusroyeem"
assert encriptarEscalera("realmente secreto", 4) == "rmecoee rranseelteta"

#(f) desencriptarEscalera: str int int -> str
#recibe string que representa un mensaje, n que representa peldaños y r que es la cantidad de caracteres adicionales 
#entrega un nuevo string que representa el mensaje desencriptado de acuerdo al algoritmo de Escalera.
#Ejemplo:
def desencriptarEscalera(msg, n, r):
    assert type(msg) == str
    assert type(n) == int
    assert type(r) == int
    
    ListaMsg = list(msg)
    LargoMsg = len(ListaMsg)
    Desencriptado = []
    
    # Calcular el número de elementos por peldaño
    elementos_por_peldaño = LargoMsg // n
    
    # Reconstruir el mensaje original
    i = 0
    j = 0
    while i < elementos_por_peldaño:
        j = 0
        while j < n:
            posicion = (elementos_por_peldaño * j) + i
            caracter = ListaMsg[posicion]
            Desencriptado.append(caracter)
            j += 1
        i += 1
    
    # Unir el resultado y eliminar los caracteres adicionales
    resultado = "".join(Desencriptado)
    if r > 0:
        resultado = resultado[:-r]
    
    return resultado
#Test
assert desencriptarEscalera("m ctusroyeem", 3, 0) == "muy secreto"
assert desencriptarEscalera("rmecoee rranseelteta", 4, 2) == "realmente secreto"