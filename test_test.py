import json
import flask
from flask import jsonify
from run import app
from flask_testing import TestCase

#import requests

class Tests_Maintance_API(TestCase):

    def create_app(self):
        return app

    #create a request
    def test_create_request(self):
        with self.client:
            post_data = (
                {
                    'requests':'fix my car', 
                    'type':'repair'
                }
            )

            response = self.client.post(
                '/api/v1/users/requests', 
                content_type = 'application/json', data =json.dumps(post_data))
            reply = json.loads(response.data.decode())
            if reply['requests'] == None :
                return jsonify({'message': 'Please fill in a request'})
                
    
            # self.assertEquals(reply['status'], 'OK')
            # self.assertEquals(reply['message'], 'A new request has been created')
            self.assertEquals(response.status_code, 201 )
    
    # #modify a request
    def test_modify_request(self):
            
         with self.client:
                post_data = (
                    {
                        'requests':'#123', 
                        'type':'this is a request'
                        }
                    )
                response = self.client.put('/api/v1/users/requests/1', data= json.dumps(dict(post_data)) ,
                content_type = 'application/json')
                
                reply = json.loads(response.data.decode())  
                
                self.assertEquals(reply['status'], 'OK')
                self.assertEquals(reply['message'], 'A Request has been modified')
                self.assertEquals(response.status_code, 200 )

    
    # # #fetch all requests
    def test_fetch_all_requests(self):
        with self.client:
            
            response = self.client.get('api/v1/users/requests', 
            content_type = 'application/json')
            reply = json.loads(response.data.decode())

            self.assertEquals(reply['status'], 'OK')
            self.assertEquals(reply['message'], 'here are all your requests')
            self.assertEquals(response.status_code, 200 )



    #fetch single id
    def test_fetch_single_id(self):
        with self.client:  
            response = self.client.get('/api/v1/users/requests/1', 
            content_type = 'application/json')
            reply = json.loads(response.data.decode())
            self.assertEquals(response.status_code, 200 )

        








if __name__ == '__main__':
    app.run(debug=True)