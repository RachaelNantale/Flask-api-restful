from flask import Flask, request, jsonify,abort, Blueprint
import json
from api.models import maintance_requests, user_list
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
app = Flask(__name__)

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
            Request = {
                'id':id,
                'requests':data['requests'],
                'type':data['type']
            }
            maintance_requests.append(Request)  
        return jsonify({
            'requests':Request
        }), 201
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
        maintance_requests[int(id)-1]['requests'] = data['requests'] #references a parameter in the dictionary 
        maintance_requests[int(id)-1]['type'] = data['type']

        return jsonify({
            'status': 'OK',
            'request': maintance_requests[int(id)-1]['requests'],
            'message': 'A Request has been modified',
            'request_id': id
            
        }), 200
#except AttributeError, IndexError):
    else:
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
    
    # data_r = [data_r2 for data_r2 in maintance_requests if data_r2['id'] == requestID ]
    # if len(data_r) == 0:
    #     return jsonify ({"message":"Please fill in a valid ID"}), 400
    # return jsonify({
    #     'Request information':data_r[0]
    # }),200

# @app.route('/api/v1/auth/register', methods = ['POST'])

#@app.route('/api/v1/auth/login', methods = ['POST']

# @auth.get_password
# def get_password():
#     if 'username' == [user_list]['username']:
#         return 'python'
#     return None

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Unauthorized access'}), 401)



    