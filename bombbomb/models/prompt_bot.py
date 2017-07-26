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


class PromptBot(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, email_id=None, list_id=None, name=None, contact_field_value_column=None, start_date=None, end_date=None, bot_type_id=None, template_id=None, video_id=None, content=None, subject=None, generated_by=None):
        """
        PromptBot - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'email_id': 'str',
            'list_id': 'str',
            'name': 'str',
            'contact_field_value_column': 'str',
            'status': 'int',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'bot_type_id': 'str',
            'template_id': 'str',
            'video_id': 'str',
            'content': 'str',
            'subject': 'str',
            'generated_by': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'email_id': 'emailId',
            'list_id': 'listId',
            'name': 'name',
            'contact_field_value_column': 'contactFieldValueColumn',
            'status': 'status',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'bot_type_id': 'botTypeId',
            'template_id': 'templateId',
            'video_id': 'videoId',
            'content': 'content',
            'subject': 'subject',
            'generated_by': 'generatedBy'
        }

        self._id = None
        self._user_id = None
        self._status = None
        self._email_id = email_id
        self._list_id = list_id
        self._name = name
        self._contact_field_value_column = contact_field_value_column
        self._start_date = start_date
        self._end_date = end_date
        self._bot_type_id = bot_type_id
        self._template_id = template_id
        self._video_id = video_id
        self._content = content
        self._subject = subject
        self._generated_by = generated_by

    @property
    def id(self):
        """
        Gets the id of this PromptBot.
        The identifier of the prompt bot. Read Only.

        :return: The id of this PromptBot.
        :rtype: str
        """
        return self._id

    @property
    def user_id(self):
        """
        Gets the user_id of this PromptBot.
        The prompt bot's owner. Read Only.

        :return: The user_id of this PromptBot.
        :rtype: str
        """
        return self._user_id

    @property
    def email_id(self):
        """
        Gets the email_id of this PromptBot.
        The default email being sent to contacts in the prompt bot list.

        :return: The email_id of this PromptBot.
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """
        Sets the email_id of this PromptBot.
        The default email being sent to contacts in the prompt bot list.

        :param email_id: The email_id of this PromptBot.
        :type: str
        """

        self._email_id = email_id

    @property
    def list_id(self):
        """
        Gets the list_id of this PromptBot.
        The list to attach the Prompt Bot to.

        :return: The list_id of this PromptBot.
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """
        Sets the list_id of this PromptBot.
        The list to attach the Prompt Bot to.

        :param list_id: The list_id of this PromptBot.
        :type: str
        """

        self._list_id = list_id

    @property
    def name(self):
        """
        Gets the name of this PromptBot.
        The name of the bot.

        :return: The name of this PromptBot.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PromptBot.
        The name of the bot.

        :param name: The name of this PromptBot.
        :type: str
        """

        self._name = name

    @property
    def contact_field_value_column(self):
        """
        Gets the contact_field_value_column of this PromptBot.
        The custom contact field value column used for this bot.

        :return: The contact_field_value_column of this PromptBot.
        :rtype: str
        """
        return self._contact_field_value_column

    @contact_field_value_column.setter
    def contact_field_value_column(self, contact_field_value_column):
        """
        Sets the contact_field_value_column of this PromptBot.
        The custom contact field value column used for this bot.

        :param contact_field_value_column: The contact_field_value_column of this PromptBot.
        :type: str
        """

        self._contact_field_value_column = contact_field_value_column

    @property
    def status(self):
        """
        Gets the status of this PromptBot.
        The status of the prompt bot. Read Only.

        :return: The status of this PromptBot.
        :rtype: int
        """
        return self._status

    @property
    def start_date(self):
        """
        Gets the start_date of this PromptBot.
        when the bot started

        :return: The start_date of this PromptBot.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this PromptBot.
        when the bot started

        :param start_date: The start_date of this PromptBot.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this PromptBot.
        when the bot should finish

        :return: The end_date of this PromptBot.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this PromptBot.
        when the bot should finish

        :param end_date: The end_date of this PromptBot.
        :type: datetime
        """

        self._end_date = end_date

    @property
    def bot_type_id(self):
        """
        Gets the bot_type_id of this PromptBot.
        The type of bot.

        :return: The bot_type_id of this PromptBot.
        :rtype: str
        """
        return self._bot_type_id

    @bot_type_id.setter
    def bot_type_id(self, bot_type_id):
        """
        Sets the bot_type_id of this PromptBot.
        The type of bot.

        :param bot_type_id: The bot_type_id of this PromptBot.
        :type: str
        """

        self._bot_type_id = bot_type_id

    @property
    def template_id(self):
        """
        Gets the template_id of this PromptBot.
        The template id used to generate the default email.

        :return: The template_id of this PromptBot.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this PromptBot.
        The template id used to generate the default email.

        :param template_id: The template_id of this PromptBot.
        :type: str
        """

        self._template_id = template_id

    @property
    def video_id(self):
        """
        Gets the video_id of this PromptBot.
        The video that was added to the prompt.

        :return: The video_id of this PromptBot.
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """
        Sets the video_id of this PromptBot.
        The video that was added to the prompt.

        :param video_id: The video_id of this PromptBot.
        :type: str
        """

        self._video_id = video_id

    @property
    def content(self):
        """
        Gets the content of this PromptBot.
        The content to use in the email.

        :return: The content of this PromptBot.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this PromptBot.
        The content to use in the email.

        :param content: The content of this PromptBot.
        :type: str
        """

        self._content = content

    @property
    def subject(self):
        """
        Gets the subject of this PromptBot.
        The subject of the default email.

        :return: The subject of this PromptBot.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this PromptBot.
        The subject of the default email.

        :param subject: The subject of this PromptBot.
        :type: str
        """

        self._subject = subject

    @property
    def generated_by(self):
        """
        Gets the generated_by of this PromptBot.
        Set when generated as a default by a bot.

        :return: The generated_by of this PromptBot.
        :rtype: str
        """
        return self._generated_by

    @generated_by.setter
    def generated_by(self, generated_by):
        """
        Sets the generated_by of this PromptBot.
        Set when generated as a default by a bot.

        :param generated_by: The generated_by of this PromptBot.
        :type: str
        """

        self._generated_by = generated_by

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