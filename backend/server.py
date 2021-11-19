from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__,
            static_folder='../frontend/dist/static',
            template_folder='../frontend/dist')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
 
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')

@app.route('/api/v1.0/message')
def message():
    return jsonify('Nuevo mensaje desde el backend')

# In order to run the backend server write the following command:
# python server.py
if __name__ == "__main__":
    app.run(debug=True)