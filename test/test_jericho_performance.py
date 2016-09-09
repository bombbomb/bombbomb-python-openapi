# coding: utf-8

"""
    BombBomb

    We make it easy to build relationships using simple videos.

    OpenAPI spec version: 2.0.20679
    
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
from bombbomb.models.jericho_performance import JerichoPerformance


class TestJerichoPerformance(unittest.TestCase):
    """ JerichoPerformance unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJerichoPerformance(self):
        """
        Test JerichoPerformance
        """
        model = bombbomb.models.jericho_performance.JerichoPerformance()


if __name__ == '__main__':
    unittest.main()