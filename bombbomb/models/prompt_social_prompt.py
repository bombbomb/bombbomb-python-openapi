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


class PromptSocialPrompt(object):
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
        'id': 'str',
        'user_id': 'str',
        'jericho_id': 'str',
        'prompt_subject': 'str',
        'prompt_html': 'str',
        'scheduled_send_date': 'datetime',
        'client_group_id': 'str',
        'thumbnail_url': 'str',
        'status': 'int',
        'created_date': 'datetime',
        'last_notified': 'datetime',
        'send_mechanism': 'datetime',
        'send_types': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'jericho_id': 'jerichoId',
        'prompt_subject': 'promptSubject',
        'prompt_html': 'promptHtml',
        'scheduled_send_date': 'scheduledSendDate',
        'client_group_id': 'clientGroupId',
        'thumbnail_url': 'thumbnailUrl',
        'status': 'status',
        'created_date': 'createdDate',
        'last_notified': 'lastNotified',
        'send_mechanism': 'sendMechanism',
        'send_types': 'sendTypes'
    }

    def __init__(self, id=None, user_id=None, jericho_id=None, prompt_subject=None, prompt_html=None, scheduled_send_date=None, client_group_id=None, thumbnail_url=None, status=None, created_date=None, last_notified=None, send_mechanism=None, send_types=None):  # noqa: E501
        """PromptSocialPrompt - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._user_id = None
        self._jericho_id = None
        self._prompt_subject = None
        self._prompt_html = None
        self._scheduled_send_date = None
        self._client_group_id = None
        self._thumbnail_url = None
        self._status = None
        self._created_date = None
        self._last_notified = None
        self._send_mechanism = None
        self._send_types = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if jericho_id is not None:
            self.jericho_id = jericho_id
        if prompt_subject is not None:
            self.prompt_subject = prompt_subject
        if prompt_html is not None:
            self.prompt_html = prompt_html
        if scheduled_send_date is not None:
            self.scheduled_send_date = scheduled_send_date
        if client_group_id is not None:
            self.client_group_id = client_group_id
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if status is not None:
            self.status = status
        if created_date is not None:
            self.created_date = created_date
        if last_notified is not None:
            self.last_notified = last_notified
        if send_mechanism is not None:
            self.send_mechanism = send_mechanism
        if send_types is not None:
            self.send_types = send_types

    @property
    def id(self):
        """Gets the id of this PromptSocialPrompt.  # noqa: E501

        The identifier of the prompt. Read Only.  # noqa: E501

        :return: The id of this PromptSocialPrompt.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PromptSocialPrompt.

        The identifier of the prompt. Read Only.  # noqa: E501

        :param id: The id of this PromptSocialPrompt.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this PromptSocialPrompt.  # noqa: E501

        The prompt's owner. Read Only.  # noqa: E501

        :return: The user_id of this PromptSocialPrompt.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PromptSocialPrompt.

        The prompt's owner. Read Only.  # noqa: E501

        :param user_id: The user_id of this PromptSocialPrompt.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def jericho_id(self):
        """Gets the jericho_id of this PromptSocialPrompt.  # noqa: E501

        If sent in a jericho context, this will have the jericho id  # noqa: E501

        :return: The jericho_id of this PromptSocialPrompt.  # noqa: E501
        :rtype: str
        """
        return self._jericho_id

    @jericho_id.setter
    def jericho_id(self, jericho_id):
        """Sets the jericho_id of this PromptSocialPrompt.

        If sent in a jericho context, this will have the jericho id  # noqa: E501

        :param jericho_id: The jericho_id of this PromptSocialPrompt.  # noqa: E501
        :type: str
        """

        self._jericho_id = jericho_id

    @property
    def prompt_subject(self):
        """Gets the prompt_subject of this PromptSocialPrompt.  # noqa: E501

        The prompt's subject line  # noqa: E501

        :return: The prompt_subject of this PromptSocialPrompt.  # noqa: E501
        :rtype: str
        """
        return self._prompt_subject

    @prompt_subject.setter
    def prompt_subject(self, prompt_subject):
        """Sets the prompt_subject of this PromptSocialPrompt.

        The prompt's subject line  # noqa: E501

        :param prompt_subject: The prompt_subject of this PromptSocialPrompt.  # noqa: E501
        :type: str
        """

        self._prompt_subject = prompt_subject

    @property
    def prompt_html(self):
        """Gets the prompt_html of this PromptSocialPrompt.  # noqa: E501

        The suggested script of the prompt.  # noqa: E501

        :return: The prompt_html of this PromptSocialPrompt.  # noqa: E501
        :rtype: str
        """
        return self._prompt_html

    @prompt_html.setter
    def prompt_html(self, prompt_html):
        """Sets the prompt_html of this PromptSocialPrompt.

        The suggested script of the prompt.  # noqa: E501

        :param prompt_html: The prompt_html of this PromptSocialPrompt.  # noqa: E501
        :type: str
        """

        self._prompt_html = prompt_html

    @property
    def scheduled_send_date(self):
        """Gets the scheduled_send_date of this PromptSocialPrompt.  # noqa: E501

        When the final email is scheduled to be sent  # noqa: E501

        :return: The scheduled_send_date of this PromptSocialPrompt.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_send_date

    @scheduled_send_date.setter
    def scheduled_send_date(self, scheduled_send_date):
        """Sets the scheduled_send_date of this PromptSocialPrompt.

        When the final email is scheduled to be sent  # noqa: E501

        :param scheduled_send_date: The scheduled_send_date of this PromptSocialPrompt.  # noqa: E501
        :type: datetime
        """

        self._scheduled_send_date = scheduled_send_date

    @property
    def client_group_id(self):
        """Gets the client_group_id of this PromptSocialPrompt.  # noqa: E501

        The client group campaign that created the prompt.  # noqa: E501

        :return: The client_group_id of this PromptSocialPrompt.  # noqa: E501
        :rtype: str
        """
        return self._client_group_id

    @client_group_id.setter
    def client_group_id(self, client_group_id):
        """Sets the client_group_id of this PromptSocialPrompt.

        The client group campaign that created the prompt.  # noqa: E501

        :param client_group_id: The client_group_id of this PromptSocialPrompt.  # noqa: E501
        :type: str
        """

        self._client_group_id = client_group_id

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this PromptSocialPrompt.  # noqa: E501

        The URL of a thumbnail image for this prompt  # noqa: E501

        :return: The thumbnail_url of this PromptSocialPrompt.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this PromptSocialPrompt.

        The URL of a thumbnail image for this prompt  # noqa: E501

        :param thumbnail_url: The thumbnail_url of this PromptSocialPrompt.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def status(self):
        """Gets the status of this PromptSocialPrompt.  # noqa: E501

        The status of the prompt: created = 0, sent = 10, recorded = 20, job_created = 30, timed_out = 40, declined = 50 Read Only  # noqa: E501

        :return: The status of this PromptSocialPrompt.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PromptSocialPrompt.

        The status of the prompt: created = 0, sent = 10, recorded = 20, job_created = 30, timed_out = 40, declined = 50 Read Only  # noqa: E501

        :param status: The status of this PromptSocialPrompt.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def created_date(self):
        """Gets the created_date of this PromptSocialPrompt.  # noqa: E501

        When the email was first sent out  # noqa: E501

        :return: The created_date of this PromptSocialPrompt.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this PromptSocialPrompt.

        When the email was first sent out  # noqa: E501

        :param created_date: The created_date of this PromptSocialPrompt.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def last_notified(self):
        """Gets the last_notified of this PromptSocialPrompt.  # noqa: E501

        When the user was last notified about a prompt email waiting for a video  # noqa: E501

        :return: The last_notified of this PromptSocialPrompt.  # noqa: E501
        :rtype: datetime
        """
        return self._last_notified

    @last_notified.setter
    def last_notified(self, last_notified):
        """Sets the last_notified of this PromptSocialPrompt.

        When the user was last notified about a prompt email waiting for a video  # noqa: E501

        :param last_notified: The last_notified of this PromptSocialPrompt.  # noqa: E501
        :type: datetime
        """

        self._last_notified = last_notified

    @property
    def send_mechanism(self):
        """Gets the send_mechanism of this PromptSocialPrompt.  # noqa: E501

        The sendMechanism property  # noqa: E501

        :return: The send_mechanism of this PromptSocialPrompt.  # noqa: E501
        :rtype: datetime
        """
        return self._send_mechanism

    @send_mechanism.setter
    def send_mechanism(self, send_mechanism):
        """Sets the send_mechanism of this PromptSocialPrompt.

        The sendMechanism property  # noqa: E501

        :param send_mechanism: The send_mechanism of this PromptSocialPrompt.  # noqa: E501
        :type: datetime
        """

        self._send_mechanism = send_mechanism

    @property
    def send_types(self):
        """Gets the send_types of this PromptSocialPrompt.  # noqa: E501

        The types of mechanisms this prompt can send.  # noqa: E501

        :return: The send_types of this PromptSocialPrompt.  # noqa: E501
        :rtype: list[str]
        """
        return self._send_types

    @send_types.setter
    def send_types(self, send_types):
        """Sets the send_types of this PromptSocialPrompt.

        The types of mechanisms this prompt can send.  # noqa: E501

        :param send_types: The send_types of this PromptSocialPrompt.  # noqa: E501
        :type: list[str]
        """

        self._send_types = send_types

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
        if not isinstance(other, PromptSocialPrompt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
