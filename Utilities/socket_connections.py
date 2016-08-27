from websocket import create_connection


socket_endpoints = {
    "mapping": 5000,
    "person": 5001,
    "world": 5002
}

def get_socket(end_point_name: string):
    return create_connection('ws://localhost:{0}'.format(socket_endpoints["end_point_name"]))