#!flask/bin/python
import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<html>
    <head>
        <title>capKopper simple-web</title>
    </head>
    <body>
        <pre>
'''+ (socket.gethostname()) +'''
        </pre>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)