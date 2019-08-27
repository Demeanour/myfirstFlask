from flask import Flask, request
from flask_restful import (reqparse, abort, Resource, Api)
from flask_restful import fields, marshal_with

app = Flask(__name__)
api = Api(app)

recource_fields = {
    'tast': fields.String,
    'url': fields.Url('tuneloft_ep')
}

## Error handling functions
## if item doesn exist Send a message to notify

def abort_it_doesnt_exist(self,item):
    ##declare self.item
    self.item = item
    abort(404, message="Item {} doesn't exist").format(item)

def verify_account(self, email):
    ## send an email or text to verify account
    pass


######### End of Error handling funcitons ###########

#### User creation and login ####

class Users(Resource):
    def __init__(self):
        pass

class Signup(Resource):
    """
        When the user registers on to the service, they have 4 options:
        - creating an account with us
        - use facebook to create an account with your facebook profile
        - use google to create an account with your google profile
        - use twitter to create an account with your twitter profile.

        what is required from the sign-up is your name email and password. we need to verify 
        your email to grant you access to the site.
    """
    def put(self, signup):
        pass
    def get(self,uid):
        return {'this is ': "a test"}

## Class for logging in the user.
class Login(Resource):
    """
        This is the login class. create a token_id with login. and get device mac_address.
    """
    def get():
        return 'Testing'



######## End of User Creation and Login #######

#### Data and feature ####

## Timeline class for adding items to the home page.
## This class must return a json list of items that are
## to be displayed in the app.
class Timeline(Resource):
    """
        This class will get data from kafka and also will confirm if the user is registered/logged in
        Then it should return a json file that contains the latest Items from the database (these items
        are user posts, events, and stories). Then also has to make a settings check for user preferences
        (has to be a function call to the database again.)
    """
    def get(self):
        return  ("get working now", 203)


class Music:
    """
        This class deals with getting music content from the servers and sending it to the user.
        Not working yet. It still need to be discussed.
    """
    def __init__(self):
        pass

    def get():
        blog_post = api.model('Blog post',{
            'category_id': fields.Integer(attribute='category_id'),
            'name': fields.String(attribute=lambda x: x._private_name)
        })
        return blog_post

    def view_artist():
        pass


class Following(Resource):
    def __init__(self):
        test = {"name": "This is a test"}
        return test
    def view_user():
        pass

###### End of Data and Features ######

## api Resource for all the api requests in app.
api.add_resource(Timeline, '/')
api.add_resource(Signup, '/r')
api.add_resource(Login,)
api.add_resource(Following, '/myfollowing')
api.add_resource(Music, '/music')

if __name__ == '__main__':
    app.run(debug=True,port=2000)
    
    
