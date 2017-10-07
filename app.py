from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#route mascotas

@app.route('/aves')
def mostrar_aves():
    return render_template('/mascotas/aves/aves.html')

@app.route('/tortugas')
def mostrar_tortugas():
    return render_template('/mascotas/tortugas/tortugas.html')

@app.route('/peces')
def mostrar_peces():
    return render_template('/mascotas/peces/peces.html')

@app.route('/reptiles')
def mostrar_reptiles():
    return render_template('/mascotas/reptiles/reptiles.html')

@app.route('/conejos')
def mostrar_conejos():
    return render_template('/mascotas/conejos/conejos.html')

#route productos

@app.route('/jaulas')
def mostrar_jaulas():
    return render_template('/productos/jaulas/jaulas.html')

@app.route('/peceras')
def mostrar_peceras():
    return render_template('/productos/peceras/peceras.html')

@app.route('/alimento')
def mostrar_alimento():
    return render_template('/productos/alimento/alimento.html')

@app.route('/accesorios')
def mostrar_accesorios():
    return render_template('/productos/accesorios/accesorios.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
