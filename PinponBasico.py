import turtle
#iniciando pantalla
ventana = turtle.Screen()
ventana.title("My pong")

# ventana.setup(600, 100)
ventana.setup(0.6, 0.5)
ventana.bgcolor("black")
ventana.tracer(1)
anchoPlayer= 6
altoPlayer=1
gameOver = True
# Definir parametros de jugadores
# definiendo Player1
player1 = turtle.Turtle()
player1.speed(2)
player1.shape("square")
player1.color("white")
player1.goto(20-ventana.canvwidth, 0)
player1.shapesize(stretch_wid=anchoPlayer,stretch_len=altoPlayer)
player1.penup()


# definiendo Player2
player2 = turtle.Turtle()
player2.speed(1)
player2.shape("square")
player2.color("blue")
player2.goto(ventana.canvwidth-20, 0)
player2.shapesize(6, 1)
player2.penup()

lineaCentral= turtle.Turtle()
lineaCentral.penup()
lineaCentral.goto(0,ventana.canvheight)
lineaCentral.pendown()
lineaCentral.color("green")
lineaCentral.goto(0,-ventana.canvheight )

pelota = turtle.Turtle()
radioPelota=10

pelota.color("red")
pelota.speed(0)
pelota.shape("circle")
pelota.shapesize((radioPelota)/10)
pelota.penup()
pelota.dx  = 3
pelota.dy  = 3

# limpiar
turtle.penup()
turtle.goto(radioPelota+1,0)
turtle.pendown()
turtle.goto(ventana.canvwidth,0)
turtle.penup()
turtle.goto(-radioPelota,0)
turtle.pendown()
turtle.goto(-ventana.canvwidth,0)


# hacer que se mueva el player1

def player1_sube():
    if player1.ycor() <= ((anchoPlayer*20)):
        y = player1.ycor()
        y+= 20
        player1.sety(y)
def player1_baja():
    if player1.ycor() >= -anchoPlayer*20:
        y = player1.ycor()
        y -= 20
        player1.sety(y)
def player2_sube():
    if player2.ycor() <= ((anchoPlayer*20)):
        y = player2.ycor()
        y+= 20
        player2.sety(y)
def player2_baja():
    if player2.ycor() >= -anchoPlayer*20:
        y = player2.ycor()
        y -= 20
        player2.sety(y)

# configurando acciones del teclado

ventana.listen()
ventana.onkeypress(player1_sube,"w")
ventana.onkeypress(player1_baja,"s")
ventana.onkeypress(player2_sube,"Up")
ventana.onkeypress(player2_baja,"Down")

while gameOver:
    ventana.update()
    pelota.setx(pelota.xcor()+pelota.dx)
    pelota.sety(pelota.ycor()+pelota.dy)
