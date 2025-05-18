# I enjoy a comment preamble for all my code... This file will act as the master for the backend in the finite element analysis solver tool (FEAST). Initially i will use script and/or file input for problem init

# after talking to someone about linux i decided i would change the backend of the code for this project, where before data was parsed through script and file input i will now change the methodology to accept json file to allow
# to be implemented more easily with other apps.

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from fea_s import run_fea

app = Flask(__name__)
CORS(app, resources={r"/upload": {"origins": "*"}}, supports_credentials=True)

@app.route('/upload', methods=['POST', 'OPTIONS'])
def handle_upload():
    if request.method == 'OPTIONS':
        # define explicitly the response headers to try and please CORS
        response = app.make_default_options_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        return response

    # fix for CORS error 405 ---
    file = request.files['file']
    data = json.load(file)
    displacements = run_fea(data)
    response = jsonify({'displacements': displacements})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)
#-----------------