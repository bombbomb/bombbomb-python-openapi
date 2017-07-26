# coding: utf-8

"""
    BombBomb

    We make it easy to build relationships using simple videos.

    OpenAPI spec version: 2.0.24005
    
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


class VideoRecorderMethodResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, user_id=None, email=None, client_id=None, vid_id=None, content=None, width=None, height=None, https=None):
        """
        VideoRecorderMethodResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_id': 'str',
            'email': 'str',
            'client_id': 'str',
            'vid_id': 'str',
            'content': 'str',
            'width': 'int',
            'height': 'int',
            'https': 'bool'
        }

        self.attribute_map = {
            'user_id': 'user_id',
            'email': 'email',
            'client_id': 'client_id',
            'vid_id': 'vid_id',
            'content': 'content',
            'width': 'width',
            'height': 'height',
            'https': 'https'
        }

        self._user_id = user_id
        self._email = email
        self._client_id = client_id
        self._vid_id = vid_id
        self._content = content
        self._width = width
        self._height = height
        self._https = https

    @property
    def user_id(self):
        """
        Gets the user_id of this VideoRecorderMethodResponse.
        The id of the user for whom this video will be recorded

        :return: The user_id of this VideoRecorderMethodResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this VideoRecorderMethodResponse.
        The id of the user for whom this video will be recorded

        :param user_id: The user_id of this VideoRecorderMethodResponse.
        :type: str
        """

        self._user_id = user_id

    @property
    def email(self):
        """
        Gets the email of this VideoRecorderMethodResponse.
        The email address of the user for whom this video will be recorded

        :return: The email of this VideoRecorderMethodResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this VideoRecorderMethodResponse.
        The email address of the user for whom this video will be recorded

        :param email: The email of this VideoRecorderMethodResponse.
        :type: str
        """

        self._email = email

    @property
    def client_id(self):
        """
        Gets the client_id of this VideoRecorderMethodResponse.
        The client_id of the user for whom this video will be recorded

        :return: The client_id of this VideoRecorderMethodResponse.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this VideoRecorderMethodResponse.
        The client_id of the user for whom this video will be recorded

        :param client_id: The client_id of this VideoRecorderMethodResponse.
        :type: str
        """

        self._client_id = client_id

    @property
    def vid_id(self):
        """
        Gets the vid_id of this VideoRecorderMethodResponse.
        The id of the video that will be recorded

        :return: The vid_id of this VideoRecorderMethodResponse.
        :rtype: str
        """
        return self._vid_id

    @vid_id.setter
    def vid_id(self, vid_id):
        """
        Sets the vid_id of this VideoRecorderMethodResponse.
        The id of the video that will be recorded

        :param vid_id: The vid_id of this VideoRecorderMethodResponse.
        :type: str
        """

        self._vid_id = vid_id

    @property
    def content(self):
        """
        Gets the content of this VideoRecorderMethodResponse.
        An HTML blob that displays a video recorder

        :return: The content of this VideoRecorderMethodResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this VideoRecorderMethodResponse.
        An HTML blob that displays a video recorder

        :param content: The content of this VideoRecorderMethodResponse.
        :type: str
        """

        self._content = content

    @property
    def width(self):
        """
        Gets the width of this VideoRecorderMethodResponse.
        The width of the video recorder

        :return: The width of this VideoRecorderMethodResponse.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this VideoRecorderMethodResponse.
        The width of the video recorder

        :param width: The width of this VideoRecorderMethodResponse.
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """
        Gets the height of this VideoRecorderMethodResponse.
        the Height of the video recorder

        :return: The height of this VideoRecorderMethodResponse.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this VideoRecorderMethodResponse.
        the Height of the video recorder

        :param height: The height of this VideoRecorderMethodResponse.
        :type: int
        """

        self._height = height

    @property
    def https(self):
        """
        Gets the https of this VideoRecorderMethodResponse.
        Whether communication from the recorder will be handled via HTTPS (always true)

        :return: The https of this VideoRecorderMethodResponse.
        :rtype: bool
        """
        return self._https

    @https.setter
    def https(self, https):
        """
        Sets the https of this VideoRecorderMethodResponse.
        Whether communication from the recorder will be handled via HTTPS (always true)

        :param https: The https of this VideoRecorderMethodResponse.
        :type: bool
        """

        self._https = https

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
