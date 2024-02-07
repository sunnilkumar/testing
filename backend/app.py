from flask import Flask, request, jsonify, render_template,send_from_directory
from flask_cors import CORS, cross_origin


api = Flask(__name__ ,static_folder='build',static_url_path='')
cors = CORS(api)


@api.route('/profile', methods=['GET', 'POST'])
@cross_origin()
def profile():
    if request.method == 'POST':
        data = request.json
        print(data)
        return jsonify(data)
    else:
        response_body = {
            "name": "Nagato",
            "about": "Hello! I'm a full stack developer that loves python and javascript"
        }
        return jsonify(response_body)

@api.route('/')
def serve():
    return send_from_directory(api.static_folder, 'index.html')

