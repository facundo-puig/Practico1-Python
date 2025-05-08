import requests

from flask import Flask, render_template, request
from lista_ciudades import ciudades

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        ciudades=ciudades
    )

@app.route("/clima")
def clima():
    # /clima?ciudad=Nombre
    ciudad = request.args.get("ciudad")
    lat = ciudades[ciudad]["lat"]
    lon = ciudades[ciudad]["lon"]

    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
    data = response.json()
    clima = data['current_weather']
    return render_template(
        "clima.html", ciudad=ciudad, clima=clima
    )