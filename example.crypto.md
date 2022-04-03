### crypto/diffie_hellman

- Both server and client generate a key pair (public and private) and exchange public key.
- Use received public key and own private key to calculate a common/shared private key.
- Server and client have same modulus and base to generate own key pair.

Run server.py first then client.py.
#### server
```
ycheng@nuc:/mnt/sdb/Data/learn/github/Algorithm_And_Data_Structure/crypto/diffie_hellman$ ./server.py
[Server]
- private key: 201
- public key: 10
- waiting new connection.
- connection from ('127.0.0.1', 37032).
- received data: 19 (client's public key)
- shared private key: 5
```

#### client
```
ycheng@nuc:/mnt/sdb/Data/learn/github/Algorithm_And_Data_Structure/crypto/diffie_hellman$ ./client.py
[Client]
- private key: 829
- public key: 19
- connecting to server ('localhost', 8899).
- connected
- received data: 10 (server's public key)
- shared private key: 5

```