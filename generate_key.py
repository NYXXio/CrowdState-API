import secrets

from app.security.hashing import hash_api_key


api_key = "cs_live_" + secrets.token_hex(32)

print()

print("API KEY")

print(api_key)

print()

print("HASH")

print(hash_api_key(api_key))