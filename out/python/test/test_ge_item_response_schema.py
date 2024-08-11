# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ge_item_response_schema import GEItemResponseSchema

class TestGEItemResponseSchema(unittest.TestCase):
    """GEItemResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GEItemResponseSchema:
        """Test GEItemResponseSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GEItemResponseSchema`
        """
        model = GEItemResponseSchema()
        if include_optional:
            return GEItemResponseSchema(
                data = openapi_client.models.ge_item_schema.GEItemSchema(
                    code = '', 
                    stock = 56, 
                    sell_price = 56, 
                    buy_price = 56, )
            )
        else:
            return GEItemResponseSchema(
                data = openapi_client.models.ge_item_schema.GEItemSchema(
                    code = '', 
                    stock = 56, 
                    sell_price = 56, 
                    buy_price = 56, ),
        )
        """

    def testGEItemResponseSchema(self):
        """Test GEItemResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
