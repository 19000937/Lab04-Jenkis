from flask import Flask  
app = Flask(__name__)  

@app.route('/')  
def hello():  
    return "SSe realizo con exito el laboratorio #4. Si sale este mensaje es que Jenkis y Docker funcionan a la perfeccion. :)!"  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)
