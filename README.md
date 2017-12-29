This is a package implementing Visionect API in Python.

Check [API documentation](https://api.visionect.com/) for more info.

## Installation

`pip install vss-python-api`

## Use

`from vss_python_api import ApiDeclarations`

`{object_name} = ApiDeclarations(url, key, secret)`

`status_code, response = {object_name}.{function({params})}`

## Function list

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

`update_all_devices(device_object)`

 - params: device_object *json*
 - returns: status code *int*, response *json*

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

