import tink
from tink import aead
from tink import cleartext_keyset_handle

plaintext = b'your data...'
associated_data = b'context'

# Register all AEAD primitives
aead.register()

# 1. Get a handle to the key material.
with open("aes.gcm.keyset.json", 'r') as f:
  aes_gcm_keyset = f.read()

reader = tink.JsonKeysetReader(aes_gcm_keyset)
keyset_handle = cleartext_keyset_handle.read(reader)
#keyset_handle = tink.new_keyset_handle(aead.aead_key_templates.AES256_GCM)

# 2. Get the primitive.
aead_primitive = keyset_handle.primitive(aead.Aead)

# 3. Use the primitive.
ciphertext = aead_primitive.encrypt(plaintext, associated_data)

# 4. decrypt
decrypted = aead_primitive.decrypt(ciphertext, associated_data)
print(decrypted, associated_data)
