from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/formularios_guardados')
def formularios_guardados():
    return render_template('formularios_guardados.html')

if __name__ == '__main__':
    app.run(debug=True)