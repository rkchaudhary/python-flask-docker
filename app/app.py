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
    response = dict()
    response['success'] = True
    response['code'] = 200
    return json.dumps(response)


@app.route("/api/results/<search_id>")
def results(search_id):
    is_valid_request = _validate_token()
    response = dict()
    if is_valid_request is True:
        device_1 = {'fl_user_id': 'rkchaudhary', 'fl_email_add': 'rkchaudhary@ibm.com',
                    'fl_device_id': 'ApplF2LV13JPHFM2', 'fl_device_platform': 'iOS',
                    'first_observed':'2019-12-04T09:37:54.6939357Z','last_observed':'2019-12-04T09:37:54.6939357Z' };
        device_2 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                    'fl_device_platform': 'iOS',
                    'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_3 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                    'fl_device_platform': 'iOS',
                    'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_4 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                    'fl_device_platform': 'iOS',
                    'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_5 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                    'fl_device_platform': 'iOS',
                    'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_6 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                    'fl_device_platform': 'iOS',
                    'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_7 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                    'fl_device_platform': 'iOS',
                    'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_8 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                    'fl_device_platform': 'iOS',
                    'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_9 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                    'fl_device_platform': 'iOS',
                    'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_10 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                     'fl_device_platform': 'iOS',
                     'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_11 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                     'fl_device_platform': 'iOS',
                     'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_12 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                     'fl_device_platform': 'iOS',
                     'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};
        device_13 = {'fl_user_id': 'vikas', 'fl_email_add': 'vikas.kumar1@ibm.com', 'fl_device_id': 'ApplF2L12345634',
                     'fl_device_platform': 'iOS',
                     'first_observed': '2019-12-04T09:37:54.6939357Z', 'last_observed': '2019-12-04T09:37:54.6939357Z'};

        device_list = [device_1, device_2, device_3, device_4, device_5, device_6, device_7, device_8, device_9,
                       device_10, device_11,
                       device_12, device_13]
        response['success'] = True
        response['code'] = 200
        response['searchId'] = search_id
        response['data'] = device_list
    else:
        response['success'] = False
        response['errmsg'] = "Invalid Auth Token"
        response['code'] = 401
        response['searchId'] = search_id
    return json.dumps(response)


@app.route("/api/query", methods=['POST'])
def query():
    response = dict()
    is_valid_request = _validate_token()
    query_expression = request.data
    search_id = base64.b64encode(query_expression).decode()

    if is_valid_request is True:
        response['success'] = True
        response['code'] = 200
        response['errmsg'] = ""
        response['search_id'] = search_id
    else:
        response['success'] = False
        response['errmsg'] = "Invalid Auth Token"
        response['code'] = 401
    return json.dumps(response)


@app.route("/api/status/<search_id>")
def status(search_id):
    response = dict()
    is_valid_request = _validate_token()

    if is_valid_request is True:
        response['success'] = True
        response['status'] = "COMPLETED"
        response['progress'] = 100
        response['search_id'] = search_id
    else:
        response['success'] = False
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
