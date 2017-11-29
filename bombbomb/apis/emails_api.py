# coding: utf-8

"""
    BombBomb

    We make it easy to build relationships using simple videos.

    OpenAPI spec version: 2.0.25797
    
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


class EmailsApi(object):
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

    def create_printing_press_email(self, template_id, content, **kwargs):
        """
        Create an Email with Printing Press
        Prints an email using the template id and content to the users account.If a video id is included, it will replace any video placeholders with that video.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_printing_press_email(template_id, content, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str template_id: The template id to be printed. (required)
        :param str content: The content of the email. (required)
        :param str email_id: The email id to be printed to.
        :param str video_id: A video to replace video place holders with.
        :param str subject_line: The subject line to be printed.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_printing_press_email_with_http_info(template_id, content, **kwargs)
        else:
            (data) = self.create_printing_press_email_with_http_info(template_id, content, **kwargs)
            return data

    def create_printing_press_email_with_http_info(self, template_id, content, **kwargs):
        """
        Create an Email with Printing Press
        Prints an email using the template id and content to the users account.If a video id is included, it will replace any video placeholders with that video.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_printing_press_email_with_http_info(template_id, content, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str template_id: The template id to be printed. (required)
        :param str content: The content of the email. (required)
        :param str email_id: The email id to be printed to.
        :param str video_id: A video to replace video place holders with.
        :param str subject_line: The subject line to be printed.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id', 'content', 'email_id', 'video_id', 'subject_line']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_printing_press_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params) or (params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `create_printing_press_email`")
        # verify the required parameter 'content' is set
        if ('content' not in params) or (params['content'] is None):
            raise ValueError("Missing the required parameter `content` when calling `create_printing_press_email`")

        resource_path = '/emails/print'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'template_id' in params:
            form_params.append(('templateId', params['template_id']))
        if 'content' in params:
            form_params.append(('content', params['content']))
        if 'email_id' in params:
            form_params.append(('emailId', params['email_id']))
        if 'video_id' in params:
            form_params.append(('videoId', params['video_id']))
        if 'subject_line' in params:
            form_params.append(('subjectLine', params['subject_line']))

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

    def get_all_templates_for_current_user(self, **kwargs):
        """
        Get all user templates
        Get all templates accessible to the current user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_templates_for_current_user(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool quick_send_only: Whether to return only quick send templates.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_templates_for_current_user_with_http_info(**kwargs)
        else:
            (data) = self.get_all_templates_for_current_user_with_http_info(**kwargs)
            return data

    def get_all_templates_for_current_user_with_http_info(self, **kwargs):
        """
        Get all user templates
        Get all templates accessible to the current user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_templates_for_current_user_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool quick_send_only: Whether to return only quick send templates.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quick_send_only']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_templates_for_current_user" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/emails/templates'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'quick_send_only' in params:
            query_params['quickSendOnly'] = params['quick_send_only']

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

    def get_email_tracking(self, email_id, **kwargs):
        """
        Get Email Tracking
        Get Tracking data for all sends of an Email

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_email_tracking(email_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_id: ID of the email (required)
        :param str job_id: ID of the Job (or null for all jobs)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_email_tracking_with_http_info(email_id, **kwargs)
        else:
            (data) = self.get_email_tracking_with_http_info(email_id, **kwargs)
            return data

    def get_email_tracking_with_http_info(self, email_id, **kwargs):
        """
        Get Email Tracking
        Get Tracking data for all sends of an Email

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_email_tracking_with_http_info(email_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_id: ID of the email (required)
        :param str job_id: ID of the Job (or null for all jobs)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email_id', 'job_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_email_tracking" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email_id' is set
        if ('email_id' not in params) or (params['email_id'] is None):
            raise ValueError("Missing the required parameter `email_id` when calling `get_email_tracking`")

        resource_path = '/emails/{emailId}/tracking'.replace('{format}', 'json')
        path_params = {}
        if 'email_id' in params:
            path_params['emailId'] = params['email_id']

        query_params = {}
        if 'job_id' in params:
            query_params['jobId'] = params['job_id']

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

    def get_email_tracking_interactions(self, email_id, **kwargs):
        """
        Get Email Tracking Interactions
        Get Contact detail interactions for an Email

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_email_tracking_interactions(email_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_id: ID of the email (required)
        :param str job_id: ID of the Job (or null for all jobs)
        :param str interaction_type: Interaction type to order and filter by
        :param str search_term: Search term to filer by
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_email_tracking_interactions_with_http_info(email_id, **kwargs)
        else:
            (data) = self.get_email_tracking_interactions_with_http_info(email_id, **kwargs)
            return data

    def get_email_tracking_interactions_with_http_info(self, email_id, **kwargs):
        """
        Get Email Tracking Interactions
        Get Contact detail interactions for an Email

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_email_tracking_interactions_with_http_info(email_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_id: ID of the email (required)
        :param str job_id: ID of the Job (or null for all jobs)
        :param str interaction_type: Interaction type to order and filter by
        :param str search_term: Search term to filer by
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email_id', 'job_id', 'interaction_type', 'search_term']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_email_tracking_interactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email_id' is set
        if ('email_id' not in params) or (params['email_id'] is None):
            raise ValueError("Missing the required parameter `email_id` when calling `get_email_tracking_interactions`")

        resource_path = '/emails/{emailId}/tracking/interactions'.replace('{format}', 'json')
        path_params = {}
        if 'email_id' in params:
            path_params['emailId'] = params['email_id']

        query_params = {}
        if 'job_id' in params:
            query_params['jobId'] = params['job_id']
        if 'interaction_type' in params:
            query_params['interactionType'] = params['interaction_type']
        if 'search_term' in params:
            query_params['searchTerm'] = params['search_term']

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

    def get_hourly_email_tracking(self, email_id, **kwargs):
        """
        Get Hourly Email Tracking
        Get Tracking data for an Email,             broken down by the hour and filterable by an Interaction type

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_hourly_email_tracking(email_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_id: ID of the email (required)
        :param str job_id: ID of the Job (or null for all jobs)
        :param str interaction_type: Interaction type to filter by
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_hourly_email_tracking_with_http_info(email_id, **kwargs)
        else:
            (data) = self.get_hourly_email_tracking_with_http_info(email_id, **kwargs)
            return data

    def get_hourly_email_tracking_with_http_info(self, email_id, **kwargs):
        """
        Get Hourly Email Tracking
        Get Tracking data for an Email,             broken down by the hour and filterable by an Interaction type

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_hourly_email_tracking_with_http_info(email_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email_id: ID of the email (required)
        :param str job_id: ID of the Job (or null for all jobs)
        :param str interaction_type: Interaction type to filter by
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email_id', 'job_id', 'interaction_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hourly_email_tracking" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email_id' is set
        if ('email_id' not in params) or (params['email_id'] is None):
            raise ValueError("Missing the required parameter `email_id` when calling `get_hourly_email_tracking`")

        resource_path = '/emails/{emailId}/tracking/hourly'.replace('{format}', 'json')
        path_params = {}
        if 'email_id' in params:
            path_params['emailId'] = params['email_id']

        query_params = {}
        if 'job_id' in params:
            query_params['jobId'] = params['job_id']
        if 'interaction_type' in params:
            query_params['interactionType'] = params['interaction_type']

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

    def get_quick_send_templates(self, **kwargs):
        """
        Get all quicksend templates
        Get all quicksend templates accessible to the user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_quick_send_templates(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_quick_send_templates_with_http_info(**kwargs)
        else:
            (data) = self.get_quick_send_templates_with_http_info(**kwargs)
            return data

    def get_quick_send_templates_with_http_info(self, **kwargs):
        """
        Get all quicksend templates
        Get all quicksend templates accessible to the user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_quick_send_templates_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_quick_send_templates" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/emails/quicksend/templates'.replace('{format}', 'json')
        path_params = {}

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

    def video_quick_sender(self, **kwargs):
        """
        Send a quicksend email
        Send a quicksend video email to the list or users provided.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.video_quick_sender(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str video_id: A guid id for the video.
        :param str email_addresses: A semi-colon separated list of email addresses to send to.
        :param str subject: Subject line for the email.
        :param str message: Message for the body of the email.
        :param str list_ids: An array of list ids
        :param int scheduled_send_timestamp: When to schedule the send (seconds since epoch). null value means send immediately.
        :param str extended_properties: Bool value that when checked will send back both emailId as well as extra properties
        :param str template_id: Id of a template to use for this send. A null value means use the default for this user.
        :param str strip_html: remove HTML elements
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.video_quick_sender_with_http_info(**kwargs)
        else:
            (data) = self.video_quick_sender_with_http_info(**kwargs)
            return data

    def video_quick_sender_with_http_info(self, **kwargs):
        """
        Send a quicksend email
        Send a quicksend video email to the list or users provided.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.video_quick_sender_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str video_id: A guid id for the video.
        :param str email_addresses: A semi-colon separated list of email addresses to send to.
        :param str subject: Subject line for the email.
        :param str message: Message for the body of the email.
        :param str list_ids: An array of list ids
        :param int scheduled_send_timestamp: When to schedule the send (seconds since epoch). null value means send immediately.
        :param str extended_properties: Bool value that when checked will send back both emailId as well as extra properties
        :param str template_id: Id of a template to use for this send. A null value means use the default for this user.
        :param str strip_html: remove HTML elements
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'email_addresses', 'subject', 'message', 'list_ids', 'scheduled_send_timestamp', 'extended_properties', 'template_id', 'strip_html']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method video_quick_sender" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/emails/quicksend'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'video_id' in params:
            form_params.append(('videoId', params['video_id']))
        if 'email_addresses' in params:
            form_params.append(('emailAddresses', params['email_addresses']))
        if 'subject' in params:
            form_params.append(('subject', params['subject']))
        if 'message' in params:
            form_params.append(('message', params['message']))
        if 'list_ids' in params:
            form_params.append(('listIds', params['list_ids']))
        if 'scheduled_send_timestamp' in params:
            form_params.append(('scheduledSendTimestamp', params['scheduled_send_timestamp']))
        if 'extended_properties' in params:
            form_params.append(('extendedProperties', params['extended_properties']))
        if 'template_id' in params:
            form_params.append(('templateId', params['template_id']))
        if 'strip_html' in params:
            form_params.append(('stripHTML', params['strip_html']))

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
