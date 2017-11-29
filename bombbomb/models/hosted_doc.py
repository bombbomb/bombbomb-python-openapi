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

from pprint import pformat
from six import iteritems
import re


class HostedDoc(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, user_id=None, file_name=None, short_url=None, long_url=None, upload_date=None):
        """
        HostedDoc - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'file_name': 'str',
            'short_url': 'str',
            'long_url': 'str',
            'upload_date': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'file_name': 'fileName',
            'short_url': 'shortUrl',
            'long_url': 'longUrl',
            'upload_date': 'uploadDate'
        }

        self._id = id
        self._user_id = user_id
        self._file_name = file_name
        self._short_url = short_url
        self._long_url = long_url
        self._upload_date = upload_date

    @property
    def id(self):
        """
        Gets the id of this HostedDoc.
        The doc's id.

        :return: The id of this HostedDoc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HostedDoc.
        The doc's id.

        :param id: The id of this HostedDoc.
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this HostedDoc.
        The doc's owner.

        :return: The user_id of this HostedDoc.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this HostedDoc.
        The doc's owner.

        :param user_id: The user_id of this HostedDoc.
        :type: str
        """

        self._user_id = user_id

    @property
    def file_name(self):
        """
        Gets the file_name of this HostedDoc.
        docs file name.

        :return: The file_name of this HostedDoc.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this HostedDoc.
        docs file name.

        :param file_name: The file_name of this HostedDoc.
        :type: str
        """

        self._file_name = file_name

    @property
    def short_url(self):
        """
        Gets the short_url of this HostedDoc.
        The doc's short url.

        :return: The short_url of this HostedDoc.
        :rtype: str
        """
        return self._short_url

    @short_url.setter
    def short_url(self, short_url):
        """
        Sets the short_url of this HostedDoc.
        The doc's short url.

        :param short_url: The short_url of this HostedDoc.
        :type: str
        """

        self._short_url = short_url

    @property
    def long_url(self):
        """
        Gets the long_url of this HostedDoc.
        The doc's long url.

        :return: The long_url of this HostedDoc.
        :rtype: str
        """
        return self._long_url

    @long_url.setter
    def long_url(self, long_url):
        """
        Sets the long_url of this HostedDoc.
        The doc's long url.

        :param long_url: The long_url of this HostedDoc.
        :type: str
        """

        self._long_url = long_url

    @property
    def upload_date(self):
        """
        Gets the upload_date of this HostedDoc.
        The doc's upload date.

        :return: The upload_date of this HostedDoc.
        :rtype: datetime
        """
        return self._upload_date

    @upload_date.setter
    def upload_date(self, upload_date):
        """
        Sets the upload_date of this HostedDoc.
        The doc's upload date.

        :param upload_date: The upload_date of this HostedDoc.
        :type: datetime
        """

        self._upload_date = upload_date

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
