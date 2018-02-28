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


def api_requires_extension(func):
    def wrapper(*args):
        if request.extension != 'html':
            response.view = 'generic.' + request.extension
        else:
            response.view = 'generic.json'
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


@api_requires_login
def user():
    import hashlib
    avatar = 'https://www.gravatar.com/avatar/{}.jpg?s=200&d=mm'.format(
        hashlib.md5(auth.user.email.lower()).hexdigest())
    user_data = {'name': auth.user.first_name, 'email': auth.user.email, 'avatar': avatar}
    return user_data


#@api_requires_extension
def register():
    '''
        errors	:	None
        message	:	Registration successful
        user	:
        email	:	robertop23@hotmail.com
        first_name	:	roberto2
        id	:2L
        last_name	:	gjkh
        '''
    first_name = request.vars.first_name
    last_name = request.vars.last_name
    email = request.vars.email
    password = request.vars.password
    authentication = AuthAPI(db).register(first_name=first_name,
                                          last_name=last_name,
                                          email=email,
                                          password=password,
                                          registration_key=None)
    if not authentication['errors'] is None:
        error = ['{} {}'.format(k, v) for k, v in authentication['errors'].iteritems()][0]
        raise HTTP(400, error.replace('_', ' ').lower().capitalize())
    else:
        return authentication


myjwt = AuthJWT(auth, secret_key='secret')


def token():
    return myjwt.jwt_token_manager()


@api_requires_login
def protected():
    return '%s$%s' % (request.now, auth.user_id)


@api_requires_login
def myapi():
    return 'hello %s' % auth.user.email
