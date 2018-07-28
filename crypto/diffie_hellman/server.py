#!/usr/bin/python3

import sys, os, json, random, socket

SHARED_MODULUS = 23
SHARED_BASE = 5


def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('0.0.0.0', 8899)
    sock.bind(server_address)
    sock.listen(1)
    print("[Server]")

    while True:
        try:
            private_key = random.randrange(100)
            public_key = (SHARED_BASE**private_key) % SHARED_MODULUS
            print("- private key: %s" % private_key)
            print("- public key: %s" % public_key)

            print("- waiting new connection.")
            connection, client_address = sock.accept()

            print("- connection from %s." % str(client_address))
    
            data = connection.recv(32)
            print("- received data: %s" % int(data))
            if data.isdigit():
                client_pub_key = int(data)
                shared_secret_key = (client_pub_key**private_key) % SHARED_MODULUS

                connection.sendall(str(public_key).encode('utf-8'))

                print("- shared private key: %s" % shared_secret_key)

            connection.close()
            print("")

        except KeyboardInterrupt as e:
            print("server stop.")
            break

        except Exception as e:
            print("Error, %s" % e)
            break

    sock.close()


if __name__ == '__main__':
    main()
