from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello World</h1>"


@app.route('/hello')
def hello():
    return "Hello World"


@app.route('/greet/<name>')

def greet(name):
    return f"hello {name}"


@app.route('/add/<number1>/<number2>')

def add(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    return f'{number1} + {number2} = {number1+number2}'


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)