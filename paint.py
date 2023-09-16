from turtle import *

from freegames import vector
#Vamos a utilizar el package de freegames, el cual contiene "Paint", necesario para la actividad.

def line(start, end): #Define "line"
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
# Lo que line hace es agarrar la posicion x/y del primer click del mouse, y luego moverse a la segunda posicion
# dejando una linea del color seleccionado.

def square(start, end): #Define "square"
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill() #end fill indica cuando se rellenara la figura
# Similar a line, utilizara la distancia entre los 2 clicks para crear un cuadrado.
# En este caso, por 4 ciclos, recorrera la distancia dada, luego girara 90 grados a la izquierda. Asi dando nuestro cuadrado.

def circle(start, end): #Añadimos la funcion para crear un circulo de tamaño predeterminado
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(180): #Va correr 180 veces, avanzara 2 puntos y luego girara 2 grados. 
        forward(2)
        left(2)
    end_fill()
    pass  # TODO


def rectangle(start, end): #Añadimos la funcion para crear un rectangulo, el cual sus lados verticales seran la mitad del valor dado paralos horizontales
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.x/2 - start.x/2)
        left(90)
    end_fill()
    
    pass  # TODO


def triangle(start, end): #Funcion para triangulo, avanza una distancia indicada, luego gira 120 grados
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()
    pass  # TODO


def tap(x, y): #Tap se quedara con el valor inicial de la figura dibujada.
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0) #Le damos un tamaño a nuestro canvas.
onscreenclick(tap)
listen()
#onkey hace que cuando una tecla sea presionada, tal accion suceda. Ya sea cambiar color o hacer figuras.
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O') #Added orange color - FJBG
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()