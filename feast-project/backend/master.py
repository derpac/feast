# I enjoy a comment preamble for all my code... This file will act as the master for the backend in the finite element analysis solver tool (FEAST). Initially i will use script and/or file input for problem init

# from flask import Flask, request, jsonify
# import os
# from fea_s import input, solve_fea


# app = Flask(__name__)
# upload_folder = 'problem-upload'
# app.config['upload_folder'] = upload_folder
# os.makedirs(upload_folder, exist_ok=True)

# @app.route('/upload', methods=['POST'])  # accept file input in .msh file format for normal users
# def upload_file():
#     file = request.files['file']
#     path = os.path.join(app.config['upload_folder'],file.filename)
#     file.save(path)

#     nodes, elements = input(path)
#     results = solve_fea(nodes, elements)

#     return jsonify(results)

# @app.route('/submit', methods=['POST'])   # accept script input for nodes and elements for uber nerds
# def submit_data():
#     data = request.get_json()
#     nodes = data['nodes']
#     elements = data['elements']

#     results = solve_fea(nodes, elements)

#     return jsonify(results)

# if __name__ == '__main__':
#     app.run(debug=True)


# after talking to someone about linux i decided i would change the backend of the code for this project, where before data was parsed through script and file input i will now change the methodology to accept json file to allow
# to be implemented more easily with other apps.

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from fea_s import run_fea

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def handle_upload():
    file = request.files['file']
    data = json.load(file)
    displacements = run_fea(data)
    return jsonify({'displacements': displacements})

if __name__ == '__main__':
    app.run(debug=True)
#-----------------