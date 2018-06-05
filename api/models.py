#create class for
class a_request:
    def __init__(self, _id, _request, _type):
        self._request = _request
        self._type = _type
        self._id = _id
    
    def get_id(self):
        return self._id
    
    def get_request(self):
        return self._request

    def get_type(self):
        return self._type

    def get_dict(self):
        return{'_id':self._id,
        '_type':self._type,
        '_request':self._request}


maintance_requests = [
a_request('1', 'computer not working','repair')
]
#create class for users
class a_user:
    def __init__(self, _id, _username, _password):
        self._id = _id
        self._username = _username
        self._password = _password
    
    def get_id(self):
        return self._id
    
    def get_username(self):
        return self._username

    def get_password(self):
        return self._password





user_list = [
a_user('1','rachaelN','123abc')
   
]