from flask import Flask
from flask import request , jsonify
import db_connector
import queries
import sys
import json

db = db_connector.DataProvider('KLAZE.db')
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/status', methods=['POST'])
def post_status():
    DATA= json.loads(request.data)
    if(DATA is None):
        return 400
    else:
        hostname = DATA['hostname']
        try:
            db.execute(queries.insert_new_status.format(HOSTNAME=hostname , DATA = json.dumps(DATA)), cursor = db.get_cursor())
            return 'OK',200
        except:
            return sys.exc_info()[0],500

@app.route('/status/<ID>', methods = ['GET'])
def get_status(ID):
    try:
        data = db.execute(queries.get_latest_status.format(HOSTNAME = ID) , cursor = db.get_cursor())    
        
        return jsonify(json.loads(data[0][0]))
    except:
        return sys.exc_info()[0] , 500


if __name__ == '__main__':
    app.run(host='prsubrama-lt')