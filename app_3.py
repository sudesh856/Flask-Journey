from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/', methods = ['GET', 'POST'])

def index():

    if request.method == "GET":
        return render_template('index.html')
    
    elif request.method == "POST":
        return ""


if __name__ == '__main__':
    app.rub(debug=True)