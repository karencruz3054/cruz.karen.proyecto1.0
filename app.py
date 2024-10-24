from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ruta principal para mostrar el formulario
@app.route("/")
def index():
    return render_template("Index.html")

# Ruta para procesar el formulario y devolver los datos en JSON
@app.route('/enviar_datos', methods=['POST'])
def enviar_datos():
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    dni = request.form.get('dni')
    
    # Procesar y crear un diccionario con los datos
    datos = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni
    }

    # Devolver los datos en formato JSON
    return jsonify(datos)

@app.route("/Alumnos")
def alumnos():
    return render_template("Alumnos.html")

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    dni = request.form.get('dni')
    
    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni
    }
    
    return jsonify(datos)

@app.route("/Cursos")
def cursos():
    return render_template("Cursos.html")

# Ruta para procesar la inscripción al curso
@app.route('/inscribirse', methods=['POST'])
def inscribirse():
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    dni = request.form.get('dni')
    email = request.form.get('email')
    curso = request.form.get('cursos')

    # Crear un diccionario con los datos
    datos_inscripcion = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "email": email,
        "curso": curso
    }

    # Retornar los datos en formato JSON
    return jsonify(datos_inscripcion)

# Ruta para la página de Profesores
@app.route('/Profesores')
def profesores():
    return render_template('Profesores.html')

# Ruta para procesar el formulario de contacto
@app.route('/enviar_mensaje', methods=['POST'])
def enviar_mensaje():
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    dni = request.form.get('dni')

    # Crear un diccionario con los datos
    datos_formulario = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni
    }

    # Retornar los datos en formato JSON
    return jsonify(datos_formulario)




if __name__ == '__main__':
    app.run(debug=True)

