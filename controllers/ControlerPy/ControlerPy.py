"""ControlerPy controller."""

# You may need to import some classes of the controller module. Ex:
from controller import Robot, Motor, DistanceSensor, Keyboard
from controller import Robot
import random
# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

#Iniciar teclado

kb = Keyboard()
kb.enable(timestep)
#Iniciar motores

motor_izq = robot.getDevice("left wheel motor")
motor_der = robot.getDevice("right wheel motor")
#Configurar posición inicial

motor_izq.setPosition(float('inf'))
motor_der.setPosition(float('inf'))

#Setear velocidad inicial

motor_der.setVelocity(0.0)
motor_izq.setVelocity(0.0)


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key = kb.getKey()
    
    #Generamos ruido en cada paso
    ruido_izq = random.uniform(-0.1, 0.1)
    ruido_der = random.uniform(-0.1, 0.1)
    
    if key == ord('1'): #Linea recta
       
        motor_der.setVelocity(2.0 + ruido_der)
        motor_izq.setVelocity(2.0 + ruido_izq)
        
    elif key==ord('2'): #Circulo
    
        motor_der.setVelocity(5.0 + ruido_der)
        motor_izq.setVelocity(3.0 + ruido_izq)
        
    elif key == ord('3'): #Cuadrado
        contador = 0
        estado = "AVANZAR"
        lados_completados = 0
        pasos_avance = 150
        pasos_giro = 35
        while robot.step(timestep)!= -1:
            if lados_completados < 4:
                if estado == "AVANZAR":
                    motor_izq.setVelocity(2.0 + ruido_izq)
                    motor_der.setVelocity(2.0 + ruido_der)
                    
                    if contador >= pasos_avance:
                        estado = "GIRAR"
                        contador = 0
                elif estado == "GIRAR":
                    motor_izq.setVelocity(2.0 + ruido_izq)
                    motor_der.setVelocity(-2.0 + ruido_der)
                    
                    if contador >= pasos_giro:
                        estado = "AVANZAR"
                        contador = 0
                        lados_completados += 1
                contador += 1
            else:
                motor_izq.setVelocity(0.0)
                motor_der.setVelocity(0.0)
                break
    elif key == ord('4'): #Curva
        pasos_curva = 0
        
        while robot.step(timestep) != 1:
            motor_der.setVelocity(2.0 + ruido_der)
            motor_izq.setVelocity(1.5 + ruido_izq)
            pasos_curva += 1
            if pasos_curva >= 300: #Aproximadamente 90°
                motor_izq.setVelocity(2.0 + ruido_izq)
                motor_der.setVelocity(2.0 + ruido_der)
                break
    
    elif key == ord('5'): #Rotacion en el lugar
        motor_izq.setVelocity(2.0)
        motor_der.setVelocity(-2.0)
    
    elif key == ord('0'): #Detenerse
        motor_izq.setVelocity(0.0)
        motor_der.setVelocity(0.0)
    pass

# Enter here exit cleanup code.
