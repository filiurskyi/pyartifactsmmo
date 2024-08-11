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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pyartifactsmmo.models.announcement_schema import AnnouncementSchema
from typing import Optional, Set
from typing_extensions import Self

class StatusSchema(BaseModel):
    """
    StatusSchema
    """ # noqa: E501
    status: StrictStr = Field(description="Server status")
    version: Optional[StrictStr] = None
    characters_online: Optional[StrictInt] = None
    server_time: Optional[datetime] = None
    announcements: Optional[List[AnnouncementSchema]] = None
    last_wipe: StrictStr = Field(description="Last server wipe.")
    next_wipe: StrictStr = Field(description="Next server wipe.")
    __properties: ClassVar[List[str]] = ["status", "version", "characters_online", "server_time", "announcements", "last_wipe", "next_wipe"]

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
        """Create an instance of StatusSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in announcements (list)
        _items = []
        if self.announcements:
            for _item_announcements in self.announcements:
                if _item_announcements:
                    _items.append(_item_announcements.to_dict())
            _dict['announcements'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StatusSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "version": obj.get("version"),
            "characters_online": obj.get("characters_online"),
            "server_time": obj.get("server_time"),
            "announcements": [AnnouncementSchema.from_dict(_item) for _item in obj["announcements"]] if obj.get("announcements") is not None else None,
            "last_wipe": obj.get("last_wipe"),
            "next_wipe": obj.get("next_wipe")
        })
        return _obj


