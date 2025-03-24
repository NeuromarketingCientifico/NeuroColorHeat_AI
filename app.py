from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  

# Login básico
users = {"usuario": "password123"}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("map"))
        else:
            return "Usuario o contraseña incorrectos"
    return render_template("login.html")

@app.route("/map")
def map():
    if "username" in session:
        return render_template("map.html")
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
