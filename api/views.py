from flask import Flask, request, jsonify,abort, Blueprint
import json
from api.models import a_request, a_user
from api.models import maintance_requests, user_list
import jwt
import datetime
import uuid
from werkzerg.security import generate_password_hash, check_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = "nanana"

my_app = Blueprint('my_app',__name__)

    
#create a new request
@my_app.route('/api/v1/users/requests' ,methods= ['POST'])
def create_request():

    """
        This endpoint creates a maintance request ticket
    """
   
    data = request.get_json()
   
    _requests = data.get('requests'),
    if not _requests or _requests == '':
        return jsonify ({'message': 'Missing information. Please fill in'}), 400
    _types = data.get('type')
    if not _types or _types =='':
         return jsonify ({'message': 'Missing infor Please fill in'}), 400
   
    try:
        if isinstance(data['requests'], str) and isinstance(data['type'], str):
            id = len(maintance_requests)
            id += 1 
            Request =a_request(id,data['requests'],data['type'] )
            maintance_requests.append(Request)  
        return jsonify(Request.get_dict()), 201
    #Add an Attribut error to catch the errors
    except AttributeError:
        return jsonify({
            'status': 'FAIL',
            'message': 'Failed to create a request. Invalid data'
        }), 400

#create an api endpoint for modifying requests
@app.route('/api/v1/users/requests/<id>' ,methods= ['PUT'])
def modify_request(id):
    data = request.get_json()
    """
    This endpoint modifies a request 
    """
    _requests = data.get('requests'),
    _types = data.get('type')
    if not _requests or _requests == ' ':
        return jsonify ({'message': 'Missing information. Please fill in'}), 400
    _types = data.get('type')
    if not _types or _types ==' ':
         return jsonify ({'message': 'Missing infor Please fill in'}), 400
  
    
    #try:
    if isinstance(data['requests'], str) and isinstance(data['type'], str):
        counter = 0
    for item in maintance_request:
        if id == item.get_id():
            maintance_request[counter]
        return
        counter = counter +1
        a_request('id', 'request','type'),200
#except AttributeError, IndexError):
        return jsonify({
            'status': 'FAIL',
            'message': 'Failed to modify a request. Invalid data'
        }), 400

#create API endpoints for fetching all requests
@app.route('/api/v1/users/requests',methods= ['GET'])
def fetch_all_requests():
    count = len(maintance_requests) 
  


    return jsonify({
        'status': 'OK',
        'message': 'here are all your requests',
        'request_number': count,
        'requests': maintance_requests

    }), 200

#create API endpoints for fecthind a single id
@app.route('/api/v1/users/requests/<requestID>/', methods = ['GET'])
def fetch_request_id(requestID):
    fetch_requests = []
    data = maintance_requests
    if int(requestID) > len(data):
        return jsonify({
            'status':'Fail',
            'message':'ID not found. Please add a valid ID'

        }),400
    obj = data[int(requestID)-1]
    fetch_requests.append(obj)

    return jsonify({
        'status':'Success',
        'request':fetch_requests
    })

@app.route('/auth/login', methods = ['POST'])
def user_login():
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'username': request.get_json()["username"]
        }
        token = jwt.encode(payload,app.config.get('SECRET_KEY'),algorithm='HS256')
        return jsonify({"token":token.decode('UTF-8')})
    except Exception as e:
        return e


@app.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User (public_id =str(uuid.uuid4()), name=data ['name'],password,admin=False)   


# @auth.get_password
# def get_password():
#     if 'username' == [user_list]['username']:
#         return 'python'
#     return None

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Unauthorized access'}), 401)



    