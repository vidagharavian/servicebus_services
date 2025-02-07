import datetime
import inspect
import uuid
from typing import Any


class MessageFormatter:
    revision = "1"
    writer: str
    transport: str
    messageId = str(
        uuid.uuid4())
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    isError = False
    isDuplicate = False
    messageContentType = "application/json"
    messageEncoding = "None"

    def __init__(self, revision, writer, transport,receivedTs, messageId=None, timestamp=None, isError=False,
                 isDuplicate=False, messageEncoding="None"):
        self.revision = revision
        self.writer = writer
        self.transport = transport
        if messageId is not None:
            self.messageId = messageId
        if timestamp is not None:
            self.timestamp = datetime.datetime.now(timestamp).isoformat()
        self.isError = bool(isError)
        self.isDuplicate = bool(isDuplicate)
        self.messageEncoding = messageEncoding
        self.receivedTs = receivedTs

    def to_dict(self) -> dict[str, Any]:
        attributes = {k: v for k, v in self.__dict__.items() if
                      not callable(v) and not k.startswith('_')}
        properties = {key: v.fget(self) for key, v in inspect.getmembers(self.__class__) if
                      isinstance(v, property) and key != 'fmt'}
        attributes.update(properties)
        return attributes
