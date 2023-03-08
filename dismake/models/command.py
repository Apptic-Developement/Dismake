from __future__ import annotations
import re

from pydantic import BaseModel, validator
from typing import Any, Optional
from ..types import CommandTypes, OptionTypes, SnowFlake

__all__ = ("Option", "Choice", "SlashCommand")
# SLASH_COMMAND_REGEX = re.compile(r"^[-_\p{L}\p{N}\p{sc=Deva}\p{sc=Thai}]{1,32}$")


class Option(BaseModel):
    name: str
    description: str = "No Description Provided."
    choices: Optional[list[Choice]] = None
    channel_types: Optional[str] = None # TODO: Optional[ChannelTypes]
    min_value: Optional[int] = None
    max_value: Optional[int] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    required: Optional[bool] = False
    type: int = OptionTypes.STRING
    autocomplete: Optional[bool] = None

    class Config:
        arbitrary_types_allowed = True

class Choice(BaseModel):
    name: str
    value: str | int | float


class SlashCommand(BaseModel):
    id: SnowFlake | None = None
    type: int = CommandTypes.SLASH
    application_id: Optional[SnowFlake] = None
    guild_id: Optional[SnowFlake] = None
    name: str
    name_localizations: Optional[list[dict[str, Any]]] = None
    description: str
    description_localizations: Optional[list[dict[str, Any]]] = None
    options: Optional[list[Option]] = None
    default_member_permissions: Optional[str] = None
    dm_permission: Optional[bool] = None
    default_permission: Optional[bool] = None
    nsfw: Optional[bool] = None
    version: Optional[int] = None

    class Config:
        arbitrary_types_allowed = True
    
    
    # @validator("name")
    # def validate_name(cls, name: str):
    #     match = SLASH_COMMAND_REGEX.match(name)
    #     if match is None:
    #         raise ValueError(
    #             f"{name!r} must be between 1-32 characters and contain only lower-case letters, numbers, hyphens, or underscores."
    #         )

    #     if name.lower() != name:
    #         raise ValueError(f'{name!r} must be all lower-case')
    #     return name


