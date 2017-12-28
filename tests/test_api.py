import unittest

from vss_python_api import ApiDeclarations


class MyTest(unittest.TestCase):

    # def test_delete_device(self):
    #     sc, resp = my_api.delete_device('46002c00-1351-3432-3434-373300000000')
    #     self.assertEqual(sc, 204)
    # def test_reboot_device(self):
    #     sc, resp = my_api.reboot_device(uuid)
    #     self.assertEqual(sc, 204)
    # def test_reboot_device_list(self):
    #     sc, resp = my_api.reboot_device_list(uuid)
    #     self.assertEqual(sc, 204)
    # def test_delete_session(self):
    #     sc, resp = my_api.delete_session(uuid)
    #     self.assertEqual(sc, 200)
    # def test_delete_user(self):
    #     sc, resp = my_api.delete_user("tester")
    #     self.assertEqual(sc, 204)



    def test_get_device(self):
        sc, resp = my_api.get_device(uuid)
        self.assertEqual(sc, 200)

    def test_update_device(self):
        sc, resp = my_api.get_device(uuid)
        sc2 = my_api.update_device(uuid, resp)
        self.assertEqual(sc2, 204)

    def test_get_all_devices(self):
        sc, resp = my_api.get_all_devices()
        self.assertEqual(sc, 200)

    def test_update_all_devices(self):
        sc, resp = my_api.get_all_devices()
        sc2, resp2 = my_api.update_all_devices(resp)
        self.assertEqual(sc2, 204)

    def test_get_device_config_list(self):
        sc, resp = my_api.get_device_config_list(uuid)
        self.assertEqual(sc, 200)

    def test_get_device_config(self):
        sc, resp = my_api.get_device_config(uuid, 29)
        self.assertEqual(sc, 200)

    def test_update_device_config(self):
        sc, resp = my_api.update_device_config(uuid, 29, 10)
        self.assertEqual(sc, 200)

    def test_get_session(self):
        sc, resp = my_api.get_session(uuid)
        self.assertEqual(sc, 200)

    def test_update_session(self):
        sc, resp = my_api.get_session(uuid)
        sc2, resp2 = my_api.update_session(uuid, resp)
        self.assertEqual(sc2, 204)

    def test_get_session_list(self):
        sc, resp = my_api.get_session_list()
        self.assertEqual(sc, 200)

    def test_create_session(self):
        sc, resp = my_api.create_session()
        self.assertEqual(sc, 201)

    def test_update_session_list(self):
        sc, resp = my_api.update_session_list(uuid)
        self.assertEqual(sc, 204)

    def test_restart_session(self):
        sc, resp = my_api.restart_session(uuid)
        self.assertEqual(sc, 204)

    def test_restart_session_list(self):
        sc, resp = my_api.restart_session_list([uuid])
        self.assertEqual(sc, 204)

    def test_get_user(self):
        sc, resp = my_api.get_user("tester")
        self.assertEqual(sc, 200)

    def test_update_user(self):
        sc, resp = my_api.get_user("tester")
        sc2, resp2 = my_api.update_user("tester", resp)
        self.assertEqual(sc2, 204)

    def test_get_user_list(self):
        sc, resp = my_api.get_user_list()
        self.assertEqual(sc, 200)

    def test_create_user(self):
        sc, resp = my_api.create_user("saban", "saban2")
        self.assertEqual(sc, 201)

    def test_update_user_list(self):
        sc, resp = my_api.get_user_list()
        sc2, resp2 = my_api.update_user_list(resp)
        self.assertEqual(sc2, 204)

    def test_get_config(self):
        sc, resp = my_api.get_config()
        self.assertEqual(sc, 200)

    def test_update_config(self):
        sc, resp = my_api.get_config()
        sc2, resp2 = my_api.update_config(resp)
        self.assertEqual(sc2, 204)

    def test_get_live_view(self):
        sc, resp = my_api.get_live_view(uuid, 'image', '.png')
        self.assertEqual(sc, 200)

    def test_get_status(self):
        sc, resp = my_api.get_status()
        self.assertEqual(sc, 200)

    # def test_set_http(self):
    #     f = (open('snamp.png', 'rb')).read()
    #     fr = {'image': f}
    #     # f = {'file': ('snamp.png', open('snamp.png', 'rb'), 'multipart/form-data', {'Expires': '0'})}
    #     sc = my_api.set_http(uuid, fr)
    #     self.assertEqual(sc, 200)