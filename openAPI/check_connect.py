import platform
import socket

from flask import jsonify

def check_connection_type():

    if not platform.node():
        is_connected_to = "No Network Name Found"
    else:
        network_name = platform.node()
        host = socket.gethostbyname(network_name)
        host = str(host)

        if "127" in host:
            is_connected_to = "Connected to Localhost"
        else:
            is_connected_to = "Connected to Internet"

    connection_info = {"connection": is_connected_to}
    return jsonify(connection_info)




