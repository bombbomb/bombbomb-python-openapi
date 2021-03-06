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


class FilesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def doc_host_delete(self, doc_id, **kwargs):  # noqa: E501
        """Delete file  # noqa: E501

        Deletes a users file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.doc_host_delete(doc_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str doc_id: Id of document (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.doc_host_delete_with_http_info(doc_id, **kwargs)  # noqa: E501
        else:
            (data) = self.doc_host_delete_with_http_info(doc_id, **kwargs)  # noqa: E501
            return data

    def doc_host_delete_with_http_info(self, doc_id, **kwargs):  # noqa: E501
        """Delete file  # noqa: E501

        Deletes a users file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.doc_host_delete_with_http_info(doc_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str doc_id: Id of document (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['doc_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method doc_host_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'doc_id' is set
        if ('doc_id' not in params or
                params['doc_id'] is None):
            raise ValueError("Missing the required parameter `doc_id` when calling `doc_host_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'doc_id' in params:
            path_params['docId'] = params['doc_id']  # noqa: E501

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
            '/files/{docId}', 'DELETE',
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

    def doc_host_get(self, doc_id, **kwargs):  # noqa: E501
        """Get file  # noqa: E501

        Get a single file by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.doc_host_get(doc_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str doc_id: Id of document (required)
        :return: HostedDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.doc_host_get_with_http_info(doc_id, **kwargs)  # noqa: E501
        else:
            (data) = self.doc_host_get_with_http_info(doc_id, **kwargs)  # noqa: E501
            return data

    def doc_host_get_with_http_info(self, doc_id, **kwargs):  # noqa: E501
        """Get file  # noqa: E501

        Get a single file by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.doc_host_get_with_http_info(doc_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str doc_id: Id of document (required)
        :return: HostedDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['doc_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method doc_host_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'doc_id' is set
        if ('doc_id' not in params or
                params['doc_id'] is None):
            raise ValueError("Missing the required parameter `doc_id` when calling `doc_host_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'doc_id' in params:
            path_params['docId'] = params['doc_id']  # noqa: E501

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
            '/files/{docId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HostedDoc',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def doc_host_list(self, **kwargs):  # noqa: E501
        """List all files  # noqa: E501

        List all uploaded user files  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.doc_host_list(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[HostedDoc]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.doc_host_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.doc_host_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def doc_host_list_with_http_info(self, **kwargs):  # noqa: E501
        """List all files  # noqa: E501

        List all uploaded user files  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.doc_host_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[HostedDoc]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method doc_host_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/files', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[HostedDoc]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def doc_host_upload_v2(self, file, **kwargs):  # noqa: E501
        """Upload a file  # noqa: E501

        Upload a new file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.doc_host_upload_v2(file, async=True)
        >>> result = thread.get()

        :param async bool
        :param str file: The file being uploaded (required)
        :return: list[HostedDoc]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.doc_host_upload_v2_with_http_info(file, **kwargs)  # noqa: E501
        else:
            (data) = self.doc_host_upload_v2_with_http_info(file, **kwargs)  # noqa: E501
            return data

    def doc_host_upload_v2_with_http_info(self, file, **kwargs):  # noqa: E501
        """Upload a file  # noqa: E501

        Upload a new file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.doc_host_upload_v2_with_http_info(file, async=True)
        >>> result = thread.get()

        :param async bool
        :param str file: The file being uploaded (required)
        :return: list[HostedDoc]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method doc_host_upload_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `doc_host_upload_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            form_params.append(('file', params['file']))  # noqa: E501

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
            '/files', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[HostedDoc]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_hosted_images_paged(self, page_size, page, **kwargs):  # noqa: E501
        """Get paged hosted images  # noqa: E501

        Get a specific page of uploaded images available to the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_hosted_images_paged(page_size, page, async=True)
        >>> result = thread.get()

        :param async bool
        :param str page_size: The number of items to retrieve in a single db query. (required)
        :param str page: Zero-based index of the page of data to retrieve from the db. (required)
        :param str search: Filter results with names that match the search term.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_hosted_images_paged_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_hosted_images_paged_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_hosted_images_paged_with_http_info(self, page_size, page, **kwargs):  # noqa: E501
        """Get paged hosted images  # noqa: E501

        Get a specific page of uploaded images available to the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_hosted_images_paged_with_http_info(page_size, page, async=True)
        >>> result = thread.get()

        :param async bool
        :param str page_size: The number of items to retrieve in a single db query. (required)
        :param str page: Zero-based index of the page of data to retrieve from the db. (required)
        :param str search: Filter results with names that match the search term.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', 'search']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hosted_images_paged" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_hosted_images_paged`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_hosted_images_paged`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501

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
            '/files/images/paged', 'GET',
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
