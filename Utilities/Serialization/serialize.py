
def serialize(message):
    message.type = type(message).__name__
    return message.SerializeToString()