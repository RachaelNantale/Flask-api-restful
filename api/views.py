from flask import Flask, request, jsonify,abort, Blueprint, make_response
import json
from api.models import a_request, a_user
from api.models import maintance_requests, user_list
import jwt
import datetime
import uuid
from werkzeug.security import generate_password_hash
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = "nanana"

my_app = Blueprint('my_app',__name__)
#create a token header
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		if not token:
			return jsonify({'message':'Token is missing'}),401

		try:
			data =jwt.decode(token, app_config('SECRET_KEY'))
			current_user = a_user.query.filter_by(_id=data['id'])
		except:
			return jsonify({'message':'Token is missing'}),401
		return f(current_user, *args, **kwargs)
	return decorated

	
#create a new request
@my_app.route('/api/v1/users/requests' ,methods= ['POST'])
@token_required

def create_request(current_user):

	"""
		This endpoint creates a maintance request ticket
	"""
	if not current_user.admin:
		return jsonify({'message: User can not collect all requests'})
	
   
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
@token_required

def modify_request(id, current_user):
	if not current_user.admin:
		return jsonify({'message: User can not collect all requests'})
	
	
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
@token_required

def fetch_all_requests(current_user):
	if not current_user.admin:
		return jsonify({'message: User can not collect all requests'})
	

	count = len(maintance_requests) 
  


	return jsonify({
		'status': 'OK',
		'message': 'here are all your requests',
		'request_number': count,
		'requests': maintance_requests

	}), 200

#create API endpoints for fecthind a single id
@app.route('/api/v1/users/requests/<requestID>/', methods = ['GET'])
@token_required

def fetch_request_id(requestID, current_user):
	if not current_user.admin:
		return jsonify({'message: User can not collect all requests'})
	
	

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
	
@app.route('/auth/login')

def user_login():
	auth = request.authorization

	if not auth or not auth.username or not auth.password:
		return make_response('could not verify',401,{'WWW-Aunthenticate':'Basic realm="Login required"'})

	user = a_user.filter_by(name=auth.username).first()

	if not user:
		return jsonify({'message':'No user Found'})

	if check_password_hash(user.password, auth.password):
		payload = {
		'_id':'a_user._id',
		'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

		}
		token = jwt.encode({payload,app.config.get(SECRET_KEY)})
		return jsonify({'token':token.decode(UTF-8)})
	return make_response('Could not verify',401,{'WWW-Aunthenticate':'Basic realm="Login required"'})
	



@app.route('/api/v1/users', methods=['POST'])
@token_required

def create_user(current_user):
	if not current_user.admin:
		return jsonify({'message: User can not collect all requests'})
	
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	new_user = a_user(_id =str(uuid.uuid4()), name=data ['username'],password=data['hashed_password'],admin=False)   



	