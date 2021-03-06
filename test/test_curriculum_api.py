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

from __future__ import absolute_import

import os
import sys
import unittest

import bombbomb
from bombbomb.rest import ApiException
from bombbomb.apis.curriculum_api import CurriculumApi


class TestCurriculumApi(unittest.TestCase):
    """ CurriculumApi unit test stubs """

    def setUp(self):
        self.api = bombbomb.apis.curriculum_api.CurriculumApi()

    def tearDown(self):
        pass

    def test_get_curricula(self):
        """
        Test case for get_curricula

        Get Curricula
        """
        pass

    def test_get_user_curriculum_with_progress(self):
        """
        Test case for get_user_curriculum_with_progress

        Get Detailed For User
        """
        pass


if __name__ == '__main__':
    unittest.main()
