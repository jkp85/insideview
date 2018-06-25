# coding: utf-8

from tapioca import TapiocaAdapter, JSONAdapterMixin
from requests.auth import AuthBase

from .custom import TapiocaInstantiator

from .resource_mapping import RESOURCE_MAPPING


class InsideViewAuth(AuthBase):
    def __init__(self, access_token):
        self.access_token = access_token

    def __call__(self, r):
        r.headers['accessToken'] = self.access_token
        return r


class InsideViewClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.insideview.com/api/v1'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        arguments = super().get_request_kwargs(api_params, *args, **kwargs)
        arguments['headers']['Content-Type'] = 'application/x-www-form-urlencoded'
        arguments['headers']['accept'] = 'application/json'
        arguments['auth'] = InsideViewAuth(api_params.get('access_token'))
        return arguments

    def get_iterator_list(self, response_data):
        std_keys = {'totalResults', 'page', 'resultsPerPage'}
        key = next(key for key in response_data.keys() if key not in std_keys)
        return response_data[key]

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        page = response_data.get('page')
        if page:
            page = int(page) + 1
            return {'page': page}


InsideView = TapiocaInstantiator(InsideViewClientAdapter)
