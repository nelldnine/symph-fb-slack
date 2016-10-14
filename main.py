from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/messages', methods=['GET', 'POST'])
@app.route('/api/v1/messages/<int:id>', methods=['GET', 'POST'])
def messages(id=None):
    return 'Hello world'


@app.route('/api/v1/archive', methods=['GET', 'POST'])
def archive():
    return 'Hello world'
