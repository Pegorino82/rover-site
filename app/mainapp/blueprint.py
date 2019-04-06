from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from mainapp.forms import ActionForm
import socket
import json

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    form = ActionForm(request.form)

    client = socket.socket()
    client.connect(('127.0.0.1', 8080))

    if request.method == 'POST':
        data = {key: val for key, val in request.form.items() if not key.startswith('csrf')}
        json_data = json.dumps(data).encode('utf-8')
        client.send(json_data)
    return render_template('mainapp/index.html', form=form)


@main.route('/action', methods=['GET', 'POST'])
def action():
    client = socket.socket()
    client.connect(('127.0.0.1', 8080))

    data = request.json

    print(data)
    client.send(json.dumps(data).encode('utf-8'))
    return jsonify(**{'status': 'ok'})
