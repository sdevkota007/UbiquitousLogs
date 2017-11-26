from flask import Flask, request, jsonify
from flask_cors import CORS

SECRET_KEY = "this is a secret key"

app = Flask(__name__)
CORS(app)




app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


########################################################################################3


#########################################################################################

#------------------------------------------------------------------------------------------------------------------



@app.route('/')
def home():
    return "Ubiquitous logs"



@app.route('/logs/shree', methods=['POST'])
def getdata():
    json_data = request.get_json()
    print (json_data)

    return jsonify({'msg':'success'})



if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)

