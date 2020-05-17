from flask import request

def validate_token():
    token = request.headers['X-Auth-Token']
    if(token == 'BDFSXK-EVDKESD-DHDJDB-DSKANS'):
        return True
    return False
