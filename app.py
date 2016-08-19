from flask import Flask
from flask import request,redirect,render_template,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0',8000)
    app.run(debug=True)
