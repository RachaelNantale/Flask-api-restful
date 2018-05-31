import json
import flask
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
                    'request':'fix my car', 
                    'type':'repair'
                }
            )

            response = self.client.post(
                '/users/requests', 
                content_type = 'application/json', data =json.dumps(post_data))
            reply = json.loads(response.data.decode())
            # if reply['request'] == None :
            #     return jsonify({'message': 'Please fill in a request'})
                
    
            self.assertEquals(reply['status'], 'OK')
            self.assertEquals(reply['message'], 'A new request has been created')
            self.assertEquals(response.status_code, 201 )

    # #fetch request id for a logged in user
    # def test_fetch_id(self):
    #     with self.client:
    #         post_data = ({'name':'lakeli', 'username':'seada'})
    #         response = self.client.get('/users/requests/requestID', content_type = 'application/json', data =json.dumps(post_data))
    #         reply = json.loads(response.data.decode())
    #         self.assertEquals(reply['name'],'lakeli' )
    
    #modify a request
    def test_modify_request(self):
            
         with self.client:
                post_data = (
                    {
                        'request':'#123', 
                        'type':'this is a request'})
                response = self.client.put('/users/requests/1',data=  json.dumps(post_data) ,
                content_type = 'application/json',)
                reply = json.loads(response.data.decode())  
                
                self.assertEquals(reply['status'], 'OK')
                self.assertEquals(reply['message'], 'A Request has been modified')
                self.assertEquals(response.status_code, 201 )

    
    #fetch all requests
    def test_fetch_all_requests(self):
        with self.client:
            post_data = (
                {
                    'request':'lakeli', 
                    'type':'seada'})
            response = self.client.get('api/v1/users/requests', 
            content_type = 'application/json', data =json.dumps(post_data))
            reply = json.loads(response.data.decode())

            self.assertEquals(reply['status'], 'OK')
            self.assertEquals(reply['message'], 'here are all your requests')
            self.assertEquals(response.status_code, 201 )



    #fetch single id
    def test_fetch_single_id(self):
        with self.client:
            post_data = (
                {
                    'request':'lakeli', 
                    'type':'seada'})
            response = self.client.get('users/requests/1', 
            content_type = 'application/json', data =json.dumps(post_data))
            reply = json.loads(response.data.decode())

            self.assertEquals(reply['status'], 'OK')
            self.assertEquals(reply['message'], 'here is your request')
            self.assertEquals(response.status_code, 201 )

        








if __name__ == '__main__':
    app.run(debug=True)