from flask import Flask, render_template, request, jsonify
import requests
from .service import extract_pokemon_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_pokemon_info')
def get_pokemon_info():

    url = f'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/get_pokemon')
def get_pokemon():
    name = request.args.get('name')
    url = f'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    data = response.json()
    pokemon_data = data['results'][0]['url']
    return pokemon_data




    # if pokemon_data:
    #     url = f'{pokemon_data}'
    #     response = requests.get(url)
    #     data = response.json()
    #     pokemon_info = []
    #     return data
    #     for entry in data['list']:
    #         ext_data = extract_pokemon_data(entry)
    #         pokemon_info.append(ext_data)
    #     return jsonify(pokemon_info)
    # else:
    #     return jsonify(error="!!"), 400



