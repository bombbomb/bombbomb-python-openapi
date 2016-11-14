# coding: utf-8

"""
    BombBomb

    We make it easy to build relationships using simple videos.

    OpenAPI spec version: 2.0.21432
    
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

from pprint import pformat
from six import iteritems
import re


class JerichoConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, send_date=None, is_prompt=None, email_id=None, prompt_subject=None, prompt_body=None, email_subject=None, email_body=None, send_without_video=None):
        """
        JerichoConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'client_group_id': 'str',
            'send_date': 'datetime',
            'is_prompt': 'bool',
            'email_id': 'str',
            'prompt_subject': 'str',
            'prompt_body': 'str',
            'email_subject': 'str',
            'email_body': 'str',
            'send_without_video': 'bool',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'client_group_id': 'clientGroupId',
            'send_date': 'sendDate',
            'is_prompt': 'isPrompt',
            'email_id': 'emailId',
            'prompt_subject': 'promptSubject',
            'prompt_body': 'promptBody',
            'email_subject': 'emailSubject',
            'email_body': 'emailBody',
            'send_without_video': 'sendWithoutVideo',
            'status': 'status'
        }

        self._id = None
        self._client_group_id = None
        self._status = None
        self._send_date = send_date
        self._is_prompt = is_prompt
        self._email_id = email_id
        self._prompt_subject = prompt_subject
        self._prompt_body = prompt_body
        self._email_subject = email_subject
        self._email_body = email_body
        self._send_without_video = send_without_video

    @property
    def id(self):
        """
        Gets the id of this JerichoConfiguration.


        :return: The id of this JerichoConfiguration.
        :rtype: str
        """
        return self._id

    @property
    def client_group_id(self):
        """
        Gets the client_group_id of this JerichoConfiguration.


        :return: The client_group_id of this JerichoConfiguration.
        :rtype: str
        """
        return self._client_group_id

    @property
    def send_date(self):
        """
        Gets the send_date of this JerichoConfiguration.
        When the email should be sent.

        :return: The send_date of this JerichoConfiguration.
        :rtype: datetime
        """
        return self._send_date

    @send_date.setter
    def send_date(self, send_date):
        """
        Sets the send_date of this JerichoConfiguration.
        When the email should be sent.

        :param send_date: The send_date of this JerichoConfiguration.
        :type: datetime
        """

        self._send_date = send_date

    @property
    def is_prompt(self):
        """
        Gets the is_prompt of this JerichoConfiguration.
        Determines whether this is a static or prompted send.

        :return: The is_prompt of this JerichoConfiguration.
        :rtype: bool
        """
        return self._is_prompt

    @is_prompt.setter
    def is_prompt(self, is_prompt):
        """
        Sets the is_prompt of this JerichoConfiguration.
        Determines whether this is a static or prompted send.

        :param is_prompt: The is_prompt of this JerichoConfiguration.
        :type: bool
        """

        self._is_prompt = is_prompt

    @property
    def email_id(self):
        """
        Gets the email_id of this JerichoConfiguration.
        Static send: The Email to send on behalf of the group members.

        :return: The email_id of this JerichoConfiguration.
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """
        Sets the email_id of this JerichoConfiguration.
        Static send: The Email to send on behalf of the group members.

        :param email_id: The email_id of this JerichoConfiguration.
        :type: str
        """

        self._email_id = email_id

    @property
    def prompt_subject(self):
        """
        Gets the prompt_subject of this JerichoConfiguration.
        Video Prompt: The subject line prompting the user to record a video.

        :return: The prompt_subject of this JerichoConfiguration.
        :rtype: str
        """
        return self._prompt_subject

    @prompt_subject.setter
    def prompt_subject(self, prompt_subject):
        """
        Sets the prompt_subject of this JerichoConfiguration.
        Video Prompt: The subject line prompting the user to record a video.

        :param prompt_subject: The prompt_subject of this JerichoConfiguration.
        :type: str
        """

        self._prompt_subject = prompt_subject

    @property
    def prompt_body(self):
        """
        Gets the prompt_body of this JerichoConfiguration.
        Video Prompt: The HTML body of the email prompting the user to record a video.

        :return: The prompt_body of this JerichoConfiguration.
        :rtype: str
        """
        return self._prompt_body

    @prompt_body.setter
    def prompt_body(self, prompt_body):
        """
        Sets the prompt_body of this JerichoConfiguration.
        Video Prompt: The HTML body of the email prompting the user to record a video.

        :param prompt_body: The prompt_body of this JerichoConfiguration.
        :type: str
        """

        self._prompt_body = prompt_body

    @property
    def email_subject(self):
        """
        Gets the email_subject of this JerichoConfiguration.
        Video Prompt: The subject line of the final sent email

        :return: The email_subject of this JerichoConfiguration.
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """
        Sets the email_subject of this JerichoConfiguration.
        Video Prompt: The subject line of the final sent email

        :param email_subject: The email_subject of this JerichoConfiguration.
        :type: str
        """

        self._email_subject = email_subject

    @property
    def email_body(self):
        """
        Gets the email_body of this JerichoConfiguration.
        Video Prompt: The HTML body of the final sent email.

        :return: The email_body of this JerichoConfiguration.
        :rtype: str
        """
        return self._email_body

    @email_body.setter
    def email_body(self, email_body):
        """
        Sets the email_body of this JerichoConfiguration.
        Video Prompt: The HTML body of the final sent email.

        :param email_body: The email_body of this JerichoConfiguration.
        :type: str
        """

        self._email_body = email_body

    @property
    def send_without_video(self):
        """
        Gets the send_without_video of this JerichoConfiguration.
        Video Prompt: Whether to send the final email if no video was recorded.

        :return: The send_without_video of this JerichoConfiguration.
        :rtype: bool
        """
        return self._send_without_video

    @send_without_video.setter
    def send_without_video(self, send_without_video):
        """
        Sets the send_without_video of this JerichoConfiguration.
        Video Prompt: Whether to send the final email if no video was recorded.

        :param send_without_video: The send_without_video of this JerichoConfiguration.
        :type: bool
        """

        self._send_without_video = send_without_video

    @property
    def status(self):
        """
        Gets the status of this JerichoConfiguration.
        The state of the send.

        :return: The status of this JerichoConfiguration.
        :rtype: str
        """
        return self._status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
