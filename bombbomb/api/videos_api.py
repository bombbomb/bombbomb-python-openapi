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


class VideosApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_video_encoding_status(self, video_id, **kwargs):  # noqa: E501
        """Video Encoding Status  # noqa: E501

        Get information about the current state of encoding for a given video id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_video_encoding_status(video_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str video_id: The video's id. (required)
        :return: VideoEncodingStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_video_encoding_status_with_http_info(video_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_video_encoding_status_with_http_info(video_id, **kwargs)  # noqa: E501
            return data

    def get_video_encoding_status_with_http_info(self, video_id, **kwargs):  # noqa: E501
        """Video Encoding Status  # noqa: E501

        Get information about the current state of encoding for a given video id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_video_encoding_status_with_http_info(video_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str video_id: The video's id. (required)
        :return: VideoEncodingStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_encoding_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params or
                params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `get_video_encoding_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'video_id' in params:
            path_params['videoId'] = params['video_id']  # noqa: E501

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
            '/videos/{videoId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VideoEncodingStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_video_recorder(self, **kwargs):  # noqa: E501
        """Get Live Video Recorder HTML  # noqa: E501

        Returns an object with a number of properties to help you put a video recorder on your site.         This is to be used in conjunction with the VideoRecordedLive call one the user has confirmed in your UI that         the video is how they want it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_video_recorder(async=True)
        >>> result = thread.get()

        :param async bool
        :param int width: The width of the recorder to present.
        :param str video_id: The id of the video to record
        :return: VideoRecorderMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_video_recorder_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_video_recorder_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_video_recorder_with_http_info(self, **kwargs):  # noqa: E501
        """Get Live Video Recorder HTML  # noqa: E501

        Returns an object with a number of properties to help you put a video recorder on your site.         This is to be used in conjunction with the VideoRecordedLive call one the user has confirmed in your UI that         the video is how they want it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_video_recorder_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int width: The width of the recorder to present.
        :param str video_id: The id of the video to record
        :return: VideoRecorderMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['width', 'video_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_recorder" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501
        if 'video_id' in params:
            query_params.append(('videoId', params['video_id']))  # noqa: E501

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
            '/videos/live/getRecorder', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VideoRecorderMethodResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def mark_live_recording_complete(self, video_id, filename, title, **kwargs):  # noqa: E501
        """Completes a live recording  # noqa: E501

        Used in conjunction with the live recorder method to mark a video recording as complete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.mark_live_recording_complete(video_id, filename, title, async=True)
        >>> result = thread.get()

        :param async bool
        :param str video_id: The id of the video to mark as done. (required)
        :param str filename: The filename that was chosen as the final video. (required)
        :param str title: The title to give the video (required)
        :return: VideoPublicRepresentation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.mark_live_recording_complete_with_http_info(video_id, filename, title, **kwargs)  # noqa: E501
        else:
            (data) = self.mark_live_recording_complete_with_http_info(video_id, filename, title, **kwargs)  # noqa: E501
            return data

    def mark_live_recording_complete_with_http_info(self, video_id, filename, title, **kwargs):  # noqa: E501
        """Completes a live recording  # noqa: E501

        Used in conjunction with the live recorder method to mark a video recording as complete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.mark_live_recording_complete_with_http_info(video_id, filename, title, async=True)
        >>> result = thread.get()

        :param async bool
        :param str video_id: The id of the video to mark as done. (required)
        :param str filename: The filename that was chosen as the final video. (required)
        :param str title: The title to give the video (required)
        :return: VideoPublicRepresentation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'filename', 'title']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mark_live_recording_complete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params or
                params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `mark_live_recording_complete`")  # noqa: E501
        # verify the required parameter 'filename' is set
        if ('filename' not in params or
                params['filename'] is None):
            raise ValueError("Missing the required parameter `filename` when calling `mark_live_recording_complete`")  # noqa: E501
        # verify the required parameter 'title' is set
        if ('title' not in params or
                params['title'] is None):
            raise ValueError("Missing the required parameter `title` when calling `mark_live_recording_complete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'video_id' in params:
            form_params.append(('videoId', params['video_id']))  # noqa: E501
        if 'filename' in params:
            form_params.append(('filename', params['filename']))  # noqa: E501
        if 'title' in params:
            form_params.append(('title', params['title']))  # noqa: E501

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
            '/videos/live/markComplete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VideoPublicRepresentation',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sign_upload(self, policy, **kwargs):  # noqa: E501
        """Generate Signed Url  # noqa: E501

        Generates a signed url to be used for video uploads.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sign_upload(policy, async=True)
        >>> result = thread.get()

        :param async bool
        :param SignUploadRequest policy: The policy to sign (required)
        :param bool v4: Whether to do v4 signing
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.sign_upload_with_http_info(policy, **kwargs)  # noqa: E501
        else:
            (data) = self.sign_upload_with_http_info(policy, **kwargs)  # noqa: E501
            return data

    def sign_upload_with_http_info(self, policy, **kwargs):  # noqa: E501
        """Generate Signed Url  # noqa: E501

        Generates a signed url to be used for video uploads.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sign_upload_with_http_info(policy, async=True)
        >>> result = thread.get()

        :param async bool
        :param SignUploadRequest policy: The policy to sign (required)
        :param bool v4: Whether to do v4 signing
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy', 'v4']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sign_upload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy' is set
        if ('policy' not in params or
                params['policy'] is None):
            raise ValueError("Missing the required parameter `policy` when calling `sign_upload`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'v4' in params:
            form_params.append(('v4', params['v4']))  # noqa: E501

        body_params = None
        if 'policy' in params:
            body_params = params['policy']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/video/signedUpload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_video_thumbnail_v2(self, video_id, thumbnail, **kwargs):  # noqa: E501
        """Upload thumbnail  # noqa: E501

        Upload a new video thumbnail  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_video_thumbnail_v2(video_id, thumbnail, async=True)
        >>> result = thread.get()

        :param async bool
        :param str video_id: The id of the video (required)
        :param str thumbnail: The thumbnail being uploaded (required)
        :param bool custom: The default email to use.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_video_thumbnail_v2_with_http_info(video_id, thumbnail, **kwargs)  # noqa: E501
        else:
            (data) = self.update_video_thumbnail_v2_with_http_info(video_id, thumbnail, **kwargs)  # noqa: E501
            return data

    def update_video_thumbnail_v2_with_http_info(self, video_id, thumbnail, **kwargs):  # noqa: E501
        """Upload thumbnail  # noqa: E501

        Upload a new video thumbnail  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_video_thumbnail_v2_with_http_info(video_id, thumbnail, async=True)
        >>> result = thread.get()

        :param async bool
        :param str video_id: The id of the video (required)
        :param str thumbnail: The thumbnail being uploaded (required)
        :param bool custom: The default email to use.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'thumbnail', 'custom']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_video_thumbnail_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params or
                params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `update_video_thumbnail_v2`")  # noqa: E501
        # verify the required parameter 'thumbnail' is set
        if ('thumbnail' not in params or
                params['thumbnail'] is None):
            raise ValueError("Missing the required parameter `thumbnail` when calling `update_video_thumbnail_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'video_id' in params:
            form_params.append(('videoId', params['video_id']))  # noqa: E501
        if 'custom' in params:
            form_params.append(('custom', params['custom']))  # noqa: E501
        if 'thumbnail' in params:
            form_params.append(('thumbnail', params['thumbnail']))  # noqa: E501

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
            '/videos/thumbnail', 'PUT',
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
