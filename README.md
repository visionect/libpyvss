This is a package implementing Visionect API in Python.

Check [API documentation](https://api.visionect.com/) for more info.

API endpoints and responses are subject to change, so make sure to follow [release notes.](http://docs.visionect.com/ReleaseNotes/VisionectSoftwareSuite.html)

----

### Installation

```bash
pip install vss-python-api`
```
### Use

```python
from vss_python_api import ApiDeclarations
vss_api_instance = ApiDeclarations(url, key, secret)
status_code, response (optional) = vss_api_instance.{function(params)}
```

### Function list

#### Device

##### retrieve a device

`get_device(uuid)`

 - params: uuid *string*
 - returns: status code *int*, response *json*

##### update a device

`update_device(uuid, device_object)`

 - params: uuid *string*, device_object *json*
 - returns: status code *int*

##### delete a device

`delete_device(uuid)`

 - params: uuid *string*
 - returns: status code *int*, response *json*

----

#### Device collection

##### list all devices

`get_all_devices()`

 - params: /
 - returns: status code *int*, response *json*

##### update a list of devices

`update_all_devices(device_object_list)`

 - params: device_object_list *json list*
    - example: `device_object_list = [device_object1, device_object2, ... device_objectN]`
 - returns: status code *int*

----

#### Device configuration

##### get configuration list

`get_device_config_list(uuid)`

 - params: uuid *string*
 - returns: status code *int*, response *json*

##### get configuration

`get_device_config(uuid, tclv_type)`

 - params: uuid *string*, tclv_type *int*
 - returns: status code *int*, response *json*

##### set configuration

`update_device_config(uuid, tclv_type, value)`

 - params: uuid *string*, tclv_type *int*, value *int*
 - returns: status code *int*

----

#### Reboot

##### reboot device

`reboot_device(uuid)`

 - params: uuid *string*
 - returns: status code *int*

##### reboot a list of devices

`reboot_device_list(uuid_list)`

 - params: uuid_list *list*
      - example: `uuid_list = [uuid1, uuid2, ... uuidN]`
  - returns: status code *int*

----

#### Sessions

##### retrieve a session

`get_session(uuid)`

 - params: uuid *string*
 - returns: status code *int*, response *json*

##### update a session

`update_session(uuid, session_object)`

 - params: uuid *string*, session_object *json*
 - returns: status_code *int*

##### remove a session

 `delete_session(uuid)`

 - params: uuid *string*
 - returns: status_code *int*

----

#### Session collection

##### list all sessions

 `get_session_list()`

 - returns: status_code *int*, response *json*

##### create a session

 `create_session(session_object)`

 - params: session_object *json*
    - example:
        ```python
        session_object = {
            "Uuid": {uuid},
            "Backend": {
                "Name": "HTML",
                "Fields": {
                    "url": "http://demo.visionect.com/clock/?t=602"
                }
            },
            "Options": {
                "DefaultDithering": "none",
                "DefaultEncoding": "4"
            }
        }
        ```
 - returns: status_code *int*

##### update a list of sessions

 `update_session_list(sessions_object)`

 - params: sessions_object *json list*
    - example: `sessions_object = [session_object1, session_object2, ...  session_objectN]`
 - returns: status_code *int*

----

#### Restart

##### restart a session

 `restart_session(uuid)`

 - params: uuid *string*
 - returns: status_code *int*

##### restart a list of sessions

 `restart_session_list(uuid_list)`

 - params: uuid_list *string list*
    - example: `[uuid1, uuid2, ... uuidN]`
 - returns: status_code *int*

----

#### User

##### retrieve a user

 `get_user(username)`

 - params: username *string*
 - returns: status_code *int*, response *json*

##### update a user

 `update_user(username, user_object)`

 - params: username *string*, user_object *json*
    - example:
    ```python
    {
        "Username": {username},
        "Password": {password},
        "IsActive": true,
        "IsAPI": false
    }
    ```
 - returns: status_code *int*

##### delete a user

 `delete_user(username)`

 - params: username *string*
 - returns: status_code *int*

----

#### User list

##### list all users

 `get_user_list()`

 - returns: status_code *int*, response *json*

#### create a user

 `create_user(username, password)`

 - params: username *string*, password *string*
 - returns: status_code *int*

#### update a list of users

 `update_user_list(user_list_object)`

 - params: user_list_object *json list*
    - example: `user_list_object = [user_object1, user_object2, ... user_objectN]`
 - returns: status_code *int*

----

#### Config

##### retrieve configuration

 `get_config()`

 - returns: status_code *int*, response *json*

#### update configuration

 `update_config(config_object)`

 - params: config_object *json*
 - returns: status_code *int*

----

#### Live view

 `get_live_view(uuid, type, file_lv)`

 - params: uuid *string*, type *string*, file_lv *string*
    - example: `get_live_view({uuid}, 'image', '.png')`
 - returns: status_code *int*

----

#### Status

 `get_status()`

 - returns: status_code *int*, response *json*