from google.protobuf.internal.containers import BaseContainer
from google.protobuf.reflection import GeneratedProtocolMessageType
from google.protobuf.message import Message as ProtocolMessage, DecodeError


def copy_pb_to_dict(dictionary, instance):
    for descriptor, value in instance.ListFields():
        # If the field is another Protobuf Message, make a new dictionary
        # and copy the messages fields
        if isinstance(value, ProtocolMessage):
            dictionary[descriptor.name] = {}
            copy_pb_to_dict(dictionary[descriptor.name], value)
        # If the field is repeated, create a list and copy the repeated field
        # values into the dictionary
        elif isinstance(value, BaseContainer):
            dictionary[descriptor.name] = []
            for item in value:
                if isinstance(item, ProtocolMessage):
                    dict_item = {}
                    copy_pb_to_dict(dict_item, item)
                    dictionary[descriptor.name].append(dict_item)
                else:
                    dictionary[descriptor.name].append(item)
        # Otherwise the field value is just a basic type and should be set
        # on the dict.
        else:
            dictionary[descriptor.name] = value
