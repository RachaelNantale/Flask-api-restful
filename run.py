from flask import Flask, request, jsonify,abort
from api.views import my_app
import json
import api
from api import *
from api.views import app
app.register_blueprint(my_app)



if __name__ == '__main__':
    app.run(debug='True')
                
                