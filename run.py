from flask import Flask, request, jsonify
import json
from models import *

app = Flask(__name__)

#create a new request
@app.route('/users/requests' ,methods= ['POST'])
def create_request():

    """
        This endpoint creates a maintance request ticket
    """
    # 1. get the data from request
    data = request.get_json()
    # 2. validate the data
    try:
        if isinstance(data['request'].encode(), str) and isinstance(data['type'].encode(), str):
            # 3. store the data
            id = len(maintance_requests) #  count how many maintance requests you have save so far
            id += 1 
            req = a_request(id, data['request'], data['type'])
            maintance_requests.append(req)  #  Save request in the list

            return jsonify({
                'status': 'OK',
                'message': 'A new request has been created',
                'request id': id
            }), 201
    #Add an Attribut error to catch the errors
    except AttributeError:
        return jsonify({
            'status': 'FAIL',
            'message': 'Failed to create a request. Invalid data'
        }), 400

#create an api endpoint for modifying requests
@app.route('/users/requests/<id>' ,methods= ['PUT'])
def modify_request(id):
     # 1. get the data from request
    
    data = request.get_json()
    """
        This endpoint modifies a request 
    """
    # 2. validate the data
    try:
        if isinstance(data['request'].encode(), str) and isinstance(data['type'].encode(), str):
            # 3. store the data
#            id = len(maintance_requests) #  count how many maintance requests you have save so far
#            id += 1 
            maintance_requests[int(id)-1].request = data['request'].encode() #references a parameter in the dictionary 
            maintance_requests[int(id)-1].type = data['type'].encode()

            return jsonify({
                'status': 'OK',
                'request': maintance_requests[int(id)-1].request,
                'message': 'A request has been modified',
                'request_id': id
                
            }), 201
    except (AttributeError, IndexError):
        return jsonify({
            'status': 'FAIL',
            'message': 'Failed to modify a request. Invalid data'
        }), 400


#create API endpoints for fetching all requests
@app.route('/api/v1/users/requests',methods= ['GET'])
def fetch_all_requests():
    count = len(maintance_requests) #  count how many maintance requests you have save so far
    requests = maintance_requests
    return jsonify({
        'status': 'OK',
        'message': 'here are all your requests',
        'request_number': count,
        'requests':[json.dumps(a_request.__dict__) for a_request in requests]

    }), 201

#create API endpoints for fecthind a single id
@app.route('/users/requests/<requestID>', methods = ['GET'])
def fetch_request_id(requestID):
    try:
        #add the first code cause its unicode and we want the in
        if  isinstance(int(requestID), int): 
            return jsonify({
                'status': 'OK',
                #'requests': [json.dumps(maintance_requests[int(requestID)])],
                'type': maintance_requests[int(requestID)].get_type,
                'request':maintance_requests[int(requestID)].get_request,                
                'message': 'here is your message',
                'request_id': requestID
            }), 201
    except AttributeError:
        return jsonify({
            'status': 'FAIL',
            'message': 'Failed to modify a request. Invalid data'
        }), 400





if __name__ == '__main__':
    app.run(debug='True')
                
                