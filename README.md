# Python-Encryption  
​​
This is a simple and custom encryption method made in Python. It utilizes a combination of XOR and symmetric key encryption  

More specifically, it uses a one-time pad approach where the message is XORed with a random key that is generated from the encryption key. Then, the result is XORed with an initialization vector before being passed through a hash function (this is used to verify keys). Finally, the result is encoded in base64.  

The decryption algorithm reverses this process by decoding the base64-encoded input, and then reversing the XOR and symmetric encryption to retrieve the original message. However, both the original encryption key, and initialization vector are required to produce correct output.

## How to use

Here is an example of how a message can be encrypted

```python
# To use a custom key: pass it as a variable to the class.
encryption = XorCryption()
ciphertext, initialization_vector = encryption.encrypt('Hello, world!')

print('Original Message:', encryption.message)
print('Encrypted Message:', ciphertext)
print('Initialization Vector:', initialization_vector)
print('Used Encryption Key:', encryption.encryption_key_bytes.decode())
```

and here is an example of how a message can be decrypted

```python
encryption = XorCryption('(^yPu[v&gyVvc??OsZ{l,M;$]].~&2bjGGVk~S&al+KK4W{)Z{}efO33!h<L+Vm;ojyKfbL/EN1MGhj&I>MJ(-qX~V*+')
ciphertext = 'xhiQHoC9elO1ocNqWfN65Ebd9LjzxHH+KJ7gG7jzm9X81sbiJQ10EN3L3wUS'
initialization_vector = 'nO3T3j96IkHVwOUXUGMPTA=='
plaintext = encryption.decrypt(ciphertext, initialization_vector)

print('Encrypted message:', ciphertext)
print('Decrypted message:', plaintext)
```
