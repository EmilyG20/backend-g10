from flask import Flask, request
from flask_cors import CORS
#Si el archivo es el archivo principal del proyecto, la variable sera __name__ con valor __main__ caso contrario sera None
app = Flask(__name__)
# ahora configuramos el CORS (Control de acceso de recursos cruzados)
CORS(app=app, origins=['http://127.0.0.1:5500'], methods=['GET','POST'])
#patron de diseño de software (Singleton)
usuarios = [
 {
  'nombre' : 'Eduardo',
  'apellido': 'Juarez'
 },
 {
  'nombre' : 'Juana',
  'apellido': 'Rodriguez'
 },
 {
  'nombre' : 'Roberto',
  'apellido': 'Castillo'
 }
]
# Un decorador se usa con el @ , sirve para modificar cierto método de una clase pero sin la necesidad de modificar el funcionamiento natural (es una modificación parcial) se crea una nueva función que será la nueva funcionalidad del metodo
@app.route('/')
def inicio():
 return 'Hola desde mi servidor de Flask!!!'

@app.route("/mostrar-hora", methods=['Get','POST'])
def mostrarHora():
 #Controlador > funcionalidad que se realiza dentro de un determinado endpoint
 print(request.method)
 if request.method == 'GET':
  return {
   'content': 'Me hiciste GET'
  }
 elif request.method == 'POST':
  return {
   'content': 'Me hiciste POST'
  }
 #No se suele retornar strings sino diccionarios
 return {
  'content': '22:50:15'
 }

@app.route("/usuarios", methods=['GET','POST'])
def gestionUsuario():
 if request.method == 'GET':
  return {
   'message': 'Los usuarios son:',
   'content': usuarios
  }
 elif request.method == 'POST':
  # agregar un nuevo usuario
  print(request.get_json())
  data = request.get_json()
  usuarios.append(data)
  return {
   'message': 'Usuario agregado exitosamente'
  }


 #debug > cada vez que modifiquemos el codigo y guardemos, se reiniciara el servidor
app.run(debug=True)