# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Max Bader
# mibader@uci.edu
# 77466224

import json
import socket
from ds_protocol import extract_json
import time


def connection(server, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server, port))
    return client


def json_data(username, password):
    data = {"join": {"username": username, "password": password, "token": ""}}
    return json.dumps(data)


def write_message(token, message, send_s):
    r_message = json.dumps({"token": token, "post": {"entry": message, "timestamp": str(time.time())}})
    send_s.write(r_message + "\r\n")
    send_s.flush()


def write_bio(token, bio, send_s):
    bio_message = json.dumps({"token": token, "bio": {"entry": bio, "timestamp": str(time.time())}})
    send_s.write(bio_message + '\r\n')
    send_s.flush()


def send(server: str, port: int, username: str, password: str, message: str, bio: str = None):
    """
    Send function joins a ds server and sends a message, bio, or both.

    :param server: The ip address for the ICS 32 DS server.
    :param port: The port where the ICS 32 DS server is accepting connections.
    :param username: The user name to be assigned to the message.
    :param password: The password associated with the username.
    :param message: The message to be sent to the server.
    :param bio: Optional, a bio for the user.
    """
    # TODO: return either True or False depending on results of required operation
    try:
        client = connection(server, port)

        send_s = client.makefile('w')
        receive_s = client.makefile('r')

        json_line = json_data(username, password)

        send_s.write(json_line + '\r\n')
        send_s.flush()

        response = receive_s.readline()
        response_tuple = extract_json(response)

        token = response_tuple.token
        
        if "response" in response:
            if response_tuple.type == "ok":
                write_message(token, message, send_s)

                if bio:
                    write_bio(token, bio, send_s)
        
                return True
          
            elif response_tuple.type == "error":
                print("Error")

        else:
            print("Error: invalid format")
            return False
      
    except Exception as e:
        print(f"Error: {e}")
        return False

    client.close()
