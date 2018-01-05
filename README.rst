This is a package implementing Visionect API in Python (version 2.7).

Check `API documentation <https://api.visionect.com/>`__ for more info.

API endpoints and responses are subject to change, so make sure to
follow `release
notes. <http://docs.visionect.com/ReleaseNotes/VisionectSoftwareSuite.html>`__

--------------

Installation
~~~~~~~~~~~~

.. code:: bash

    pip install vss-python-api

Use
~~~

.. code:: python

    from vss_python_api import ApiDeclarations
    vss_api_instance = ApiDeclarations(url, key, secret)
    status_code, response (optional) = vss_api_instance.{function(params)}

Function list
~~~~~~~~~~~~~

Device
^^^^^^

retrieve a device
'''''''''''''''''

``get_device(uuid)``

-  params: uuid *string*
-  returns: status code *int*, response *json*

update a device
'''''''''''''''

``update_device(uuid, device_object)``

-  params: uuid *string*, device\_object *json*
-  returns: status code *int*

delete a device
'''''''''''''''

``delete_device(uuid)``

-  params: uuid *string*
-  returns: status code *int*, response *json*

--------------

Device collection
^^^^^^^^^^^^^^^^^

list all devices
''''''''''''''''

``get_all_devices()``

-  params: /
-  returns: status code *int*, response *json*

update a list of devices
''''''''''''''''''''''''

``update_all_devices(device_object_list)``

-  params: device\_object\_list *json list*

   -  example:
      ``device_object_list = [device_object1, device_object2, ... device_objectN]``

-  returns: status code *int*

--------------

Device configuration
^^^^^^^^^^^^^^^^^^^^

get configuration list
''''''''''''''''''''''

``get_device_config_list(uuid)``

-  params: uuid *string*
-  returns: status code *int*, response *json*

get configuration
'''''''''''''''''

``get_device_config(uuid, tclv_type)``

-  params: uuid *string*, tclv\_type *int*
-  returns: status code *int*, response *json*

set configuration
'''''''''''''''''

``update_device_config(uuid, tclv_type, value)``

-  params: uuid *string*, tclv\_type *int*, value *int*
-  returns: status code *int*

--------------

Reboot
^^^^^^

reboot device
'''''''''''''

``reboot_device(uuid)``

-  params: uuid *string*
-  returns: status code *int*

reboot a list of devices
''''''''''''''''''''''''

``reboot_device_list(uuid_list)``

-  params: uuid\_list *list*

   -  example: ``uuid_list = [uuid1, uuid2, ... uuidN]``

-  returns: status code *int*

--------------

Sessions
^^^^^^^^

retrieve a session
''''''''''''''''''

``get_session(uuid)``

-  params: uuid *string*
-  returns: status code *int*, response *json*

update a session
''''''''''''''''

``update_session(uuid, session_object)``

-  params: uuid *string*, session\_object *json*
-  returns: status\_code *int*

remove a session
''''''''''''''''

``delete_session(uuid)``

-  params: uuid *string*
-  returns: status\_code *int*

--------------

Session collection
^^^^^^^^^^^^^^^^^^

list all sessions
'''''''''''''''''

``get_session_list()``

-  returns: status\_code *int*, response *json*

create a session
''''''''''''''''

``create_session(session_object)``

-  params: session\_object *json*

   -  example:

      .. code:: python

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

-  returns: status\_code *int*

update a list of sessions
'''''''''''''''''''''''''

``update_session_list(sessions_object)``

-  params: sessions\_object *json list*

   -  example:
      ``sessions_object = [session_object1, session_object2, ...  session_objectN]``

-  returns: status\_code *int*

--------------

Restart
^^^^^^^

restart a session
'''''''''''''''''

``restart_session(uuid)``

-  params: uuid *string*
-  returns: status\_code *int*

restart a list of sessions
''''''''''''''''''''''''''

``restart_session_list(uuid_list)``

-  params: uuid\_list *string list*

   -  example: ``[uuid1, uuid2, ... uuidN]``

-  returns: status\_code *int*

--------------

User
^^^^

retrieve a user
'''''''''''''''

``get_user(username)``

-  params: username *string*
-  returns: status\_code *int*, response *json*

update a user
'''''''''''''

``update_user(username, user_object)``

-  params: username *string*, user\_object *json*

   -  example:

      .. code:: python

          {
          "Username": {username},
          "Password": {password},
          "IsActive": true,
          "IsAPI": false
          }

-  returns: status\_code *int*

delete a user
'''''''''''''

``delete_user(username)``

-  params: username *string*
-  returns: status\_code *int*

--------------

User list
^^^^^^^^^

list all users
''''''''''''''

``get_user_list()``

-  returns: status\_code *int*, response *json*

create a user
^^^^^^^^^^^^^

``create_user(username, password)``

-  params: username *string*, password *string*
-  returns: status\_code *int*

update a list of users
^^^^^^^^^^^^^^^^^^^^^^

``update_user_list(user_list_object)``

-  params: user\_list\_object *json list*

   -  example:
      ``user_list_object = [user_object1, user_object2, ... user_objectN]``

-  returns: status\_code *int*

--------------

Config
^^^^^^

retrieve configuration
''''''''''''''''''''''

``get_config()``

-  returns: status\_code *int*, response *json*

update configuration
^^^^^^^^^^^^^^^^^^^^

``update_config(config_object)``

-  params: config\_object *json*
-  returns: status\_code *int*

--------------

Live view
^^^^^^^^^

``get_live_view(uuid, type, file_lv)``

-  params: uuid *string*, type *string*, file\_lv *string*

   -  example: ``get_live_view({uuid}, 'image', '.png')``

-  returns: status\_code *int*

--------------

Status
^^^^^^

``get_status()``

-  returns: status\_code *int*, response *json*

--------------

HTTP Backend
^^^^^^^^^^^^

Upload an image to the device via HTTP backend. Make sure device's
backend is set to the HTTP.

``set_http(uuid, img)``

-  params: uuid *string*, img *file*

   -  example:

      .. code:: python

          img = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'img.png')
          fr = {'image': ('img.png', open(img, 'rb'), 'image/png', {'Expires': '0'})}
          sc = my_api.set_http(uuid, fr)

-  returns: status\_code *int*
