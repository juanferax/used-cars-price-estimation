from flask import Flask, jsonify, render_template, Response, request
from flask_cors import CORS
from predictor import client_predict

app = Flask(__name__,
            static_folder='../frontend/dist/static',
            template_folder='../frontend/dist')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')

# This method receives car data sent from the frontend and returns the price preticted by model
@app.route('/api/v1.0/estimateCarPrice', methods=['POST'])
def estimateCarPrice():
    try:
        if request.method == "POST":
            response = request.get_json()

            labelsList = ["brand", "kilometers", "model", "motor", "transmission", "year"]
            data = []
            data.append(response["brand"])
            data.append(float(response["kilometers"]))
            data.append(response["model"])
            data.append(float(response["motor"]))
            data.append(response["transmission"])
            data.append(int(response["year"]))

            # price formatting: ' indicates millions
            price = str(client_predict(data))
            price_split = price.split(".")
            price_split[0] = price_split[0][:-6] + "'" + price_split[0][-6:]
            price = price_split[0] + "." + price_split[1]

            return jsonify(str(price))
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})

# In order to run the backend server write the following command:
# python server.py
if __name__ == "__main__":
    app.run(debug=True)