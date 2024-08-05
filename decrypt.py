# Encrypted password and key
enc_password = "0Nv32PTwgYjzg9/8j5TbmvPd3e7WhtWWyuPsyO76/Y+U193E"
key = "armando"

# Convert enc_password from Base64 to byte array
enc_password_bytes = base64.b64decode(enc_password)

# Convert key to byte array
key_bytes = key.encode('ascii')

# Initialize an empty byte array for the decrypted password
decrypted_bytes = bytearray(len(enc_password_bytes))

# Decrypt the password using XOR with the key and 223
for i in range(len(enc_password_bytes)):
    decrypted_bytes[i] = enc_password_bytes[i] ^ key_bytes[i % len(key_bytes)] ^ 223

# Convert the decrypted byte array back to a string
decrypted_password = decrypted_bytes.decode('ascii')

print("Decrypted Password:", decrypted_password)
