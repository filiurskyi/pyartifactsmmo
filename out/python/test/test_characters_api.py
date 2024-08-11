# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.characters_api import CharactersApi


class TestCharactersApi(unittest.TestCase):
    """CharactersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CharactersApi()

    def tearDown(self) -> None:
        pass

    def test_create_character_characters_create_post(self) -> None:
        """Test case for create_character_characters_create_post

        Create Character
        """
        pass

    def test_delete_character_characters_delete_post(self) -> None:
        """Test case for delete_character_characters_delete_post

        Delete Character
        """
        pass

    def test_get_all_characters_characters_get(self) -> None:
        """Test case for get_all_characters_characters_get

        Get All Characters
        """
        pass

    def test_get_character_characters_name_get(self) -> None:
        """Test case for get_character_characters_name_get

        Get Character
        """
        pass


if __name__ == '__main__':
    unittest.main()
