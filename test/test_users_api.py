# coding: utf-8

"""
    BombBomb

    We make it easy to build relationships using simple videos.  # noqa: E501

    OpenAPI spec version: 2.0.831
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import bombbomb
from bombbomb.api.users_api import UsersApi  # noqa: E501
from bombbomb.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = bombbomb.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_client_contact_information(self):
        """Test case for get_client_contact_information

        Get client contact information.  # noqa: E501
        """
        pass

    def test_get_user_profile_info(self):
        """Test case for get_user_profile_info

        Get user profile information.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
