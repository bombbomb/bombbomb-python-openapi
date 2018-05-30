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


class VideosApi(object):
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

    def get_video_encoding_status(self, video_id, **kwargs):
        """
        Video Encoding Status
        Get information about the current state of encoding for a given video id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_encoding_status(video_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str video_id: The video's id. (required)
        :return: VideoEncodingStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_video_encoding_status_with_http_info(video_id, **kwargs)
        else:
            (data) = self.get_video_encoding_status_with_http_info(video_id, **kwargs)
            return data

    def get_video_encoding_status_with_http_info(self, video_id, **kwargs):
        """
        Video Encoding Status
        Get information about the current state of encoding for a given video id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_encoding_status_with_http_info(video_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str video_id: The video's id. (required)
        :return: VideoEncodingStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_encoding_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params) or (params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `get_video_encoding_status`")

        resource_path = '/videos/{videoId}/status'.replace('{format}', 'json')
        path_params = {}
        if 'video_id' in params:
            path_params['videoId'] = params['video_id']

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
                                            response_type='VideoEncodingStatusResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_video_recorder(self, **kwargs):
        """
        Get Live Video Recorder HTML
        Returns an object with a number of properties to help you put a video recorder on your site.         This is to be used in conjunction with the VideoRecordedLive call one the user has confirmed in your UI that         the video is how they want it.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_recorder(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int width: The width of the recorder to present.
        :param str video_id: The id of the video to record
        :return: VideoRecorderMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_video_recorder_with_http_info(**kwargs)
        else:
            (data) = self.get_video_recorder_with_http_info(**kwargs)
            return data

    def get_video_recorder_with_http_info(self, **kwargs):
        """
        Get Live Video Recorder HTML
        Returns an object with a number of properties to help you put a video recorder on your site.         This is to be used in conjunction with the VideoRecordedLive call one the user has confirmed in your UI that         the video is how they want it.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_recorder_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int width: The width of the recorder to present.
        :param str video_id: The id of the video to record
        :return: VideoRecorderMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['width', 'video_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_recorder" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/videos/live/getRecorder'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'width' in params:
            query_params['width'] = params['width']
        if 'video_id' in params:
            query_params['videoId'] = params['video_id']

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
                                            response_type='VideoRecorderMethodResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def mark_live_recording_complete(self, video_id, filename, title, **kwargs):
        """
        Completes a live recording
        Used in conjunction with the live recorder method to mark a video recording as complete.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mark_live_recording_complete(video_id, filename, title, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str video_id: The id of the video to mark as done. (required)
        :param str filename: The filename that was chosen as the final video. (required)
        :param str title: The title to give the video (required)
        :return: VideoPublicRepresentation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.mark_live_recording_complete_with_http_info(video_id, filename, title, **kwargs)
        else:
            (data) = self.mark_live_recording_complete_with_http_info(video_id, filename, title, **kwargs)
            return data

    def mark_live_recording_complete_with_http_info(self, video_id, filename, title, **kwargs):
        """
        Completes a live recording
        Used in conjunction with the live recorder method to mark a video recording as complete.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mark_live_recording_complete_with_http_info(video_id, filename, title, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str video_id: The id of the video to mark as done. (required)
        :param str filename: The filename that was chosen as the final video. (required)
        :param str title: The title to give the video (required)
        :return: VideoPublicRepresentation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'filename', 'title']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mark_live_recording_complete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params) or (params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `mark_live_recording_complete`")
        # verify the required parameter 'filename' is set
        if ('filename' not in params) or (params['filename'] is None):
            raise ValueError("Missing the required parameter `filename` when calling `mark_live_recording_complete`")
        # verify the required parameter 'title' is set
        if ('title' not in params) or (params['title'] is None):
            raise ValueError("Missing the required parameter `title` when calling `mark_live_recording_complete`")

        resource_path = '/videos/live/markComplete'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'video_id' in params:
            form_params.append(('videoId', params['video_id']))
        if 'filename' in params:
            form_params.append(('filename', params['filename']))
        if 'title' in params:
            form_params.append(('title', params['title']))

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
                                            response_type='VideoPublicRepresentation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def sign_upload(self, policy, **kwargs):
        """
        Generate Signed Url
        Generates a signed url to be used for video uploads.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sign_upload(policy, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SignUploadRequest policy: The policy to sign (required)
        :param bool v4: Whether to do v4 signing
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sign_upload_with_http_info(policy, **kwargs)
        else:
            (data) = self.sign_upload_with_http_info(policy, **kwargs)
            return data

    def sign_upload_with_http_info(self, policy, **kwargs):
        """
        Generate Signed Url
        Generates a signed url to be used for video uploads.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sign_upload_with_http_info(policy, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SignUploadRequest policy: The policy to sign (required)
        :param bool v4: Whether to do v4 signing
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy', 'v4']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sign_upload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy' is set
        if ('policy' not in params) or (params['policy'] is None):
            raise ValueError("Missing the required parameter `policy` when calling `sign_upload`")

        resource_path = '/video/signedUpload'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'v4' in params:
            form_params.append(('v4', params['v4']))

        body_params = None
        if 'policy' in params:
            body_params = params['policy']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
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

    def update_video_thumbnail_v2(self, video_id, thumbnail, **kwargs):
        """
        Upload thumbnail
        Upload a new video thumbnail

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_video_thumbnail_v2(video_id, thumbnail, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str video_id: The id of the video (required)
        :param str thumbnail: The thumbnail being uploaded (required)
        :param bool custom: The default email to use.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_video_thumbnail_v2_with_http_info(video_id, thumbnail, **kwargs)
        else:
            (data) = self.update_video_thumbnail_v2_with_http_info(video_id, thumbnail, **kwargs)
            return data

    def update_video_thumbnail_v2_with_http_info(self, video_id, thumbnail, **kwargs):
        """
        Upload thumbnail
        Upload a new video thumbnail

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_video_thumbnail_v2_with_http_info(video_id, thumbnail, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str video_id: The id of the video (required)
        :param str thumbnail: The thumbnail being uploaded (required)
        :param bool custom: The default email to use.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'thumbnail', 'custom']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_video_thumbnail_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params) or (params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `update_video_thumbnail_v2`")
        # verify the required parameter 'thumbnail' is set
        if ('thumbnail' not in params) or (params['thumbnail'] is None):
            raise ValueError("Missing the required parameter `thumbnail` when calling `update_video_thumbnail_v2`")

        resource_path = '/videos/thumbnail'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'video_id' in params:
            form_params.append(('videoId', params['video_id']))
        if 'custom' in params:
            form_params.append(('custom', params['custom']))
        if 'thumbnail' in params:
            form_params.append(('thumbnail', params['thumbnail']))

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

        return self.api_client.call_api(resource_path, 'PUT',
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
