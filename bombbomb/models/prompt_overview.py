# coding: utf-8

"""
    BombBomb

    We make it easy to build relationships using simple videos.  # noqa: E501

    OpenAPI spec version: 2.0.831
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PromptOverview(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start_date': 'str',
        'end_date': 'str',
        'user_batch_lists_id_helper': 'str',
        'prompt_id_helper': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'user_batch_lists_id_helper': 'userBatchListsIdHelper',
        'prompt_id_helper': 'promptIdHelper'
    }

    def __init__(self, start_date=None, end_date=None, user_batch_lists_id_helper=None, prompt_id_helper=None):  # noqa: E501
        """PromptOverview - a model defined in Swagger"""  # noqa: E501

        self._start_date = None
        self._end_date = None
        self._user_batch_lists_id_helper = None
        self._prompt_id_helper = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if user_batch_lists_id_helper is not None:
            self.user_batch_lists_id_helper = user_batch_lists_id_helper
        if prompt_id_helper is not None:
            self.prompt_id_helper = prompt_id_helper

    @property
    def start_date(self):
        """Gets the start_date of this PromptOverview.  # noqa: E501

        The startDate property  # noqa: E501

        :return: The start_date of this PromptOverview.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PromptOverview.

        The startDate property  # noqa: E501

        :param start_date: The start_date of this PromptOverview.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this PromptOverview.  # noqa: E501

        The endDate property  # noqa: E501

        :return: The end_date of this PromptOverview.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this PromptOverview.

        The endDate property  # noqa: E501

        :param end_date: The end_date of this PromptOverview.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def user_batch_lists_id_helper(self):
        """Gets the user_batch_lists_id_helper of this PromptOverview.  # noqa: E501

        The userBatchListsIdHelper property  # noqa: E501

        :return: The user_batch_lists_id_helper of this PromptOverview.  # noqa: E501
        :rtype: str
        """
        return self._user_batch_lists_id_helper

    @user_batch_lists_id_helper.setter
    def user_batch_lists_id_helper(self, user_batch_lists_id_helper):
        """Sets the user_batch_lists_id_helper of this PromptOverview.

        The userBatchListsIdHelper property  # noqa: E501

        :param user_batch_lists_id_helper: The user_batch_lists_id_helper of this PromptOverview.  # noqa: E501
        :type: str
        """

        self._user_batch_lists_id_helper = user_batch_lists_id_helper

    @property
    def prompt_id_helper(self):
        """Gets the prompt_id_helper of this PromptOverview.  # noqa: E501

        The promptIdHelper property  # noqa: E501

        :return: The prompt_id_helper of this PromptOverview.  # noqa: E501
        :rtype: str
        """
        return self._prompt_id_helper

    @prompt_id_helper.setter
    def prompt_id_helper(self, prompt_id_helper):
        """Sets the prompt_id_helper of this PromptOverview.

        The promptIdHelper property  # noqa: E501

        :param prompt_id_helper: The prompt_id_helper of this PromptOverview.  # noqa: E501
        :type: str
        """

        self._prompt_id_helper = prompt_id_helper

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PromptOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
