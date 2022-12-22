from flask import Flask
#Si el archivo es el archivo principal del proyecto, la variable sera __name__ con valor __main__ caso contrario sera None
app = Flask(__name__)
#patron de diseño de software (Singleton)

# Un decorador se usa con el @ , sirve para modificar cierto método de una clase pero sin la necesidad de modificar el funcionamiento natural (es una modificación parcial) se crea una nueva función que será la nueva funcionalidad del metodo
@app.route('/')
def inicio():
 return 'Hola desde mi servidor de Flask!!!'

 #debug > cada vez que modifiquemos el codigo y guardemos, se reiniciara el servidor
app.run(debug=True)