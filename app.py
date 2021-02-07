from flask import Flask, render_template
import user_data

app = Flask(__name__)


@app.route('/')
def index():
    name = user_data.get_name()
    return render_template('index.html',
                           name=name)


@app.route('/note')
def note():
    return '<h1>my notes!!!</h1>'


if __name__ == '__main__':
    app.run()
