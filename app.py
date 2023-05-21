from flask import Flask, render_template, request

app = Flask(__name__)

db = ['Martin', 'Monse', 'Luli', 'Gissela', 'Nancy', 'Lujan']

@app.route("/")
def homepage():
    return render_template("index.html", nombres = db)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form['user']
        password =  request.form['pass']
        print(usuario)
        print(password)
    return render_template("login.html")

@app.route("/info")
def info():
    nombre = "Penguin Academy"
    descripcion = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    vision = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

    return render_template("info.html", nombre = nombre, descripcion = descripcion, vision = vision, nombres = db)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)