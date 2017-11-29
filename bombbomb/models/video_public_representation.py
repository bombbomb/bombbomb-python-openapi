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


class VideoPublicRepresentation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, user_id=None, status=None, name=None, description=None, thumb_url=None, video_urls=None, short_url=None, height=None, width=None, upload_date=None):
        """
        VideoPublicRepresentation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'status': 'str',
            'name': 'str',
            'description': 'str',
            'thumb_url': 'str',
            'video_urls': 'list[str]',
            'short_url': 'str',
            'height': 'int',
            'width': 'int',
            'upload_date': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'status': 'status',
            'name': 'name',
            'description': 'description',
            'thumb_url': 'thumbUrl',
            'video_urls': 'videoUrls',
            'short_url': 'shortUrl',
            'height': 'height',
            'width': 'width',
            'upload_date': 'uploadDate'
        }

        self._id = id
        self._user_id = user_id
        self._status = status
        self._name = name
        self._description = description
        self._thumb_url = thumb_url
        self._video_urls = video_urls
        self._short_url = short_url
        self._height = height
        self._width = width
        self._upload_date = upload_date

    @property
    def id(self):
        """
        Gets the id of this VideoPublicRepresentation.
        The id of the video

        :return: The id of this VideoPublicRepresentation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VideoPublicRepresentation.
        The id of the video

        :param id: The id of this VideoPublicRepresentation.
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this VideoPublicRepresentation.
        The is of the owning user

        :return: The user_id of this VideoPublicRepresentation.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this VideoPublicRepresentation.
        The is of the owning user

        :param user_id: The user_id of this VideoPublicRepresentation.
        :type: str
        """

        self._user_id = user_id

    @property
    def status(self):
        """
        Gets the status of this VideoPublicRepresentation.
        The status of the video

        :return: The status of this VideoPublicRepresentation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this VideoPublicRepresentation.
        The status of the video

        :param status: The status of this VideoPublicRepresentation.
        :type: str
        """

        self._status = status

    @property
    def name(self):
        """
        Gets the name of this VideoPublicRepresentation.
        The name of the video

        :return: The name of this VideoPublicRepresentation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VideoPublicRepresentation.
        The name of the video

        :param name: The name of this VideoPublicRepresentation.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this VideoPublicRepresentation.
        A description of the video

        :return: The description of this VideoPublicRepresentation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VideoPublicRepresentation.
        A description of the video

        :param description: The description of this VideoPublicRepresentation.
        :type: str
        """

        self._description = description

    @property
    def thumb_url(self):
        """
        Gets the thumb_url of this VideoPublicRepresentation.
        The url of the thumbnail for the video

        :return: The thumb_url of this VideoPublicRepresentation.
        :rtype: str
        """
        return self._thumb_url

    @thumb_url.setter
    def thumb_url(self, thumb_url):
        """
        Sets the thumb_url of this VideoPublicRepresentation.
        The url of the thumbnail for the video

        :param thumb_url: The thumb_url of this VideoPublicRepresentation.
        :type: str
        """

        self._thumb_url = thumb_url

    @property
    def video_urls(self):
        """
        Gets the video_urls of this VideoPublicRepresentation.
        Urls to different formats of the video

        :return: The video_urls of this VideoPublicRepresentation.
        :rtype: list[str]
        """
        return self._video_urls

    @video_urls.setter
    def video_urls(self, video_urls):
        """
        Sets the video_urls of this VideoPublicRepresentation.
        Urls to different formats of the video

        :param video_urls: The video_urls of this VideoPublicRepresentation.
        :type: list[str]
        """

        self._video_urls = video_urls

    @property
    def short_url(self):
        """
        Gets the short_url of this VideoPublicRepresentation.
        The url to use to link to the video

        :return: The short_url of this VideoPublicRepresentation.
        :rtype: str
        """
        return self._short_url

    @short_url.setter
    def short_url(self, short_url):
        """
        Sets the short_url of this VideoPublicRepresentation.
        The url to use to link to the video

        :param short_url: The short_url of this VideoPublicRepresentation.
        :type: str
        """

        self._short_url = short_url

    @property
    def height(self):
        """
        Gets the height of this VideoPublicRepresentation.
        The height of the video in pixels

        :return: The height of this VideoPublicRepresentation.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this VideoPublicRepresentation.
        The height of the video in pixels

        :param height: The height of this VideoPublicRepresentation.
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """
        Gets the width of this VideoPublicRepresentation.
        The width of the video in pixels

        :return: The width of this VideoPublicRepresentation.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this VideoPublicRepresentation.
        The width of the video in pixels

        :param width: The width of this VideoPublicRepresentation.
        :type: int
        """

        self._width = width

    @property
    def upload_date(self):
        """
        Gets the upload_date of this VideoPublicRepresentation.
        The date the video was uploaded

        :return: The upload_date of this VideoPublicRepresentation.
        :rtype: str
        """
        return self._upload_date

    @upload_date.setter
    def upload_date(self, upload_date):
        """
        Sets the upload_date of this VideoPublicRepresentation.
        The date the video was uploaded

        :param upload_date: The upload_date of this VideoPublicRepresentation.
        :type: str
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
