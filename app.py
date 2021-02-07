from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/note')
def note():
    return '<h1>my notes!!!</h1>'


if __name__ == '__main__':
    app.run()
