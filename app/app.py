from flask import Flask,render_template,request
import socket
import json

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')
@app.route("/monitor.htm")
def monitor():
    return "0"

@app.route("/status")
def status():
    headers = request.headers
    isValidRequest = _validate_token()
    if(isValidRequest == True):
        request.headers.get('your-header-name')
        response = dict()
        response['status'] = "Processing"
        response['searchId'] = "23456789"
        return json.dumps(response)
    else:
        response = dict()
        response['status'] = "Invalid Auth Token"
        return json.dumps(response)


@app.route("/query")
def query():
    response = dict()
    isValidRequest = _validate_token()
    if (isValidRequest == True):
        response['status'] = "Success"
        response['id'] = 2345
        response['name'] = "Rajiv Chaudhary"
        response['team'] = "Cloud Extender Platform"
        response['role'] = "Tech Lead"
    else:
        response['status'] = "Invalid Auth Token"
    return json.dumps(response)

def _validate_token():
    token = request.headers['X-Auth-Token']
    if(token == 'BDFSXK-EVDKESD-DHDJDB-DSKANS'):
        return True
    return False

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
