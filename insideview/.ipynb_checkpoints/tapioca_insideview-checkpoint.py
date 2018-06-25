# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)
from tapioca.tapioca import TapiocaClient
from requests.auth import AuthBase

from .resource_mapping import RESOURCE_MAPPING


class InsideViewAuth(AuthBase):
    def __init__(self, access_token):
        self.access_token = access_token

    def __call__(self, r):
        r.headers['accessToken'] = self.access_token
        return r


class CustomTapiocaClient(TapiocaClient):

    def pages(self, max_pages=None, max_items=None, **kwargs):
        executor = self
        iterator_list = executor._get_iterator_list()
        page_count = 0
        item_count = 0

        while iterator_list:
            if self._reached_max_limits(page_count, item_count, max_pages,
                                        max_items):
                break
            for item in iterator_list:
                if self._reached_max_limits(page_count, item_count, max_pages,
                                            max_items):
                    break
                yield self._wrap_in_tapioca(item)
                item_count += 1

            page_count += 1

            next_request_kwargs = executor._get_iterator_next_request_kwargs()
            import ipdb;ipdb.set_trace()

            if not next_request_kwargs:
                break

            response = self.get(**next_request_kwargs)
            executor = response()
            iterator_list = executor._get_iterator_list()


class TapiocaInstantiator:
    def __init__(self, adapter_class):
        self.adapter_class = adapter_class

    def __call__(self, serializer_class=None, session=None, **kwargs):
        refresh_token_default = kwargs.pop('refresh_token_by_default', False)
        return CustomTapiocaClient(
            self.adapter_class(serializer_class=serializer_class),
            api_params=kwargs, refresh_token_by_default=refresh_token_default,
            session=session)


class InsideviewClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.insideview.com/api/v1/'
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
        results_per_page = response_data.get('resultsPerPage')
        if page:
            page = int(page) + 1
        return {'page': page, 'resultsPerPage': results_per_page}


Insideview = TapiocaInstantiator(InsideviewClientAdapter)
