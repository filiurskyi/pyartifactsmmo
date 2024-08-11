# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from pyartifactsmmo.models.character_schema import CharacterSchema
from pyartifactsmmo.models.cooldown_schema import CooldownSchema
from pyartifactsmmo.models.item_schema import ItemSchema
from typing import Optional, Set
from typing_extensions import Self

class EquipRequestSchema(BaseModel):
    """
    EquipRequestSchema
    """ # noqa: E501
    cooldown: CooldownSchema = Field(description="Cooldown details.")
    slot: StrictStr = Field(description="Item slot.")
    item: ItemSchema = Field(description="Item details.")
    character: CharacterSchema = Field(description="Player details.")
    __properties: ClassVar[List[str]] = ["cooldown", "slot", "item", "character"]

    @field_validator('slot')
    def slot_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['weapon', 'shield', 'helmet', 'body_armor', 'leg_armor', 'boots', 'ring1', 'ring2', 'amulet', 'artifact1', 'artifact2', 'artifact3', 'consumable1', 'consumable2']):
            raise ValueError("must be one of enum values ('weapon', 'shield', 'helmet', 'body_armor', 'leg_armor', 'boots', 'ring1', 'ring2', 'amulet', 'artifact1', 'artifact2', 'artifact3', 'consumable1', 'consumable2')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EquipRequestSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cooldown
        if self.cooldown:
            _dict['cooldown'] = self.cooldown.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of character
        if self.character:
            _dict['character'] = self.character.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EquipRequestSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cooldown": CooldownSchema.from_dict(obj["cooldown"]) if obj.get("cooldown") is not None else None,
            "slot": obj.get("slot"),
            "item": ItemSchema.from_dict(obj["item"]) if obj.get("item") is not None else None,
            "character": CharacterSchema.from_dict(obj["character"]) if obj.get("character") is not None else None
        })
        return _obj


