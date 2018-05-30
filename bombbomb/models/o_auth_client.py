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

from pprint import pformat
from six import iteritems
import re


class OAuthClient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, client_secret=None, grants_allowed=None, owning_user_id=None, redirect_uri=None):
        """
        OAuthClient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'identifier': 'str',
            'name': 'str',
            'client_secret': 'str',
            'grants_allowed': 'str',
            'owning_user_id': 'str',
            'redirect_uri': 'str'
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'name': 'name',
            'client_secret': 'clientSecret',
            'grants_allowed': 'grantsAllowed',
            'owning_user_id': 'owningUserId',
            'redirect_uri': 'redirectUri'
        }

        self._identifier = None
        self._name = name
        self._client_secret = client_secret
        self._grants_allowed = grants_allowed
        self._owning_user_id = owning_user_id
        self._redirect_uri = redirect_uri

    @property
    def identifier(self):
        """
        Gets the identifier of this OAuthClient.
        The id of the OAuth Client

        :return: The identifier of this OAuthClient.
        :rtype: str
        """
        return self._identifier

    @property
    def name(self):
        """
        Gets the name of this OAuthClient.
        The user-facing name of the client. Eg. MyCrm

        :return: The name of this OAuthClient.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OAuthClient.
        The user-facing name of the client. Eg. MyCrm

        :param name: The name of this OAuthClient.
        :type: str
        """

        self._name = name

    @property
    def client_secret(self):
        """
        Gets the client_secret of this OAuthClient.
        The secret supplied to the OAuth Application

        :return: The client_secret of this OAuthClient.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """
        Sets the client_secret of this OAuthClient.
        The secret supplied to the OAuth Application

        :param client_secret: The client_secret of this OAuthClient.
        :type: str
        """

        self._client_secret = client_secret

    @property
    def grants_allowed(self):
        """
        Gets the grants_allowed of this OAuthClient.
        The grants allowed

        :return: The grants_allowed of this OAuthClient.
        :rtype: str
        """
        return self._grants_allowed

    @grants_allowed.setter
    def grants_allowed(self, grants_allowed):
        """
        Sets the grants_allowed of this OAuthClient.
        The grants allowed

        :param grants_allowed: The grants_allowed of this OAuthClient.
        :type: str
        """

        self._grants_allowed = grants_allowed

    @property
    def owning_user_id(self):
        """
        Gets the owning_user_id of this OAuthClient.
        The user who controls the OAuth App

        :return: The owning_user_id of this OAuthClient.
        :rtype: str
        """
        return self._owning_user_id

    @owning_user_id.setter
    def owning_user_id(self, owning_user_id):
        """
        Sets the owning_user_id of this OAuthClient.
        The user who controls the OAuth App

        :param owning_user_id: The owning_user_id of this OAuthClient.
        :type: str
        """

        self._owning_user_id = owning_user_id

    @property
    def redirect_uri(self):
        """
        Gets the redirect_uri of this OAuthClient.
        Where OAuth authorization sessions are returned to

        :return: The redirect_uri of this OAuthClient.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """
        Sets the redirect_uri of this OAuthClient.
        Where OAuth authorization sessions are returned to

        :param redirect_uri: The redirect_uri of this OAuthClient.
        :type: str
        """

        self._redirect_uri = redirect_uri

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
