import os
from flask import Flask
from flask import request

app = Flask(__name__)

#порт 9080 для локального запуска
port = int(os.getenv('PORT', '9080'))

@app.route('/')
def index():
    return {'data':'Index'}

@app.route('/places',methods=['GET'])
def places():
    return {'data':[{'Place':1},{'Place':2}]}

@app.route('/places/<placename>',methods=['GET'])
def places_params(placename):
    return {'data':placename}

@app.route('/placesnames',methods=['GET','POST'])
def places_names():
    placeid = request.args.get('placeid',default=1)
    if request.method == 'POST':
        return {'data':placeid,'POST':True}
    else:
        return {'data':placeid,'POST':False}
        
# запуск приложения
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)