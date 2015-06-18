#!/usr/bin/python3
"""Collection of Unit Tests for Application """
# __author__ = 'sfblackl'

import unittest

from runserver import application


class OtherItems(unittest.TestCase):
    """Universal Unit Tests for REST Service"""
    def test_health_app_pool(self):
        """Happy Path test of healthcheck, app pool"""
        with application.test_client(self) as tc1:
            response = tc1.get('/tradlabs/v1/health')
            self.assertEqual(response.status_code, 200)


# Allows to file to be run directly
if __name__ == '__main__':
    unittest.main()
