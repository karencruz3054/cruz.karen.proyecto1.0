from flask import Flask,render_template

app = Flask("Proyecto-Web-Python")

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/Profesores")
def profesores():
    return render_template("Profesores.html")


@app.route("/Alumnos")
def alumnos():
    return render_template("Alumnos.html")


@app.route("/Cursos")
def cursos():
    return render_template("Cursos.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port='5000')