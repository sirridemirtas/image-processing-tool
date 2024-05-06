from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return {
        'message': 'Hello World'
    }

# static folder


@app.route('/')
def static_files():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
