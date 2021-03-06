# coding: utf-8

"""
    BombBomb

    We make it easy to build relationships using simple videos.  # noqa: E501

    OpenAPI spec version: 2.0.831
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bombbomb.api_client import ApiClient


class AutomationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_drip_drop_stats(self, drip_id, drip_drop_id, **kwargs):  # noqa: E501
        """Get Automation Email Stats  # noqa: E501

        Get Automation Email Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_drip_drop_stats(drip_id, drip_drop_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str drip_id: The id of the drip (required)
        :param str drip_drop_id: The id of the drip drop (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_drip_drop_stats_with_http_info(drip_id, drip_drop_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_drip_drop_stats_with_http_info(drip_id, drip_drop_id, **kwargs)  # noqa: E501
            return data

    def get_drip_drop_stats_with_http_info(self, drip_id, drip_drop_id, **kwargs):  # noqa: E501
        """Get Automation Email Stats  # noqa: E501

        Get Automation Email Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_drip_drop_stats_with_http_info(drip_id, drip_drop_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str drip_id: The id of the drip (required)
        :param str drip_drop_id: The id of the drip drop (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['drip_id', 'drip_drop_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_drip_drop_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drip_id' is set
        if ('drip_id' not in params or
                params['drip_id'] is None):
            raise ValueError("Missing the required parameter `drip_id` when calling `get_drip_drop_stats`")  # noqa: E501
        # verify the required parameter 'drip_drop_id' is set
        if ('drip_drop_id' not in params or
                params['drip_drop_id'] is None):
            raise ValueError("Missing the required parameter `drip_drop_id` when calling `get_drip_drop_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'drip_id' in params:
            path_params['dripId'] = params['drip_id']  # noqa: E501
        if 'drip_drop_id' in params:
            path_params['dripDropId'] = params['drip_drop_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BBOAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/automation/{dripId}/dripdrop/{dripDropId}/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_drip_stats(self, id, **kwargs):  # noqa: E501
        """Get Automation Stats  # noqa: E501

        Get Automation Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_drip_stats(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the automation (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_drip_stats_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_drip_stats_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_drip_stats_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Automation Stats  # noqa: E501

        Get Automation Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_drip_stats_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the automation (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_drip_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_drip_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BBOAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/automation/{id}/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scheduling_status(self, id, **kwargs):  # noqa: E501
        """Get the number of pending scheduling calculations  # noqa: E501

        Get the number of pending scheduling calculations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_scheduling_status(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the automation (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_scheduling_status_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scheduling_status_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_scheduling_status_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get the number of pending scheduling calculations  # noqa: E501

        Get the number of pending scheduling calculations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_scheduling_status_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the automation (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scheduling_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_scheduling_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BBOAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/automation/{id}/scheduling/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
