#!/usr/bin/python3
# ref: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange#Cryptographic_explanation
# ref: https://en.wikipedia.org/wiki/RSA_(cryptosystem)


shared_modulus = 23
shared_base = 5
print("shared modulus: %s" % shared_modulus)
print("shared base: %s" % shared_base)
print("-"*40)

alice_secret = 4
bob_secret = 3
print("alice's secret key: %s" % alice_secret)
print("bob's secret key: %s" % bob_secret)
print("-"*40)

A = (shared_base**alice_secret) % shared_modulus
B = (shared_base**bob_secret) % shared_modulus
print("alice's public key: %s" % A)
print("bob's public key: %s" % B)
print("-"*40)

alice_s = (B**alice_secret) % shared_modulus
bob_s = (A**bob_secret) % shared_modulus
print("alice's shared secret key: %s" % alice_s)
print("bob's shared secret key: %s" % bob_s)


