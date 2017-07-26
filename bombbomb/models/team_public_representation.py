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


class TeamPublicRepresentation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, created_date=None):
        """
        TeamPublicRepresentation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'created_date': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'created_date': 'createdDate'
        }

        self._id = id
        self._name = name
        self._created_date = created_date

    @property
    def id(self):
        """
        Gets the id of this TeamPublicRepresentation.
        The id of the team

        :return: The id of this TeamPublicRepresentation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TeamPublicRepresentation.
        The id of the team

        :param id: The id of this TeamPublicRepresentation.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this TeamPublicRepresentation.
        The name of the team

        :return: The name of this TeamPublicRepresentation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TeamPublicRepresentation.
        The name of the team

        :param name: The name of this TeamPublicRepresentation.
        :type: str
        """

        self._name = name

    @property
    def created_date(self):
        """
        Gets the created_date of this TeamPublicRepresentation.
        The date the team was created

        :return: The created_date of this TeamPublicRepresentation.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this TeamPublicRepresentation.
        The date the team was created

        :param created_date: The created_date of this TeamPublicRepresentation.
        :type: str
        """

        self._created_date = created_date

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
