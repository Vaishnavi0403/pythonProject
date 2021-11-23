import json
import configparser

import pytest
import requests

from utilities.BaseClass import BaseClass
from utilities.DataforVerses import DataforVerses
from utilities.configurations import *
from cerberus import Validator

# Due to time constraint i have not created separate files for each modules instead i have created in one class with different methods respectively
# this code can be easily split with minimal change

# EndPoint Provided
url = getConfig()['API']['endpoint'] + "/resources"  # getting it from properties.ini file by using config parser


class Test_RigVeda(BaseClass):

    # Test case for Schema Validation
    def test_Schema(self):

        # In this method,the data type and the length of the field will be verified i.e.,Schema validation of the
        # json data received

        resp = requests.get(url + "/all")
        # creating logger object for the logs
        log = self.get_logger()
        log.info("**** Starting Test For Schema of response Validation ****")
        log.info(type(resp.json()))

        # right now checking the schema for only one verse can be modified for all the verses using for loop
        json_data = resp.json()[0]

        log.info(json_data)
        # created on basis of API requirement doc this can also be saved in DataforVerses class
        schema = {'mandal': {'type': 'integer', 'min': 1, 'max': 10},
                  'meter': {'type': 'string'},
                  'sukta': {'type': 'integer', 'max': 191},
                  'sungby': {'type': 'string'},
                  'sungbycategory': {'type': 'string'},
                  'sungfor': {'type': 'string'},
                  'sungforcategory': {'type': 'string'}
                  }
        log.info(schema)
        # pass schema variable to an instance of the Validator class
        # and invoke the validate() to validate a dictionary against the schema.
        validator = Validator(schema, require_all=True)
        is_valid = validator.validate(json_data)

        assert is_valid, log.info(str(validator.errors) + " Schema validation failed")
        log.info("Success,Schema is validated correctly")

    # Test case for mandal resource validation
    # test data is parameterized and saved in DataforVerses class
    @pytest.mark.parametrize("val", DataforVerses.Mandal_Data)
    def test_GetMandal(self, val):
        # saving the mandal parameter data in variable 'm'
        m = {"mandal": val}

        # creating logger object for the logs
        log = self.get_logger()

        log.info("**** Starting test for mandal validation ****")
        log.info(m)
        # Checking the mandal data Type
        log.info("Mandal data type is :")
        log.info(type(m["mandal"]))

        # if the mandal data requested is integer then only it will enter the IF block otherwise else block will be executed
        if type(m["mandal"]) is int:
            log.info("mandal is integer")
            if m["mandal"] in range(1, 11):
                # GET request
                resp = requests.get(url, params=m)

                # URL Check
                log.info("url is:")
                log.info(resp.url)
                assert resp.url == url + "?mandal=" + str(val), log.error("url is not correct")

                # Status code check
                log.info("Status code returned is:")
                log.info(resp.status_code)
                assert resp.status_code == 200, log.critical(
                    "Status code is not 200. Rather found :" + str(resp.status_code) + ":" + str(resp.reason))

                # Content-Type check
                assert 'json' in resp.headers['Content-Type'], log.critical("The Content-Type is not matching")

                # type of the response received in this example is in List format so result is not parsed
                log.info("Response type received:")
                log.info(type(resp.json()))

                # reading the whole response received
                json_data = resp.json()
                log.info("Response Data Received:")
                log.info(json_data)

                key = "mandal"
                # checking mandal field existence and its value is same as that of requested data
                for i in range(len(json_data)):
                    if json_data[i].get(key) is not None:
                        if json_data[i]["mandal"] == val:
                            pass
                        else:
                            log.error("Mandal is different" + str(json_data[i]["mandal"]))
                    else:
                        log.info("No, key: '{key}' does not exists in resources")

            else:
                resp = requests.get(url, params=m)
                log.info("Response Data Received:")
                log.info(resp.json())
                assert bool(resp.json()) == True, log.error("Failed, Mandal value should be between 1 and 10 ")
        else:
            log.info("mandal is not an integer")
            resp = requests.get(url, params=m)
            assert resp.status_code == 200, log.critical(
                "Status code is not 200. Rather found :" + str(resp.status_code) + ":" + str(resp.reason))
            # The HTTP status code 500 is a generic error response. It means that the server encountered an
            # unexpected condition that prevented it from fulfilling the request.i.e., internal server error

            log.info("Response Data received:")
            log.info(resp.json())
            assert bool(resp.json()) == False, log.warning("Failed,Data is returned for invalid input")

    # Test case for sukta validation
    # test data is parameterized and saved in DataforVerses class
    @pytest.mark.parametrize("val1", DataforVerses.Sukta_Data)
    def test_GetSukta(self, val1):
        # saving the sukta parameter data in variable 's'
        s = {"sukta": val1}

        # creating logger object for the logs
        log = self.get_logger()
        log.info("**** Starting test for Sukta validation ****")
        log.info(s)

        # Checking the sukta data Type
        log.info("Sukta data type is :")
        log.info(type(s["sukta"]))

        # if the sukta is integer then only it will enter the IF block otherwise else block will be executed
        if type(s["sukta"]) is int:
            log.info("sukta is an integer")
            if s["sukta"] in range(1, 191):

                resp = requests.get(url, params=s)

                # URL check
                log.info("url is:")
                log.info(resp.url)
                assert resp.url == url + "?sukta=" + str(val1), log.error("url is not correct")

                # Status Code check
                log.info("Status code returned is:")
                log.info(resp.status_code)
                assert resp.status_code == 200, log.critical(
                    "Status code is not 200. Rather found :" + str(resp.status_code) + ":" + str(resp.reason))

                # Content-Type check
                assert 'json' in resp.headers['Content-Type'], log.error("The Content-Type is not matching")

                # type of the response received in this example it is in List format and hence its not parsed
                log.info("Response type received:")
                log.info(type(resp.json()))

                # reading the whole response received
                json_data = resp.json()
                log.info("Response Data Received:")
                log.info(json_data)

                key = "sukta"
                # checking sukta field existence and its value is same as that of requested data
                for i in range(len(json_data)):
                    if json_data[i].get(key) is not None:
                        if json_data[i]["sukta"] == val1:
                            pass
                        else:
                            log.error("Sukta is different" + str(json_data[i]["sukta"]))
                    else:
                        log.info("No, key: '{key}' does not exists in resources")

            else:
                resp = requests.get(url, params=s)
                log.info(resp.json())
                log.info(bool(resp.json()))
                assert bool(resp.json()) == True, log.error("Failed, Sukta value should be between 1 and 191")
        else:
            log.info("sukta is not an integer")
            resp = requests.get(url, params=s)
            assert resp.status_code == 200, log.critical(
                "Status code is not 200. Rather found :" + str(resp.status_code) + " : " + str(resp.reason))
            # The HTTP status code 500 is a generic error response. It means that the server encountered an
            # unexpected condition that prevented it from fulfilling the request.i.e., internal server error

            log.info("Response Data Received")
            log.info(resp.json())
            assert bool(resp.json()) == False, log.warning("Failed,Data is returned for invalid input")

    # checking if DELETE request is allowed on API or not
    # due to time constraint only DELETE request is checked
    def test_delete(self):
        resp = requests.delete(url)
        log = self.get_logger()
        log.info("**** Starting Test For Delete Request On API ****")
        log.info("Status Code returned is :")
        log.info(resp.status_code)
        log.info("Staus code reason is")
        log.info(resp.reason)
        assert resp.status_code != 200, "Delete requests are allowed"
        log.info("Success,You can make only GET calls to the API.")
