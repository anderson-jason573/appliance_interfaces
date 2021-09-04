"""
*****************************************************************************
This module creates an object, that will be used for the various classes and 
methods needed for desired API calls.

The methods in this module will login and logout of API sessions with 
the Orchestrator.
*****************************************************************************
"""

import requests
import json
import sys
from api_methods import ApiMethods
from appliance_info import ApplianceInfo
from log_file import LogFile

class OrchHelper:
    """ creates object for use in the various classes and methods for
    API calls """
    
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password
        self.url_prefix = "https://" + url + "/gms/rest"
        self.session = requests.Session()
        self.headers = {}
        self.parameters = []
        self.apiSrcId = "?source=menu_rest_apis_id"  # for API calls w/ just source as query param
        self.apiSrcId2 = "&source=menu_rest_apis_id"  # for API calls w/ multiple query params
        self.supportedAuthModes = ["local", "radius",
                                   "tacacs"]  # remote authentication modes supported via this helper module
        self.authMode = "local"  # change this to the desired auth mode before invoking login() function.
        requests.packages.urllib3.disable_warnings()  # disable certificate warning messages

    def login(self):
        
        """
        # Basic login function without multi-factor authentication
        # NOTE: if the userId is using RBAC, they must have R/O or R/W access
            to the REST API functionality to access the APIs
        # Returns True if login succeeds, False if exception raised or
            failure to login """

        if self.authMode not in self.supportedAuthModes:
            print("{0}: authentication mode not supported".format(self.authMode))
            return False

        try:
            r = ApiMethods.post_login("/authentication/login", self)
            if r.status_code == 200:
                print('\n' + ''"{0}: Orchestrator login success".format(self.url))
                # get and set X-XSRF-TOKEN
                for cookie in r.cookies:
                    if cookie.name == "orchCsrfToken":
                        self.headers["X-XSRF-TOKEN"] = cookie.value
                # get and set login cookies
                self.cookies = r.cookies
                site_detail = ApplianceInfo.get_appliances(self) # Pass OrchHelper object to get_appliances method in appliancinfo.py
                return site_detail
            else:
                sys.exit("Orchestrator login failed: Response Code <{0}>, {1}"
                         .format(r.status_code, r.text))

        except Exception as err:
            LogFile.log_error(err)

    def mfa_login(self, mfacode):

        """
        # alternative login function for multi-factor authentication
        # mfacode is integer value that is provided by Orchestrator after providing initial userid and passwd
        # To use mfa_login, first request the mfacode using send_mfa(). An MFA code will be sent depending on how the user is configured.
        # Then call this function with the provided MFA code.
        #
        # NOTE: if the userId is using RBAC, they must have R/O or R/W access to the REST API functionality to access the APIs
        # Returns True if login succeeds, False if exception raised or failure to login
        """

        try:

            response = self.post("/authentication/login",
                                 {"user": self.user, "password": self.password, "token": int(mfacode)})
            if response.status_code == 200:
                print("{0}: Orchestrator MFA login success".format(self.url))
                # get and set X-XSRF-TOKEN
                for cookie in response.cookies:
                    if cookie.name == "orchCsrfToken":
                        self.headers["X-XSRF-TOKEN"] = cookie.value
                return True
            else:
                print("{0}: Orchestrator MFA login failed: {1}".format(self.url, response.text))
                return False
        except:
            print("{0}: Exception - unable to connect to Orchestrator".format(self.url))
            return False

    def send_mfa(self):
        
        """
        # send request to Orchestrator to issue MFA token to user
        # returns True on success, False on failure or exception
        """

        try:
            response = self.post("/authentication/loginToken",
                                 {"user": self.user, "password": self.password, "TempCode": True})
        except:
            print("Exception - unable to submit token request")
            return False
        return True if response.status_code in [200, 204] else False

    def logout(self):
        try:
            r = ApiMethods.get_orch("/authentication/logout", self)
            if r.status_code == 200:
                print('\n' + "{0}: Orchestrator logout success".format(self.url))
            else:
                print('\n' + "{0}: Orchestrator logout failed: {1}".format(self.url, r.text))
        except:
            print('\n' + "{0}: Exception - unable to logout of Orchestrator".format(self.url))

#end
