import json
from gluon.tools import AuthJWT, AuthAPI
import requests


def login():
    email = request.vars.email
    password = request.vars.password
    # remember_me = request.vars.remember
    authentication = AuthAPI(db).login(email=email, password=password)
    if authentication['message'] == 'Logged in':
        data = {'username': email, 'password': password}
        r = requests.post('http://127.0.0.1:8000/api/token', data=data)
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


myjwt = AuthJWT(auth, secret_key='secretsddfsdfsd')

# this one receives the credentials and gives you a token refer to gluon/tools.py 1132 line


def token():
    return myjwt.jwt_token_manager()


@myjwt.allows_jwt()
@auth.allows_jwt()
def protected():
    return '%s$%s' % (request.now, auth.user_id)
