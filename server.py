# Imports
from flask import Flask, render_template, request
import json

# Initializing the App
app = Flask(__name__)


# Routing
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<file_name>')
def hello(file_name=None):
    if '.html' in file_name:
        return render_template(file_name)


def append_data_to_file(data_dict, file_path='./database/messages.json'):
    # file_path = './database/messages.json'
    with open(file_path, 'r+') as file:
        data = file.read()
        file.seek(0)
        messages = json.loads(data)
        messages.append(data_dict)
        data_updated = json.dumps(messages)
        file.write(data_updated)
    return data_updated


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        this_data = request.form.to_dict()
        data_updated = append_data_to_file(this_data)

        return data_updated
