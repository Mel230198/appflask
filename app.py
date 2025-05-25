from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, mundo! Flask rodando no Render!'
