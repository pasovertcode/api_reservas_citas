from flask import Flask, jsonify

app = Flask(__name__)

# Configurando app
app.secret_key = 'secret_key'

# Configurando/registrando rutas
from app.routes import usuarios_routes
app.register_blueprint(usuarios_routes, url_prefix='/usuarios')