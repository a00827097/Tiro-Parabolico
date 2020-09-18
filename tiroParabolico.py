from random import randrange
from turtle import *
from freegames import vector
#se importan las librerias de freegames y turtle

#se definen las variables para los vectores de posicion y velocidad
ball = vector(-200, -200)
speed = vector(0, 0)
targets = [] #vector vacio para meter los datos de los targets

def tap(x, y):
    "Respond to screen tap."
    #funcion para identificar la posicion y velocidad según donde de click el usuario
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    #funcion para verfificar que el click del usuario este dentro de la pantalla/el juego
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    #funcion que dibuja los puntitos
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    #funcion que determina el movimiento de las pelotas y el proyectil
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

#como se mueven las pelotas a traves de la pantalla
    for target in targets:
        target.x -= 0.5

#simula la gravedad del proyectil
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

#para detectar la colision del proyectil con las pelotas
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()



    ontimer(move, 50)

#se llama a las funciones ya establecidas
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()