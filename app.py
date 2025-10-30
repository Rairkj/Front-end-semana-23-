from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret')


@app.route('/')
def index():
# exemplo simples: passa uma lista para o template
items = ['Maçã', 'Pera', 'Banana']
return render_template('index.html', items=items)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
if request.method == 'POST':
name = request.form.get('name', 'Mundo')
return redirect(url_for('greet', name=name))
return render_template('layout.html')


@app.route('/greet/<name>')
def greet(name):
return f"<h1>Olá, {name}!</h1>"


if __name__ == '__main__':
# usa variáveis de ambiente para host/port em produção
host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
port = int(os.getenv('FLASK_RUN_PORT', 5000))
debug = os.getenv('FLASK_DEBUG', '1') == '1'
app.run(host=host, port=port, debug=debug)
