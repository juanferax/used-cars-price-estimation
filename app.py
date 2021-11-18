from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'This is the about endpoint'

# In order to run the backend server write the following command:
# python server.py
if __name__ == "__main__":
    app.run(debug=True)