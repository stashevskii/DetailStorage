import bcrypt


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def compare_passwords(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)


def get_bytes_from_db_hex_hash(db_hex_hash: str) -> bytes:
    return bytes.fromhex(db_hex_hash[2:])
