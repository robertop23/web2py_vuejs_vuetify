import json
from gluon.tools import AuthJWT, AuthAPI
import requests
import hashlib

myjwt = AuthJWT(auth, secret_key='secret')

# Decorators


def api_requires_extension(func):
    def wrapper(*args):
        if request.extension != 'html':
            response.view = 'generic.' + request.extension
        else:
            response.view = 'generic.json'
        return func(*args)
    return wrapper


@api_requires_extension
@myjwt.allows_jwt()
def api_requires_login(func):
    def wrapper(*args):
        if not auth.is_logged_in():
            raise HTTP(401)
        return func(*args)
    return wrapper

# User API


def token():
    return myjwt.jwt_token_manager()


@api_requires_extension
def login():
    email = request.vars.email
    password = request.vars.password
    remember = request.vars.remember
    # remember_me = request.vars.remember
    authentication = AuthAPI(db).login(email=email, password=password)
    if authentication['message'] == 'Logged in':
        data = {'username': email, 'password': password, 'remember': remember}
        token_url = 'http://{}:{}/{}/api/token'.format(
            request.env.remote_addr, request.env.server_port, request.application)
        r = requests.post(token_url, data=data)
        if r.status_code == 200:
            # Get Token and contruct the header
            token = r.json()['token']
            authentication['token'] = token
            return authentication
        else:
            raise HTTP(400, 'Cannot get token')
    else:
        error = ['{}'.format(v) for k, v in authentication['errors'].iteritems()][0]
        raise HTTP(400, error.replace('_', ' ').lower().capitalize())


@api_requires_login
def logout():
    authentication = AuthAPI(db).logout(next=None)
    if authentication['message'] == 'Logged out':
        return authentication
    else:
        error = ['{}'.format(k, v) for k, v in authentication['errors'].iteritems()][0]
        raise HTTP(400, error.replace('_', ' ').lower().capitalize())


@api_requires_login
def user():
    avatar = 'https://www.gravatar.com/avatar/{}.jpg?s=200&d=mm'.format(
        hashlib.md5(auth.user.email.lower()).hexdigest())
    user_data = {'first_name': auth.user.first_name,
                 'last_name': auth.user.last_name, 'email': auth.user.email, 'avatar': avatar}
    return user_data


@api_requires_extension
def register():
    first_name = request.vars.first_name
    last_name = request.vars.last_name
    email = request.vars.email
    password = request.vars.password
    authentication = AuthAPI(db).register(first_name=first_name,
                                          last_name=last_name,
                                          email=email,
                                          password=password,
                                          registration_key=None)
    if authentication['message'] == 'Registration successful':
        return authentication
    else:
        error = ['{}'.format(k, v) for k, v in authentication['errors'].iteritems()][0]
        raise HTTP(400, error.replace('_', ' ').lower().capitalize())


@api_requires_login
def profile():
    first_name = request.vars.first_name
    last_name = request.vars.last_name
    authentication = AuthAPI(db).profile(first_name=first_name, last_name=last_name)
    if authentication['message'] == 'Profile updated':
        avatar = 'https://www.gravatar.com/avatar/{}.jpg?s=200&d=mm'.format(
            hashlib.md5(auth.user.email).hexdigest())
        authentication['user']['avatar'] = avatar
        return authentication
    else:
        error = ['{}'.format(v) for k, v in authentication['errors'].iteritems()][0]
        raise HTTP(400, error.replace('_', ' ').lower().capitalize())


@api_requires_login
def change_password():
    old_password = request.vars.old_password
    new_password = request.vars.new_password
    new_password2 = request.vars.new_password2
    authentication = AuthAPI(db).change_password(old_password=old_password,
                                                 new_password=new_password,
                                                 new_password2=new_password)
    if authentication['message'] == 'Password changed':
        return authentication
    else:
        error = ['{}'.format(v) for k, v in authentication['errors'].iteritems()][0]
        raise HTTP(400, error.replace('_', ' ').lower().capitalize())
# Test jwt


@myjwt.allows_jwt(required=True, verify_expiration=True)
def unprotected():
    if auth.user:
        return '%s$%s' % (request.now, auth.user_id)

    return "No auth info!"


@api_requires_login
def myapi():
    return 'hello %s' % auth.user.email
