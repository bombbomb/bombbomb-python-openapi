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


class CurriculumUserProgress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, user_id=None, curriculum_item_id=None, curriculum_id=None, completed_date=None):
        """
        CurriculumUserProgress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'curriculum_item_id': 'str',
            'curriculum_id': 'str',
            'completed_date': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'curriculum_item_id': 'curriculumItemId',
            'curriculum_id': 'curriculumId',
            'completed_date': 'completedDate'
        }

        self._id = id
        self._user_id = user_id
        self._curriculum_item_id = curriculum_item_id
        self._curriculum_id = curriculum_id
        self._completed_date = completed_date

    @property
    def id(self):
        """
        Gets the id of this CurriculumUserProgress.
        Id

        :return: The id of this CurriculumUserProgress.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CurriculumUserProgress.
        Id

        :param id: The id of this CurriculumUserProgress.
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this CurriculumUserProgress.
        User Id

        :return: The user_id of this CurriculumUserProgress.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this CurriculumUserProgress.
        User Id

        :param user_id: The user_id of this CurriculumUserProgress.
        :type: str
        """

        self._user_id = user_id

    @property
    def curriculum_item_id(self):
        """
        Gets the curriculum_item_id of this CurriculumUserProgress.
        Curriculum Item Id

        :return: The curriculum_item_id of this CurriculumUserProgress.
        :rtype: str
        """
        return self._curriculum_item_id

    @curriculum_item_id.setter
    def curriculum_item_id(self, curriculum_item_id):
        """
        Sets the curriculum_item_id of this CurriculumUserProgress.
        Curriculum Item Id

        :param curriculum_item_id: The curriculum_item_id of this CurriculumUserProgress.
        :type: str
        """

        self._curriculum_item_id = curriculum_item_id

    @property
    def curriculum_id(self):
        """
        Gets the curriculum_id of this CurriculumUserProgress.
        Curriculum Id

        :return: The curriculum_id of this CurriculumUserProgress.
        :rtype: str
        """
        return self._curriculum_id

    @curriculum_id.setter
    def curriculum_id(self, curriculum_id):
        """
        Sets the curriculum_id of this CurriculumUserProgress.
        Curriculum Id

        :param curriculum_id: The curriculum_id of this CurriculumUserProgress.
        :type: str
        """

        self._curriculum_id = curriculum_id

    @property
    def completed_date(self):
        """
        Gets the completed_date of this CurriculumUserProgress.
        When the final email is scheduled to be sent

        :return: The completed_date of this CurriculumUserProgress.
        :rtype: datetime
        """
        return self._completed_date

    @completed_date.setter
    def completed_date(self, completed_date):
        """
        Sets the completed_date of this CurriculumUserProgress.
        When the final email is scheduled to be sent

        :param completed_date: The completed_date of this CurriculumUserProgress.
        :type: datetime
        """

        self._completed_date = completed_date

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