import requests
import base64
import hmac
import hashlib
import time
import wsgiref.handlers
import uuid
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

    def update_all_devices(self, new_object):
        r = requests.put(self.url + 'api/device/', headers=self.calc_auth("api/device/", "PUT"), json=new_object)
        return r.status_code, r.content

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
        return r.status_code, r.content

    # --------------------------------------------------------------

    #       REBOOT DEVICE
    # --------------------------------------------------------------
    def reboot_device(self, uuid):
        r = requests.post(self.url + 'api/device/' + uuid + '/reboot',
                          headers=self.calc_auth("api/device/" + uuid + "/reboot", "POST"))
        return r.status_code, r.content

    def reboot_device_list(self, uuid):
        body = [uuid]
        r = requests.post(self.url + 'api/device/reboot', headers=self.calc_auth("api/device/reboot", "POST"),
                          json=body)
        return r.status_code, r.content

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
        return r.status_code, r.content

    def delete_session(self, uuid):
        r = requests.delete(self.url + 'api/session/' + uuid, headers=self.calc_auth("api/session/"+uuid, "DELETE"))
        return r.status_code, r.content

    # --------------------------------------------------------------

    #       SESSION LIST
    # --------------------------------------------------------------
    def get_session_list(self):
        r = requests.get(self.url + 'api/session/', headers=self.calc_auth("api/session/", "GET"))
        return r.status_code, r.json()

    def create_session(self):
        uid1 = str(uuid.uuid4())
        uid1 = uid1[0:28] + '00000000'
        body = {
            "Uuid": uid1,
            "Options": {
                "DefaultDithering": "none",
                "DefaultEncoding": "4"
            },
            "Backend": {
                "Name": "HTML",
                "Fields": {
                    "url": 	"http://demo.visionect.com/clock/?t=600"
                }
            }
        }
        r = requests.post(self.url + 'api/session/', headers=self.calc_auth("api/session/", "POST"), json=body)
        return r.status_code, r.content

    def update_session_list(self, uuid):
        body = [
            {
                "Uuid": str(uuid),
                "Options": {
                    "DefaultDithering": "none",
                    "DefaultEncoding": "4"
                },
                "Backend": {
                    "Name": "HTML",
                    "Fields": {
                        "url": "http://demo.visionect.com/clock/?t=602"
                    }
                }
            }
        ]
        r = requests.put(self.url + 'api/session/', headers=self.calc_auth("api/session/", "PUT"), json=body)
        return r.status_code, r.content

    # --------------------------------------------------------------

    #       SESSION RESTART
    # --------------------------------------------------------------
    def restart_session(self, uuid):
        r = requests.post(self.url + 'api/session/' + uuid + '/restart',
                          headers=self.calc_auth('api/session/' + uuid + '/restart', "POST"))
        return r.status_code, r.content

    def restart_session_list(self, uuid_array):
        r = requests.post(self.url + 'api/session/restart', headers=self.calc_auth("api/session/restart", "POST"),
                          json=uuid_array)
        return r.status_code, r.content

    # --------------------------------------------------------------

    #       USER
    # --------------------------------------------------------------
    def get_user(self, username):
        r = requests.get(self.url + 'api/user/' + username, headers=self.calc_auth("api/user/" + username, "GET"))
        return r.status_code, r.json()

    def update_user(self, username, new_object):
        r = requests.put(self.url + 'api/user/' + username, headers=self.calc_auth("api/user/" + username, "PUT"),
                         json=new_object)
        return r.status_code, r.content

    def delete_user(self, username):
        r = requests.delete(self.url + 'api/user/' + username, headers=self.calc_auth("api/user/" + username, "DELETE"))
        return r.status_code, r.content

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
        return r.status_code, r.content

    def update_user_list(self, new_object):
        r = requests.put(self.url + 'api/user/', headers=self.calc_auth("api/user/", "PUT"), json=new_object)
        return r.status_code, r.content

    # --------------------------------------------------------------

    #       CONFIG
    # --------------------------------------------------------------
    def get_config(self):
        r = requests.get(self.url + 'api/config/', headers=self.calc_auth("api/config/", "GET"))
        return r.status_code, r.json()

    def update_config(self, new_object):
        r = requests.put(self.url + 'api/config/', headers=self.calc_auth("api/config/", "PUT"), json=new_object)
        return r.status_code, r.content

    # --------------------------------------------------------------

    #       LIVE VIEW
    # --------------------------------------------------------------
    def get_live_view(self, uuid, type, file_lv):
        r = requests.get(self.url + 'api/live/device/' + uuid + '/' + type + file_lv,
                         headers=self.calc_auth('api/live/device/' + uuid + '/' + type + file_lv, "GET"))
        return r.status_code, r.content

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
