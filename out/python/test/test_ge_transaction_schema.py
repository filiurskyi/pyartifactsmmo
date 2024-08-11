# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ge_transaction_schema import GETransactionSchema

class TestGETransactionSchema(unittest.TestCase):
    """GETransactionSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GETransactionSchema:
        """Test GETransactionSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GETransactionSchema`
        """
        model = GETransactionSchema()
        if include_optional:
            return GETransactionSchema(
                code = '',
                quantity = 56,
                price = 56,
                total_price = 56
            )
        else:
            return GETransactionSchema(
                code = '',
                quantity = 56,
                price = 56,
                total_price = 56,
        )
        """

    def testGETransactionSchema(self):
        """Test GETransactionSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
