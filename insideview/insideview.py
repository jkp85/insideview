# coding: utf-8

import os
import logging
import requests

from requests.auth import AuthBase

from typing import Dict
from urllib.parse import urlencode
from tapioca import TapiocaAdapter, JSONAdapterMixin

from urllib.parse import urlencode

from .custom import TapiocaInstantiator
from .resource_mapping import RESOURCE_MAPPING

logger = logging.getLogger("insideview")

def get_insideview_access_token() -> str:
    """
    Use InsideView client id and secret key for an API access token.
    :return: InsideView API token
    """
    url = (f"https://login.insideview.com/Auth/login/v1/token.json"
           f"?clientId={os.getenv('INSIDE_VIEW_CLIENT_ID')}"
           f"&clientSecret={os.getenv('INSIDE_VIEW_CLIENT_SECRET')}"
           f"&grantType=cred")
    logger.debug(f"Retrieving access token {url}")
    response = requests.post(url)
    response.raise_for_status()
    return response.json()['accessTokenDetails']['accessToken']


class InsideViewAuth(AuthBase):
    """
    Class used to get a valid InsideView auth token when instantiating
    object.
    """
    def __init__(self, access_token):
        self.access_token = access_token

    def __call__(self, r):
        r.headers['accessToken'] = self.access_token
        return r


class InsideViewClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    """
    Class to manage InsideView authentication and data with requests and
    reponses.
    """
    api_root = 'https://api.insideview.com/api/v1'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        """Get key/value pairs from headers"""
        arguments = TapiocaAdapter.get_request_kwargs(
            self, api_params, *args, **kwargs)
        if 'headers' not in arguments:
            arguments['headers'] = {}
            arguments['headers']['Content-Type'] = 'application/x-www-form-urlencoded'
        arguments['headers']['accept'] = 'application/json'
        arguments['auth'] = InsideViewAuth(api_params.get('access_token'))
        return arguments

    def get_iterator_list(self, response_data):
        """Method to handle InsideView pagination."""
        std_keys = {'totalResults', 'page', 'resultsPerPage'}
        key = next(key for key in response_data.keys() if key not in std_keys)
        return response_data[key]

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        """Get next page from InsideView reponse."""
        page = response_data.get('page')
        if page:
            page = int(page) + 1
            return {'page': page}

    def format_data_to_request(self, data):
        """Formats data for url encoded values."""
        if data:
            if hasattr(data, 'read'):
                return data
            return urlencode(data)

    def response_to_native(self, response):
        """Send response contant with originl InsideView formt. Otherwise
        resort to default json responses."""
        if 'Content-Disposition' in response.headers:
            return response.content
        return response.json()


InsideView = TapiocaInstantiator(InsideViewClientAdapter)
