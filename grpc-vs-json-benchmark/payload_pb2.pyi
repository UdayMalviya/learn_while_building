from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ("street", "city", "state", "zip")
    STREET_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    street: str
    city: str
    state: str
    zip: str
    def __init__(self, street: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., zip: _Optional[str] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("browser", "os", "latency")
    BROWSER_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    browser: str
    os: str
    latency: int
    def __init__(self, browser: _Optional[str] = ..., os: _Optional[str] = ..., latency: _Optional[int] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("type", "timestamp", "metadata")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    type: str
    timestamp: int
    metadata: Metadata
    def __init__(self, type: _Optional[str] = ..., timestamp: _Optional[int] = ..., metadata: _Optional[_Union[Metadata, _Mapping]] = ...) -> None: ...

class Profile(_message.Message):
    __slots__ = ("dob", "gender", "pan", "phones", "addresses")
    DOB_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    PAN_FIELD_NUMBER: _ClassVar[int]
    PHONES_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    dob: str
    gender: str
    pan: str
    phones: _containers.RepeatedScalarFieldContainer[str]
    addresses: _containers.RepeatedCompositeFieldContainer[Address]
    def __init__(self, dob: _Optional[str] = ..., gender: _Optional[str] = ..., pan: _Optional[str] = ..., phones: _Optional[_Iterable[str]] = ..., addresses: _Optional[_Iterable[_Union[Address, _Mapping]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "name", "email", "profile")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    email: str
    profile: Profile
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., profile: _Optional[_Union[Profile, _Mapping]] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ("request_id", "user", "events")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    user: User
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, request_id: _Optional[str] = ..., user: _Optional[_Union[User, _Mapping]] = ..., events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...
