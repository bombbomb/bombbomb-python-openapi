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


class CurriculumWithProgress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, progress=None, id=None, name=None, html_intro=None, img_url=None, item_count=None, render_as=None, visible_to_all_users=None):
        """
        CurriculumWithProgress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'progress': 'list[CurriculumUserProgress]',
            'id': 'str',
            'name': 'str',
            'html_intro': 'str',
            'img_url': 'str',
            'item_count': 'int',
            'render_as': 'str',
            'visible_to_all_users': 'bool'
        }

        self.attribute_map = {
            'progress': 'progress',
            'id': 'id',
            'name': 'name',
            'html_intro': 'htmlIntro',
            'img_url': 'imgUrl',
            'item_count': 'itemCount',
            'render_as': 'renderAs',
            'visible_to_all_users': 'visibleToAllUsers'
        }

        self._progress = progress
        self._id = id
        self._name = name
        self._html_intro = html_intro
        self._img_url = img_url
        self._item_count = item_count
        self._render_as = render_as
        self._visible_to_all_users = visible_to_all_users

    @property
    def progress(self):
        """
        Gets the progress of this CurriculumWithProgress.
        Collection of User Progress for Curriculum

        :return: The progress of this CurriculumWithProgress.
        :rtype: list[CurriculumUserProgress]
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this CurriculumWithProgress.
        Collection of User Progress for Curriculum

        :param progress: The progress of this CurriculumWithProgress.
        :type: list[CurriculumUserProgress]
        """

        self._progress = progress

    @property
    def id(self):
        """
        Gets the id of this CurriculumWithProgress.
        Id

        :return: The id of this CurriculumWithProgress.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CurriculumWithProgress.
        Id

        :param id: The id of this CurriculumWithProgress.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CurriculumWithProgress.
        Name

        :return: The name of this CurriculumWithProgress.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CurriculumWithProgress.
        Name

        :param name: The name of this CurriculumWithProgress.
        :type: str
        """

        self._name = name

    @property
    def html_intro(self):
        """
        Gets the html_intro of this CurriculumWithProgress.
        HTML formatted intro

        :return: The html_intro of this CurriculumWithProgress.
        :rtype: str
        """
        return self._html_intro

    @html_intro.setter
    def html_intro(self, html_intro):
        """
        Sets the html_intro of this CurriculumWithProgress.
        HTML formatted intro

        :param html_intro: The html_intro of this CurriculumWithProgress.
        :type: str
        """

        self._html_intro = html_intro

    @property
    def img_url(self):
        """
        Gets the img_url of this CurriculumWithProgress.
        URI of header image

        :return: The img_url of this CurriculumWithProgress.
        :rtype: str
        """
        return self._img_url

    @img_url.setter
    def img_url(self, img_url):
        """
        Sets the img_url of this CurriculumWithProgress.
        URI of header image

        :param img_url: The img_url of this CurriculumWithProgress.
        :type: str
        """

        self._img_url = img_url

    @property
    def item_count(self):
        """
        Gets the item_count of this CurriculumWithProgress.
        Number of curriculum items

        :return: The item_count of this CurriculumWithProgress.
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """
        Sets the item_count of this CurriculumWithProgress.
        Number of curriculum items

        :param item_count: The item_count of this CurriculumWithProgress.
        :type: int
        """

        self._item_count = item_count

    @property
    def render_as(self):
        """
        Gets the render_as of this CurriculumWithProgress.
        Render method for curriculum

        :return: The render_as of this CurriculumWithProgress.
        :rtype: str
        """
        return self._render_as

    @render_as.setter
    def render_as(self, render_as):
        """
        Sets the render_as of this CurriculumWithProgress.
        Render method for curriculum

        :param render_as: The render_as of this CurriculumWithProgress.
        :type: str
        """

        self._render_as = render_as

    @property
    def visible_to_all_users(self):
        """
        Gets the visible_to_all_users of this CurriculumWithProgress.
        Globally visible

        :return: The visible_to_all_users of this CurriculumWithProgress.
        :rtype: bool
        """
        return self._visible_to_all_users

    @visible_to_all_users.setter
    def visible_to_all_users(self, visible_to_all_users):
        """
        Sets the visible_to_all_users of this CurriculumWithProgress.
        Globally visible

        :param visible_to_all_users: The visible_to_all_users of this CurriculumWithProgress.
        :type: bool
        """

        self._visible_to_all_users = visible_to_all_users

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
