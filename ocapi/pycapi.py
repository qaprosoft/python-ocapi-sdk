import json

import requests

from ocapi.lib.conf import Provider

import logging


class PyCAPI(Provider):

    """Creates and instance of the data we need to authorize our client
    and make requests to ocapi
    """

    AUTH_BASE = 'https://account.demandware.com'
    TOKEN_URL = 'https://account.demandware.com/dw/oauth2/access_token'

    def __init__(self, *args, **kwargs):
        self.data = {}
        self.data.update((key for key in kwargs.items()))

    @property
    def client_id(self):
        if self.get_properties('client_id') is not None:
            return self.get_properties('client_id')
        else:
            return self.data['client_id']

    @property
    def client_secret(self):
        if self.get_properties('client_secret') is not None:
            return self.get_properties('client_secret')
        else:
            return self.data['client_secret']

    @property
    def hostname(self):
        if self.get_properties('hostname') is not None:
            return self.get_properties('hostname')
        else:
            return self.data['hostname']

    @property
    def api_version(self):
        if self.get_properties('api_version') is not None:
            return self.get_properties('api_version')
        else:
            return self.data['api_version']

    @property
    def creds(self):
        if (self.get_properties('client_id')) and (self.get_properties('client_secret')) is not None:
            return self.get_properties('client_id'), self.get_properties('client_secret')
        else:
            return self.data['client_id'], self.data['client_secret']

    def obtain_token(self):
        # TODO: Obtain refresh token
        auth = (self.client_id, self.client_secret)
        payload = {'grant_type': 'client_credentials'}
        resp = requests.post(
            self.TOKEN_URL,
            auth=auth,
            data=payload,
        )
        try:
            token = resp.json()['access_token']
            expires_in = resp.json()['expires_in']
            logging.info('Authorization Sucessful')
            return token, expires_in
        except Exception as e:
            logging.exception('\n\nCAN\'T REACH API!\n\n %s ' %  (json.dumps(resp.json(), indent=2) + '\n'))

    def headers(self, access_token):
        token = access_token
        if not access_token:
            token, expires_in = self.obtain_token()

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer {0}'.format(token),
            'x-dw-client-id': self.client_id,
        }
        return headers
