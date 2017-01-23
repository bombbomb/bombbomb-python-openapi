# coding: utf-8

"""
    BombBomb

    We make it easy to build relationships using simple videos.

    OpenAPI spec version: 2.0.22196
    
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
from bombbomb.apis.videos_api import VideosApi


class TestVideosApi(unittest.TestCase):
    """ VideosApi unit test stubs """

    def setUp(self):
        self.api = bombbomb.apis.videos_api.VideosApi()

    def tearDown(self):
        pass

    def test_get_video_recorder(self):
        """
        Test case for get_video_recorder

        Get Live Video Recorder HTML
        """
        pass

    def test_mark_live_recording_complete(self):
        """
        Test case for mark_live_recording_complete

        Completes a live recording
        """
        pass

    def test_sign_upload(self):
        """
        Test case for sign_upload

        Generate Signed Url
        """
        pass


if __name__ == '__main__':
    unittest.main()
