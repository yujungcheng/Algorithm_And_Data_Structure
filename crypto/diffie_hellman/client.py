#!/usr/bin/python3

import sys, os, json, random, socket

SHARED_MODULUS = 23
SHARED_BASE = 5


def main():

    print("[Client]")
    private_key = random.randrange(100)
    public_key = (SHARED_BASE**private_key) % SHARED_MODULUS

    print("- private key: %s" % private_key)
    print("- public key: %s" % public_key)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 8899)
        print("- connecting to server %s." % str(server_address))
        sock.connect(server_address)
        print("- connected")

        sock.sendall(str(public_key).encode('utf-8'))

        data = sock.recv(32)
        print("- received data: %s" % int(data))
        if data.isdigit():
            server_public_key = int(data)
            shared_secret_key = (server_public_key**private_key) % SHARED_MODULUS
            print("- shared private key: %s" % shared_secret_key)


    except Exception as e:
        print("Error, %s" %e)

    finally:
        sock.close()


if __name__ == '__main__':
    main()
