#importar la libreria de flask
from flask import Flask

#inicializar la variable app con flask
app = Flask(__name__)

#inicializar el servidor de flask
#en mac: export FLASK_APP = main.py
# en windows: set FLASK_APP = main.py

#Comando para ejecutar el servidor:
#flask --app main run

#Comando para ejecutar el servidor en otro puerto diferente, por default es el 5000
#flask --app main run -p 5002

#Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real
#flask --app main --debug run


@app.route("/hola")
def hola_mundo():
    return "Hola mundo Flask, esto es flask 1234"



#ejercicio una ruta que devuelva una lista de frutas el path seria /frutas
@app.route("/frutas")
def lista_frutas():
    list_frutas = ['Platano','Fresa','Piña','Melon','Naranja']
    return list_frutas


#ejemplo para enviar parametros en las rutas
@app.route("/nombre/<n>/apellido/<a>/edad/<int:e>")
def tunombre(n,a,e):
    return f"Eres {n} {a} y tienes {e} años"

#ejercicio2 realizar una ruta que devuelva el cuadrado de un numero dado, /numero/<parametro>
@app.route("/numero/<int:parametro>")
def cuadrado(parametro):
    return f"el cuadrado de {parametro} es: {parametro*parametro}"


#ejercicio3, realizar una ruta, que dinamicamente pueda solicitar o realizar
#operaciones de suma,resta,multiplicacion y division segun los parametros pasados en la ruta
@app.route("/operacion/<string:operacion>/<int:num1>/<int:num2>")
def operacion(operacion, num1, num2):
    if operacion == 'suma':
        resultado = num1 + num2
        return f"El resultado de la suma es: {resultado}"
    elif operacion == 'resta':
        resultado = num1 - num2
        return f"El resultado de la resta es: {resultado}"
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
        return f"El resultado de la multiplicación es: {resultado}"
    elif operacion == 'division':
        resultado = num1 / num2
        return f"El resultado de la división es: {resultado}"
    else:
        return "Operación no válida. Las opciones son: suma, resta, multiplicacion, division"
