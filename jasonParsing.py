#can be ignored

# import json
# import configparser
#
# import pytest
# import requests
#
# from utilities.BaseClass import BaseClass
# from utilities.DataforVerses import DataforVerses
# from utilities.configurations import *
# from cerberus import Validator
#
# url = getConfig()['API']['endpoint'] + "/resources"
#
#
# def test_delete(self):
#     resp = requests.delete(url)
#     log = self.get_logger()
#     log.info(resp.status_code)
#     log.info(resp.reason)
#     assert resp.status_code != 200, "Delete requests are allowed"
#     log.info("Success,You can make only GET calls to the API.")
#
# # def test_just():
# #     m = {"mandal": ['xyz']}
# #     resp = requests.get(url, params=m)
# #     print(resp.reason)
# #     #print(type(resp.json()))
# #
# #     json_data = resp.json()[0]
# #     print(json_data)
# #
# #     schema = {'mandal': {'type': 'integer', 'min': 2, 'max': 10},
# #               'meter': {'type': 'string'},
# #               'sukta': {'type': 'integer', 'max': 191},
# #               'sungby': {'type': 'string'},
# #               'sungbycategory': {'type': 'string'},
# #               'sungfor': {'type': 'string'},
# #               'sungforcategory': {'type': 'string'}
# #               }
# #
# #     validator = Validator(schema, require_all=True)
# #     is_valid = validator.validate(json_data)
# #     assert (is_valid), print(validator.errors)
#
# # resp=requests.delete(url)
# # # Status code check
# # print("Status code returned is:")
# # print(resp.status_code)
# # print (resp.reason)
# # assert resp.status_code == 200,"Status code should not be 200. Rather it should be :" + str(resp.status_code) + ":" + str(resp.reason)