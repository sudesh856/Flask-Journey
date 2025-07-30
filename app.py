from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def index():
    return '<h1> Hello World </h1>'

@app.route('/greet/<name>')

def greet(name):
    return f"hello {name}"

@app.route('/add/<number1>/<number2>')

def add(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    return f"{number1} + {number2} = {number1+number2}"    


@app.route('/handle_url_params')
def handle_url_params():
    return str(request.args)



if __name__ == "__main__":
    app.run(debug=True)
