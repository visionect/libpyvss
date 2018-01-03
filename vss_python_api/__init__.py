import requests
import base64
import hmac
import hashlib
import time
import wsgiref.handlers
import json


class ApiDeclarations:
    def __init__(self, url, key, secret):
        self.url = url
        self.key = key
        self.secret = secret

    def calc_auth(self, endpoint, verb, uid=None, multipart=False):
        headers = {
            'Date': wsgiref.handlers.format_date_time(time.time()),
            'Content-Type': 'application/json'
        }

        if uid is not None:
            h = hmac.new(self.secret, verb + '\n\n' + headers['Content-Type'] + '\n' + headers['Date'] + '\n/' + endpoint + uid, hashlib.sha256)
            headers['Authorization'] = self.key + ':' + base64.encodestring(h.digest()).strip()

        elif multipart is not False:
            h = hmac.new(self.secret, verb + '\n\n' + 'multipart/form-data' + '\n' + headers['Date'] + '\n/' + endpoint + uid, hashlib.sha256)
            headers['Authorization'] = self.key + ':' + base64.encodestring(h.digest()).strip()

        else:
            h = hmac.new(self.secret, verb + '\n\n' + headers['Content-Type'] + '\n' + headers['Date'] + '\n/' + endpoint, hashlib.sha256)
            headers['Authorization'] = self.key + ':' + base64.encodestring(h.digest()).strip()

        return headers

    #       DEVICE
    # --------------------------------------------------------------
    def get_device(self, uuid):
        r = requests.get(self.url + 'api/device/' + uuid, headers=self.calc_auth("api/device/", "GET", uuid))
        return r.status_code, r.json()

    def update_device(self,uuid, new_device):
        r = requests.put(self.url + 'api/device/' + uuid, headers=self.calc_auth("api/device/", "PUT", uuid), data=json.dumps(new_device))
        return r.status_code

    def delete_device(self, uuid):
        r = requests.delete(self.url + 'api/device/' + uuid, headers=self.calc_auth("api/device/", "DELETE", uuid))
        return r.status_code, r.content

    # --------------------------------------------------------------

    #       DEVICE COLLECTION
    # --------------------------------------------------------------
    def get_all_devices(self):
        r = requests.get(self.url + 'api/device/', headers=self.calc_auth("api/device/", "GET"))
        return r.status_code, r.json()

    def update_all_devices(self, device_object_list):
        r = requests.put(self.url + 'api/device/', headers=self.calc_auth("api/device/", "PUT"), json=device_object_list)
        return r.status_code

    # --------------------------------------------------------------

    #       DEVICE CONFIGURATION
    # --------------------------------------------------------------
    def get_device_config_list(self, uuid):
        r = requests.get(self.url + 'api/devicetclv/' + uuid,
                         headers=self.calc_auth("api/devicetclv/", "GET", uuid))
        return r.status_code, r.json()

    def get_device_config(self, uuid, type_tclv):
        tclv_to_send = '{"Data": [{"Type": ' + str(type_tclv) + ',"Control": 0, "Value": ""}]}'
        r = requests.post(self.url + 'api/cmd/Param/' + uuid,
                          headers=self.calc_auth("api/cmd/Param/", "POST", uuid), data=tclv_to_send)
        return r.status_code, r.json()

    def update_device_config(self, uuid, type, value):
        tclv_to_send = '{"Data": [{"Type": ' + str(type) + ',"Control": 1, "Value": "' + str(value) + '"}]}'
        r = requests.post(self.url + 'api/cmd/Param/' + uuid,
                          headers=self.calc_auth("api/cmd/Param/", "POST", uuid), data=tclv_to_send)
        return r.status_code

    # --------------------------------------------------------------

    #       REBOOT DEVICE
    # --------------------------------------------------------------
    def reboot_device(self, uuid):
        r = requests.post(self.url + 'api/device/' + uuid + '/reboot',
                          headers=self.calc_auth("api/device/" + uuid + "/reboot", "POST"))
        return r.status_code

    def reboot_device_list(self, uuid_list):
        r = requests.post(self.url + 'api/device/reboot', headers=self.calc_auth("api/device/reboot", "POST"),
                          json=uuid_list)
        return r.status_code
    # --------------------------------------------------------------

    #       SESSIONS
    # --------------------------------------------------------------
    def get_session(self, uuid):
        r = requests.get(self.url + 'api/session/' + uuid,
                         headers=self.calc_auth("api/session/", "GET", uuid))
        return r.status_code, r.json()

    def update_session(self, uuid, new_session):
        r = requests.put(self.url + 'api/session/' + uuid,
                         headers=self.calc_auth("api/session/", "PUT", uuid), data=json.dumps(new_session))
        return r.status_code

    def delete_session(self, uuid):
        r = requests.delete(self.url + 'api/session/' + uuid, headers=self.calc_auth("api/session/"+uuid, "DELETE"))
        return r.status_code

    # --------------------------------------------------------------

    #       SESSION LIST
    # --------------------------------------------------------------
    def get_session_list(self):
        r = requests.get(self.url + 'api/session/', headers=self.calc_auth("api/session/", "GET"))
        return r.status_code, r.json()

    def create_session(self, session_object):
        r = requests.post(self.url + 'api/session/', headers=self.calc_auth("api/session/", "POST"), json=session_object)
        return r.status_code

    def update_session_list(self, sessions_object):
        r = requests.put(self.url + 'api/session/', headers=self.calc_auth("api/session/", "PUT"), json=sessions_object)
        return r.status_code

    # --------------------------------------------------------------

    #       SESSION RESTART
    # --------------------------------------------------------------
    def restart_session(self, uuid):
        r = requests.post(self.url + 'api/session/' + uuid + '/restart',
                          headers=self.calc_auth('api/session/' + uuid + '/restart', "POST"))
        return r.status_code

    def restart_session_list(self, uuid_list):
        r = requests.post(self.url + 'api/session/restart', headers=self.calc_auth("api/session/restart", "POST"), json=uuid_list)
        return r.status_code

    # --------------------------------------------------------------

    #       USER
    # --------------------------------------------------------------
    def get_user(self, username):
        r = requests.get(self.url + 'api/user/' + username, headers=self.calc_auth("api/user/" + username, "GET"))
        return r.status_code, r.json()

    def update_user(self, username, user_object):
        r = requests.put(self.url + 'api/user/' + username, headers=self.calc_auth("api/user/" + username, "PUT"), json=user_object)
        return r.status_code

    def delete_user(self, username):
        r = requests.delete(self.url + 'api/user/' + username, headers=self.calc_auth("api/user/" + username, "DELETE"))
        return r.status_code

    # --------------------------------------------------------------

    #       USER LIST
    # --------------------------------------------------------------
    def get_user_list(self):
        r = requests.get(self.url + 'api/user/', headers=self.calc_auth("api/user/", "GET"))
        return r.status_code, r.json()

    def create_user(self, username, password):
        sc, cont = self.get_user_list()
        cont[0]['Username'] = username
        cont[0]['Password'] = password
        cont[0]["IsActive"] = True
        cont[0]["IsAPI"] = False
        print(cont)
        r = requests.post(self.url + 'api/user/', headers=self.calc_auth("api/user/", "POST"), json=cont[0])
        return r.status_code

    def update_user_list(self, user_list_object):
        r = requests.put(self.url + 'api/user/', headers=self.calc_auth("api/user/", "PUT"), json=user_list_object)
        return r.status_code

    # --------------------------------------------------------------

    #       CONFIG
    # --------------------------------------------------------------
    def get_config(self):
        r = requests.get(self.url + 'api/config/', headers=self.calc_auth("api/config/", "GET"))
        return r.status_code, r.json()

    def update_config(self, config_object):
        r = requests.put(self.url + 'api/config/', headers=self.calc_auth("api/config/", "PUT"), json=config_object)
        return r.status_code

    # --------------------------------------------------------------

    #       LIVE VIEW
    # --------------------------------------------------------------
    def get_live_view(self, uuid, type, file_lv):
        r = requests.get(self.url + 'api/live/device/' + uuid + '/' + type + file_lv,
                         headers=self.calc_auth('api/live/device/' + uuid + '/' + type + file_lv, "GET"))
        return r.status_code

    # --------------------------------------------------------------

    #       STATUS
    # --------------------------------------------------------------
    def get_status(self):
        r = requests.get(self.url + 'api/status/', headers=self.calc_auth("api/status/", "GET"))
        return r.status_code, r.json()

    # --------------------------------------------------------------

    # #       HTTP BACKEND
    # # --------------------------------------------------------------
    # def set_http(self, uuid, img):
    #     r = requests.put(self.url + 'backend/' + uuid, headers=self.calc_auth('backend/' + uuid, "PUT", uuid, True), files=img)
    #     return r.status_code
    # # --------------------------------------------------------------
