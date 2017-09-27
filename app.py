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

#route productos

@app.route('/peceras')
def mostrar_peceras():
    return render_template('/productos/peceras.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
