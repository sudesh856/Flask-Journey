from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/', methods = ['GET', 'POST'])

def index():

    if request.method == "GET":
        return render_template('index.html')
    
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "sudesh" and password == "sudesh":
            return "Success"
        
        else:
            return "Failure"
        

@app.route('/file_upload', methods = ['GET' , 'POST'])

def file_upload():
    return ""


if __name__ == '__main__':
    app.run(debug=True)