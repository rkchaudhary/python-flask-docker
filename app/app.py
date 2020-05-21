from flask import Flask, render_template, request
import socket
import json
import base64

app = Flask(__name__)


@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')


@app.route("/api/monitor.htm")
def monitor():
    return "0"


@app.route("/api/results/<search_id>")
def results(search_id):
    headers = request.headers
    print(search_id)
    is_valid_request = _validate_token()
    response = dict()
    if is_valid_request is True:
        device_1 = {'deviceId': 'iPhone', 'risk_score': '9', 'last_reported': '20-May-2020'};
        device_2 = {'deviceId': 'Android phone', 'risk_score': '6', 'last_reported': '22-May-2020'}
        device_list = [device_1, device_2]
        response['status'] = "Success"
        response['code'] = 200
        response['searchId'] = search_id
        response['data'] = device_list
    else:
        response['status'] = "Failure"
        response['errmsg'] = "Invalid Auth Token"
        response['code'] = 401
        response['searchId'] = search_id
    return json.dumps(response)


@app.route("/api/query", methods = ['POST'])
def query():
    response = dict()
    is_valid_request = _validate_token()
    query_expression = request.data
    search_id = base64.b64encode(query_expression).decode()

    if is_valid_request is True:
        response['status'] = "Success"
        response['code'] = 200
        response['errmsg'] = ""
        response['search_id'] = search_id
    else:
        response['status'] = "Failure"
        response['errmsg'] = "Invalid Auth Token"
        response['code'] = 401
    return json.dumps(response)


def _validate_token():
    token = request.headers['X-Auth-Token']
    if token == 'BDFSXK-EVDKESD-DHDJDB-DSKANS':
        return True
    return False

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
