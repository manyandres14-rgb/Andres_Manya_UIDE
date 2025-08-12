from turtle import Screen, Turtle
import time


def up():   #asignamos funciones para el movimiento de la serpiente hacia arriba 
 New_segment.setheading(90)
 New_segment.forward(20)
def down():   #asignamos funciones para el movimiento de la serpiente hacia abajo
 New_segment.setheading(270)
 New_segment.forward(20)
def left():   #asignamos funciones para el movimiento de la serpiente hacia la derecha 
 New_segment.setheading(180)
 New_segment.forward(20)
def right():   #asignamos funciones para el movimiento de la serpiente hacia la izquierda
 New_segment.setheading(0)
 New_segment.forward(20)
#Pantalla se asigna la interfaz grafica y el color de la pantalla 
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)   #asignamos el tamaño de la pantalla o interfaz grafica
screen.title("Snake Game Andres Manya UIDE")


#Serpiente 
New_segment = Turtle("square") #asignamos una variable el cual va a ser el inicio de la serpiente y la forma 
New_segment.color("white") #asignamos el color de la serpiente 
New_segment.penup()  #se asigna esta funcion para que no trace la direccion en la que se mueve la serpiente 
New_segment.goto(0, 0) #se define el rango de movimiento de la serpiente 
screen.onkey( up,"Up") #definimos la funcion para poder tener el control del movimiento hacia arriba de la serpiente 
screen.onkey( down,"Down")
screen.onkey( left,"Left")
screen.onkey( right,"Right")
screen.listen()
#for i in range(10): #asiganmos el bucle for para el movimiento de la serpiente 
#     New_segment.forward(20) #se mueve 20mpx hacia la derecha por default 
#     time.sleep(0.9) #se define el tiempo de latencia de movimiento 
screen.exitonclick() #Configura para que con un click salga de la pantalla de juego 
