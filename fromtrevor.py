from flask_testing import TestCase
from run import app
import json

class MyTests(TestCase):
    
    def create_app(self):
        return app

    #Create a request
    def test_create_requests(self):
        with self.client:
            post_data = (
                { 
                    "device_type":"laptop",
                    "fault_description": "Battery malfunctioning",
                    "status": "Submitted"
                }
            )
            response = self.client.post(
                '/v1/users/requests', 
                content_type = 'application/json', 
                data = json.dumps(post_data)
            )
            reply = json.loads(response.data.decode()) 
            self.assertEquals(reply['status'], 'OK')
            self.assertEquals(response.status_code, 201)

    #Fetch all the requests of a logged in user
    def test_view_requests(self):
        with self.client:
            response = self.client.get(
                '/v1/users/requests',
                content_type = 'application/json'
#                ,data = json.dumps()
                )
            reply = json.loads(response.data.decode())
            self.assertEquals(reply['message'], 'successful') 
            self.assertEquals(response.status_code, 201)

    #Fetch a request that belongs to a logged in user
    def test_view_user_request(self):
        with self.client:
            response = self.client.get(
                '/v1/users/requests/1', 
                content_type = 'application/json'
#                data = json.dumps()
            )
            reply = json.loads(response.data.decode()) 
            self.assertTrue(reply['device-status'] in ['Submitted', 'Rejected', 'Approved', 'Resolved'], True)
            self.assertEquals(reply['message'], 'successful')
            self.assertTrue(response.status_code, 201)

    #Modify a request
    def test_modify_request(self):
        with self.client:
            response = self.client.put(
                '/v1/users/requests/1', 
                content_type = 'application/json'
#                data = json.dumps()
            )
            reply = json.loads(response.data.decode())
            self.assertTrue(reply['device-status'] in ['Submitted', 'Rejected', 'Approved', 'Resolved'], True)
            self.assertEquals(reply['device-type'], 'phone')
            self.assertEquals(response.status_code, 201)