import json
from gluon.tools import AuthJWT, AuthAPI
import requests


@request.restful()
def index():
    response.view = 'generic.' + request.extension

    def GET(*args, **vars):
        patterns = 'auto'
        parser = db.parse_as_rest(patterns, args, vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status, parser.error)

    def POST(table_name, **vars):
        return dict(db[table_name].validate_and_insert(**vars))

    def PUT(table_name, **vars):
        return dict()

    def DELETE(table_name, **vars):
        return dict()

    return locals()


@auth.allows_jwt()
def api_requires_login(func):
    def wrapper(*args):
        if request.extension != 'html':
            response.view = 'generic.' + request.extension
        else:
            response.view = 'generic.json'
        if not auth.is_logged_in():
            raise HTTP(401)
        return func(*args)
    return wrapper


def login():
    email = request.vars.email
    password = request.vars.password
    # remember_me = request.vars.remember
    authentication = AuthAPI(db).login(email=email, password=password)
    if authentication['message'] == 'Logged in':
        data = {'username': email, 'password': password}
        token_url = 'http://{}:{}/{}/api/token'.format(
            request.env.remote_addr, request.env.server_port, request.application)
        r = requests.post(token_url, data=data)
        print(r)
        if r.status_code == 200:
            # Get Token and contruct the header
            token = r.json()['token']
            authentication['token'] = token
            return authentication
        else:
            authentication['token'] = None
            return authentication

    else:
        authentication['token'] = None
        return authentication


def logout():
    authentication = AuthAPI(db).logout(next=None)
    return authentication

# this one receives the credentials and gives you a token refer to gluon/tools.py 1132 line


myjwt = AuthJWT(auth, secret_key='secret')

# this one receives the credentials and gives you a token refer to gluon/tools.py 1132 line


def token():
    return myjwt.jwt_token_manager()


@api_requires_login
def protected():
    return '%s$%s' % (request.now, auth.user_id)


@api_requires_login
def myapi():
    return 'hello %s' % auth.user.email


@api_requires_login
def user():
    import hashlib
    avatar = 'https://www.gravatar.com/avatar/{}.jpg?s=200&d=mm'.format(
        hashlib.md5(auth.user.email.lower()).hexdigest())
    user_data = {'name': auth.user.first_name, 'email': auth.user.email, 'avatar': avatar}
    return user_data
