from flask import Flask, request, jsonify,abort
import json
from models import *

app = Flask(__name__)

#create a new request
@app.route('/api/v1/users/requests' ,methods= ['POST'])
def create_request():

    """
        This endpoint creates a maintance request ticket
    """
    # 1. get the data from request
    data = request.get_json()
   #make sure empty strings are not allowed
    _requests = data.get('requests'),
    if not _requests or _requests == '':
        return jsonify ({'message': 'Missing information. Please fill in'}), 400
    _types = data.get('type')
    if not _types or _types =='':
         return jsonify ({'message': 'Missing infor Please fill in'}), 400

     # 2. validate the data        
    try:
        if isinstance(data['requests'], str) and isinstance(data['type'], str):
            # 3. store the data
            id = len(maintance_requests) #  count how many maintance requests you have save so far
            id += 1 
        
            # req = a_request(id, data['request'], data['type'])
            requ = {
                'id':id,
                'requests':data['requests'],
                'type':data['type']
            }
            maintance_requests.append(requ)  #  Save request in the list

        return jsonify({
            'requests':requ
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
     # 1. get the data from request
    
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
    count = len(maintance_requests) #  count how many maintance requests you have save so far
    #requests = maintance_requests


    return jsonify({
        'status': 'OK',
        'message': 'here are all your requests',
        'request_number': count,
        'requests': maintance_requests

    }), 200

#create API endpoints for fecthind a single id
@app.route('/api/v1/users/requests/<requestID>', methods = ['GET'])
def fetch_request_id(requestID):
    
    data_r = [data_r2 for data_r2 in maintance_requests if data_r2['id'] == requestID ]
    if len(data_r) == 0:
        return jsonify ({"message":"Please fill in a valid ID"}), 400
    return jsonify({
        'Request information':data_r[0]
    }),200


if __name__ == '__main__':
    app.run(debug='True')
                
                