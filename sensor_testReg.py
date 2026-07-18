import secrets
import hashlib

key = "cs_live_" + secrets.token_hex(32)

print(key)

print(
    hashlib.sha256(
        key.encode()
    ).hexdigest()
)