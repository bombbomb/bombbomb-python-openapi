# coding: utf-8

"""
    BombBomb

    We make it easy to build relationships using simple videos.

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class IntegrationsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def connect_integration(self, code, **kwargs):
        """
        Activate an integration for a user.
        Provide the correct parameters to enable an integration. Required Parameters vary based on the desired          integration. Integrations requiring OAuth will provide the OAuth link that the user must be presented.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connect_integration(code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str code: The identifier of the integration. (required)
        :param str key: The key value.
        :param str secret: The secret value.
        :param str token: The token value.
        :param str data: The data value as JSON.
        :param str overwrite: Boolean value to know whether or not to delete the integration if it already exists
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.connect_integration_with_http_info(code, **kwargs)
        else:
            (data) = self.connect_integration_with_http_info(code, **kwargs)
            return data

    def connect_integration_with_http_info(self, code, **kwargs):
        """
        Activate an integration for a user.
        Provide the correct parameters to enable an integration. Required Parameters vary based on the desired          integration. Integrations requiring OAuth will provide the OAuth link that the user must be presented.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connect_integration_with_http_info(code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str code: The identifier of the integration. (required)
        :param str key: The key value.
        :param str secret: The secret value.
        :param str token: The token value.
        :param str data: The data value as JSON.
        :param str overwrite: Boolean value to know whether or not to delete the integration if it already exists
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'key', 'secret', 'token', 'data', 'overwrite']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connect_integration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params) or (params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `connect_integration`")

        resource_path = '/integrations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'code' in params:
            form_params.append(('code', params['code']))
        if 'key' in params:
            form_params.append(('key', params['key']))
        if 'secret' in params:
            form_params.append(('secret', params['secret']))
        if 'token' in params:
            form_params.append(('token', params['token']))
        if 'data' in params:
            form_params.append(('data', params['data']))
        if 'overwrite' in params:
            form_params.append(('overwrite', params['overwrite']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['BBOAuth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delete_integration(self, **kwargs):
        """
        Remove an integration for a user.
        Remove an integration by providing the integration id or integration code. Only provide one of the             parameters.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_integration(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Integration ID
        :param str code: Integration Code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_integration_with_http_info(**kwargs)
        else:
            (data) = self.delete_integration_with_http_info(**kwargs)
            return data

    def delete_integration_with_http_info(self, **kwargs):
        """
        Remove an integration for a user.
        Remove an integration by providing the integration id or integration code. Only provide one of the             parameters.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_integration_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Integration ID
        :param str code: Integration Code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'code']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_integration" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/integrations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id' in params:
            form_params.append(('id', params['id']))
        if 'code' in params:
            form_params.append(('code', params['code']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['BBOAuth2']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_integration_health(self, code, **kwargs):
        """
        Get health for a given integration
        Get health for an integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_integration_health(code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str code: The integration code for which to retrieve the information from (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_integration_health_with_http_info(code, **kwargs)
        else:
            (data) = self.get_integration_health_with_http_info(code, **kwargs)
            return data

    def get_integration_health_with_http_info(self, code, **kwargs):
        """
        Get health for a given integration
        Get health for an integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_integration_health_with_http_info(code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str code: The integration code for which to retrieve the information from (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_integration_health" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params) or (params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_integration_health`")

        resource_path = '/integrations/health/{code}'.replace('{format}', 'json')
        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['BBOAuth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_integration_page_components(self, integration_name, **kwargs):
        """
        Get page components for a given integration
        Get all page components for an integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_integration_page_components(integration_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_name: The integration for which to retrieve HTML page components. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_integration_page_components_with_http_info(integration_name, **kwargs)
        else:
            (data) = self.get_integration_page_components_with_http_info(integration_name, **kwargs)
            return data

    def get_integration_page_components_with_http_info(self, integration_name, **kwargs):
        """
        Get page components for a given integration
        Get all page components for an integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_integration_page_components_with_http_info(integration_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_name: The integration for which to retrieve HTML page components. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_integration_page_components" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_name' is set
        if ('integration_name' not in params) or (params['integration_name'] is None):
            raise ValueError("Missing the required parameter `integration_name` when calling `get_integration_page_components`")

        resource_path = '/integrations/pageComponents'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'integration_name' in params:
            query_params['integration_name'] = params['integration_name']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['BBOAuth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def sync_users_integrated_lists(self, **kwargs):
        """
        Synchronize your integration list or lists.
        Synchronize your integration contact list with the service you are integrated with. If no integration code is provided, all integrations will be synchronized.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sync_users_integrated_lists(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: The integration to sync lists for. All integrations will sync if nothing is provided.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sync_users_integrated_lists_with_http_info(**kwargs)
        else:
            (data) = self.sync_users_integrated_lists_with_http_info(**kwargs)
            return data

    def sync_users_integrated_lists_with_http_info(self, **kwargs):
        """
        Synchronize your integration list or lists.
        Synchronize your integration contact list with the service you are integrated with. If no integration code is provided, all integrations will be synchronized.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sync_users_integrated_lists_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: The integration to sync lists for. All integrations will sync if nothing is provided.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sync_users_integrated_lists" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/integrations/sync'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'integration_id' in params:
            query_params['integration_id'] = params['integration_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['BBOAuth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
