# coding: utf-8

"""
    Reseplaneraren

    Provides access to Västtrafik journey planner

    OpenAPI spec version: 1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.livemap_api import LivemapApi


class TestLivemapApi(unittest.TestCase):
    """ LivemapApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.livemap_api.LivemapApi()

    def tearDown(self):
        pass

    def test_livemap(self):
        """
        Test case for livemap

        Returns the positions of all vehicles in a given bounding box
        """
        pass


if __name__ == '__main__':
    unittest.main()
