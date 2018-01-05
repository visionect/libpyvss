import requests
import base64
import hmac
import hashlib
import time
import wsgiref.handlers
import json
from requests_toolbelt import MultipartEncoder


class ApiDeclarations:
    def __init__(self, url, key, secret):
        self.url = url
        self.key = key
        self.secret = secret

    def calc_auth(self, endpoint, verb, content_type='application/json', dt=time.time(), content=""):
        headers = {
            'Date': wsgiref.handlers.format_date_time(dt),
            'Content-Type': content_type
        }
        h = hmac.new(self.secret, verb + '\n' + content + '\n' + headers['Content-Type'] + '\n' + headers['Date'] + '\n/' + endpoint, hashlib.sha256)
        headers['Authorization'] = self.key + ':' + base64.encodestring(h.digest()).strip()

        return headers

    #       DEVICE
    # --------------------------------------------------------------
    def get_device(self, uuid):
        endpoint = 'api/device/' + uuid
        r = requests.get(self.url + endpoint, headers=self.calc_auth(endpoint, "GET"))
        return r.status_code, r.json()

    def update_device(self, uuid, new_device):
        endpoint = 'api/device/' + uuid
        r = requests.put(self.url + endpoint, headers=self.calc_auth(endpoint, "PUT", uuid), data=json.dumps(new_device))
        return r.status_code

    def delete_device(self, uuid):
        endpoint = 'api/device/' + uuid
        r = requests.delete(self.url + endpoint, headers=self.calc_auth(endpoint, "DELETE", uuid))
        return r.status_code, r.content

    # --------------------------------------------------------------

    #       DEVICE COLLECTION
    # --------------------------------------------------------------
    def get_all_devices(self):
        endpoint = 'api/device/'
        r = requests.get(self.url + endpoint, headers=self.calc_auth(endpoint, "GET"))
        return r.status_code, r.json()

    def update_all_devices(self, device_object_list):
        endpoint = 'api/device/'
        r = requests.put(self.url + endpoint, headers=self.calc_auth(endpoint, "PUT"), json=device_object_list)
        return r.status_code

    # --------------------------------------------------------------

    #       DEVICE CONFIGURATION
    # --------------------------------------------------------------
    def get_device_config_list(self, uuid):
        endpoint = "api/devicetclv/" + uuid
        r = requests.get(self.url + endpoint, headers=self.calc_auth(endpoint, "GET"))
        return r.status_code, r.json()

    def get_device_config(self, uuid, type_tclv):
        endpoint = 'api/cmd/Param/' + uuid
        tclv_to_send = '{"Data": [{"Type": ' + str(type_tclv) + ',"Control": 0, "Value": ""}]}'
        r = requests.post(self.url + endpoint, headers=self.calc_auth(endpoint, "POST"), data=tclv_to_send)
        return r.status_code, r.json()

    def update_device_config(self, uuid, typ, value):
        endpoint = 'api/cmd/Param/' + uuid
        tclv_to_send = '{"Data": [{"Type": ' + str(typ) + ',"Control": 1, "Value": "' + str(value) + '"}]}'
        r = requests.post(self.url + endpoint, headers=self.calc_auth(endpoint, "POST"), data=tclv_to_send)
        return r.status_code

    # --------------------------------------------------------------

    #       REBOOT DEVICE
    # --------------------------------------------------------------
    def reboot_device(self, uuid):
        endpoint = 'api/device/' + uuid + '/reboot'
        r = requests.post(self.url + endpoint, headers=self.calc_auth(endpoint, "POST"))
        return r.status_code

    def reboot_device_list(self, uuid_list):
        endpoint = 'api/device/reboot'
        r = requests.post(self.url + endpoint, headers=self.calc_auth(endpoint, "POST"), json=uuid_list)
        return r.status_code
    # --------------------------------------------------------------

    #       SESSIONS
    # --------------------------------------------------------------
    def get_session(self, uuid):
        endpoint = 'api/session/' + uuid
        r = requests.get(self.url + endpoint, headers=self.calc_auth(endpoint, "GET", uuid))
        return r.status_code, r.json()

    def update_session(self, uuid, new_session):
        endpoint = 'api/session/' + uuid
        r = requests.put(self.url + endpoint, headers=self.calc_auth(endpoint, "PUT"), data=json.dumps(new_session))
        return r.status_code

    def delete_session(self, uuid):
        endpoint = 'api/session/' + uuid
        r = requests.delete(self.url + endpoint, headers=self.calc_auth(endpoint, "DELETE"))
        return r.status_code

    # --------------------------------------------------------------

    #       SESSION LIST
    # --------------------------------------------------------------
    def get_session_list(self):
        endpoint = 'api/session/'
        r = requests.get(self.url + endpoint, headers=self.calc_auth(endpoint, "GET"))
        return r.status_code, r.json()

    def create_session(self, session_object):
        endpoint = 'api/session/'
        r = requests.post(self.url + endpoint, headers=self.calc_auth(endpoint, "POST"), json=session_object)
        return r.status_code

    def update_session_list(self, sessions_object):
        endpoint = 'api/session/'
        r = requests.put(self.url + endpoint, headers=self.calc_auth(endpoint, "PUT"), json=sessions_object)
        return r.status_code

    # --------------------------------------------------------------

    #       SESSION RESTART
    # --------------------------------------------------------------
    def restart_session(self, uuid):
        endpoint = 'api/session/' + uuid + '/restart'
        r = requests.post(self.url + endpoint, headers=self.calc_auth(endpoint, "POST"))
        return r.status_code

    def restart_session_list(self, uuid_list):
        endpoint = 'api/session/restart'
        r = requests.post(self.url + endpoint, headers=self.calc_auth(endpoint, "POST"), json=uuid_list)
        return r.status_code

    # --------------------------------------------------------------

    #       USER
    # --------------------------------------------------------------
    def get_user(self, username):
        endpoint = 'api/user/' + username
        r = requests.get(self.url + endpoint, headers=self.calc_auth(endpoint, "GET"))
        return r.status_code, r.json()

    def update_user(self, username, user_object):
        endpoint = 'api/user/' + username
        r = requests.put(self.url + endpoint, headers=self.calc_auth(endpoint, "PUT"), json=user_object)
        return r.status_code

    def delete_user(self, username):
        endpoint = 'api/user/' + username
        r = requests.delete(self.url + endpoint, headers=self.calc_auth(endpoint, "DELETE"))
        return r.status_code

    # --------------------------------------------------------------

    #       USER LIST
    # --------------------------------------------------------------
    def get_user_list(self):
        endpoint = 'api/user/'
        r = requests.get(self.url + endpoint, headers=self.calc_auth(endpoint, "GET"))
        return r.status_code, r.json()

    def create_user(self, username, password):
        endpoint = 'api/user/'
        sc, cont = self.get_user_list()
        cont[0]['Username'] = username
        cont[0]['Password'] = password
        cont[0]["IsActive"] = True
        cont[0]["IsAPI"] = False
        r = requests.post(self.url + endpoint, headers=self.calc_auth(endpoint, "POST"), json=cont[0])
        return r.status_code

    def update_user_list(self, user_list_object):
        endpoint = 'api/user/'
        r = requests.put(self.url + endpoint, headers=self.calc_auth(endpoint, "PUT"), json=user_list_object)
        return r.status_code

    # --------------------------------------------------------------

    #       CONFIG
    # --------------------------------------------------------------
    def get_config(self):
        endpoint = 'api/config/'
        r = requests.get(self.url + endpoint, headers=self.calc_auth(endpoint, "GET"))
        return r.status_code, r.json()

    def update_config(self, config_object):
        endpoint = 'api/config/'
        r = requests.put(self.url + endpoint, headers=self.calc_auth(endpoint, "PUT"), json=config_object)
        return r.status_code

    # --------------------------------------------------------------

    #       LIVE VIEW
    # --------------------------------------------------------------
    def get_live_view(self, uuid, typ, file_lv):
        endpoint = 'api/live/device/' + uuid + '/' + typ + file_lv
        r = requests.get(self.url + endpoint, headers=self.calc_auth(endpoint, "GET"))
        return r.status_code

    # --------------------------------------------------------------

    #       STATUS
    # --------------------------------------------------------------
    def get_status(self):
        endpoint = 'api/status/'
        r = requests.get(self.url + endpoint, headers=self.calc_auth(endpoint, "GET"))
        return r.status_code, r.json()

    # --------------------------------------------------------------

    #       HTTP BACKEND
    # --------------------------------------------------------------
    def set_http(self, uuid, img):
        endpoint = 'backend/' + uuid
        m = MultipartEncoder(fields=img)
        r = requests.put(self.url + endpoint, headers=self.calc_auth(endpoint, "PUT", m.content_type), data=m)
        return r.status_code
    # --------------------------------------------------------------
