"""
***************************************************************************
This module contains the API methods, for API calls.  OrchHelper object
gets passed to each API method, depending on the type of call - i.e.
'POST', 'GET', 'PUT', 'DELETE'.

There are two 'GET'methods, depending on the type of call to Orchestrator.
If it is a direct call to an Orchestrator API, then 'get_orch' is the 
method to call.  If it is a direct call to an appliance, which is front
ended by Orchestrator, then 'get_appl' should be used.
***************************************************************************
"""

import requests

class ApiMethods:

    """ Methods for API calls """

    @classmethod
    def post_login(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        data = {"user": obj.user, "password": obj.password,
                "loginType": obj.supportedAuthModes.index(obj.authMode)}
        return obj.session.post(obj.url_prefix + url + apiSrcStr, json=data,
                                verify=False, timeout=120,
                                headers=obj.headers)

    @classmethod
    def post_orch(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.post(obj.url_prefix + url + apiSrcStr,
                               verify=False, timeout=120,
                               headers=obj.headers, json=obj.parameters)

    @classmethod
    def get_orch(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.get(obj.url_prefix + url + apiSrcStr, verify=False,
                               timeout=120, headers=obj.headers)

    @classmethod
    def get_appl(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.get(obj.url_prefix + url + apiSrcStr, verify=False,
                               timeout=120, headers=obj.headers,
                               cookies=obj.cookies)

    @classmethod
    def delete(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.delete(obj.url_prefix + url + apiSrcStr,
                                  verify=False, timeout=120,
                                  headers=obj.headers)

    @classmethod
    def put(cls, url, obj):
        apiSrcStr = obj.apiSrcId if ("?" not in url) else obj.apiSrcId2
        return obj.session.put(obj.url_prefix + url + apiSrcStr, json=data,
                               verify=False, timeout=120,
                                headers=obj.headers)

