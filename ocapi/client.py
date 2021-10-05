import json

import requests
from requests_oauthlib import OAuth2Session

from ocapi.pycapi import PyCAPI

import logging


class ShopAPI(PyCAPI):

    """A module to wrap portions of the OCAPI API using Python

    References:

        https://github.com/ashishkumar-tudip/python-demandware-sdk
        https://api-explorer.commercecloud.salesforce.com
        https://sforce.co/2MgMiXZ
    """

    def __init__(self, *args, **kwargs):
        self.ocapi = PyCAPI(**kwargs)
        self.API_TYPE = 'dw/shop'


    def api_url(self, site_id='-'):
        return 'https://{0}/s/{1}/{2}/{3}'.format(
            self.ocapi.hostname,
            site_id,
            self.API_TYPE,
            self.ocapi.api_version
    )


    def get_access_token(self):
        return self.ocapi.obtain_token()

    def product_search(self, site_id, query, access_token=None, **kwargs):
        """
        https://sforce.co/3dmLuwV
        """

        parameters = ""

        for key in kwargs:
            parameters += '&' + str(key) + '=' + str(kwargs.get(key))

        api_url = self.api_url(site_id)
        endpoint = '/product_search?q={0}&client_id={1}{2}'.format(query, self.ocapi.client_id, parameters)
        request_url = '{0}{1}'.format(api_url, endpoint)
        res = requests.get(
            request_url,
            headers=self.ocapi.headers(access_token),
            timeout=30,
        )
        logging.debug(json.dumps(res.json(), indent=2))
        try:
            hits = res.json()['hits']
            logging.info(json.dumps(hits, indent=2))
            return hits, res.json()['total']
        except Exception as e:
            logging.exception('\n\n')


    def site(self):
        """
        https://sforce.co/3dn5KP1
        """


    def auth(self):
        # WIP
        endpoint = '/customers/auth?client_id={0}'.format(self.ocapi.client_id)
        request_url = '{0}{1}'.format(self.api_url, endpoint)
        payload = {'type': 'credentials'}
        req = requests.post(
            request_url,
            headers=self.ocapi.headers,
            auth=self.creds,
            json=payload,
        )


    def customer(self):
        # WIP
        endpoint = '/customers?client_id={0}'.format(self.ocapi.client_id)
        request_url = '{0}{1}'.format(self.api_url, endpoint)
        payload = {
            "password":"abcd1234$$",
                "customer": {
                "login": "ocapi.qa",
                "email":"ocapiguya001@mailinator.com",
                "last_name":"Ocapi"
            }
        }
        req = requests.post(
            request_url,
            headers=self.ocapi.headers,
            json=payload,
            timeout=30,
        )
        logging.info(json.dumps(req.json(), indent=2))
        print(json.dumps(req.json(), indent=2))


class DataAPI(PyCAPI):

    def __init__(self, *args, **kwargs):
        self.ocapi = PyCAPI(**kwargs)
        self.API_TYPE = 'dw/data'


    def api_url(self, site_id='-'):
        return 'https://{0}/s/{1}/{2}/{3}'.format(
            self.ocapi.hostname,
            site_id,
            self.API_TYPE,
            self.ocapi.api_version
    )