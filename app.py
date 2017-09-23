from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aves')
def mostrar_aves():
    return render_template('/aves/aves.html')

@app.route('/peceras')
def mostrar_peceras():
    return render_template('/productos/peceras.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
