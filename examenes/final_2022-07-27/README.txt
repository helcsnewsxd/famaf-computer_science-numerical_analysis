DATOS DEL ALUMNO:

	APELLIDO --> Herrador
	NOMBRE 	 --> Emanuel Nicolás
	DNI		 --> 44898601


README EN SÍ:

	El presente documento va a realizar una explicación de lo que se presenta en el final de
laboratorio de análisis numérico I del 27/07/2022.

	Los documentos que se presentan son los siguientes:

 - Documento principal   --> Final.py
 - Documentos axiliares  --> Integrales.py
							 Biseccion.py
							 Graficos.py
 - Documento explicativo --> README.txt

y cada uno tiene el siguiente contenido:

 - Final.py --> Contiene los ejercicios (1a), (1b) y (1c) resueltos y para que salgan en pantalla
				las respuestas cuando se ejecuta el archivo

 - Integrales.py --> Contiene la función intenumcomp que recibe una función, un intervalo, la cantidad
					 de subintervalos a considerar y la regla con la que se va a aproximar; y devuelve
					 la aproximación obtenida de calcular la regla con esos parámetros.

 - Biseccion.py --> Contiene la función rbisec que recibe una función, un intervalo, una cota de error y
					una cota de iteraciones; y devuelve todos los puntos generados por el método de 
					Bisección para calcular la raíz de la función, hasta que se cumpla algunas de las
					propiedades de corte.

 - Graficos.py --> Contiene la función graphic que recibe varios conjuntos de números con sus conjuntos
				   de valores asociados, los nombres con los que se va a describir cada conjunto, el
				   nombre del gráfico, una variable booleana que establece si se va a mostrar el gráfico,
				   el número de la figura a mostrar y un arreglo de booleanos que marcan si los conjuntos
				   de puntos van a mostrarse unidos mediante rectas o como puntos separados. Luego, esta
				   función no devuelve ningún valor pero realiza el gráfico con las condiciones recibidas.

 - README.txt --> Contiene una explicación breve de los archivos presentados en este final.


	Luego, por último, para no tener que recurrir a los comentarios de Final.py para poder ver la justificación
de por qué se usó bisección en el ejercicio (1b), se va a poner a continuación:

		Notemos que int_1^x (1/y)dy = [ln(y)]_1^x = ln(y)-ln(1) = ln(y)
		Luego, entonces buscamos la raíz de f(x) = ln(y) - 1, la cual es continua en (0,inf)
		Por ello, como [2,4] está en (0,inf), f(2)*f(4) < 0 y se cumplen las condiciones de continuidad para la
		aplicación del método de bisección, sabemos que este va a converger a la solución por Teorema.

	Además, se aclara que el gráfico presentado en el ejercicio (1c) NO contiene la representación de
integral_simpson(x) para x en [1,8], sino que contiene la de f(x) = integral_simpson(x)-1. Esto se debe
a que se consultó durante el exámen qué se prefería ya que no quedaba lindo que los puntos de bisección
no estuvieran sobre alguna curva de función, y se permitió realizar este cambio.

---------------------------------------------------------- FIN ----------------------------------------------
