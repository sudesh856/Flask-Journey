from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/hello')

def hello():
    response = make_response("HEY\n")
    response.status_code = 202
    response.headers['content-type'] = 'this is customized '
    response.headers['date'] = 'we dont know yet'
    return response


# @app.route('/hello', methods = ['POST', 'GET'] )
# def hey():
#     if request.method == "GET":
#         return "it's get request\n"
    
#     elif request.method == "POST":
#         return "it's post  request\n"
    
#     else:
#         return "it's get request"
    

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
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting}, {name}"

    else:
        return "Some Params are missing."


if __name__ == "__main__": 
    app.run(debug=True,)
