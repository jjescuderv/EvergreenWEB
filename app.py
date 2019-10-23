from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

tiposIndicador = ['Estrés hídrico', 'Nitrógeno foliar', 'Índice cosecha', 'Densidad volumétrica radial']

@app.route("/", methods=['GET'])
def crearIndicador():
    return render_template('formularioIndicadores.html', listaTipos = tiposIndicador)

@app.route("/listarIndicadores", methods=['GET'])
def listarIndicadores():
    indicadores_lista = requests.get('http://localhost:5000/indicadores').json()
    return render_template('listaIndicadores.html', listaIndicadores = indicadores_lista)

@app.route("/guardarIndicador", methods=['POST'])
def guardarIndicador():
    indicador = dict(request.values)
    indicador['prioridad'] = int(indicador['prioridad'])
    indicador['codigo'] = int(indicador['codigo'])
    requests.post('http://localhost:5000/indicadores', json=indicador)
    return crearIndicador()
