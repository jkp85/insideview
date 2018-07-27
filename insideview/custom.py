from urllib.parse import parse_qsl
from tapioca.tapioca import TapiocaClient, TapiocaClientExecutor


class CustomTapiocaClient(TapiocaClient):
    def _wrap_in_tapioca(self, data, *args, **kwargs):
        request_kwargs = kwargs.pop('request_kwargs', self._request_kwargs)
        return CustomTapiocaClient(self._instatiate_api(), data=data,
                                   api_params=self._api_params,
                                   request_kwargs=request_kwargs,
                                   refresh_token_by_default=self._refresh_token_default,
                                   refresh_data=self._refresh_data,
                                   session=self._session,
                                   *args, **kwargs)

    def _wrap_in_tapioca_executor(self, data, *args, **kwargs):
        request_kwargs = kwargs.pop('request_kwargs', self._request_kwargs)
        return CustomTapiocaClientExecutor(self._instatiate_api(), data=data,
                                           api_params=self._api_params,
                                           request_kwargs=request_kwargs,
                                           refresh_token_by_default=self._refresh_token_default,
                                           refresh_data=self._refresh_data,
                                           session=self._session,
                                           *args, **kwargs)


class CustomTapiocaClientExecutor(CustomTapiocaClient, TapiocaClientExecutor):
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

            if not next_request_kwargs:
                break

            req = self._response.request
            if req.method == 'POST':
                body = dict(parse_qsl(req.body))
                body.update(next_request_kwargs)
                response = self.post(data=body, url=req.url)
            else:
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
