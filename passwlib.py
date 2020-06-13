from passlib.hash import pbkdf2_sha256
#external lib

DEFAULT_PASSWD_URI = "data/passw.db"

def verify_password(in_passw):
    base_passw_hash = ""

    with open(DEFAULT_PASSWD_URI, "r") as file:
        base_passw_hash = file.read().rstrip()

    return pbkdf2_sha256.verify(in_passw, base_passw_hash)

def set_password(passw):
    hashed_pass = pbkdf2_sha256.hash(passw)
    with open(DEFAULT_PASSWD_URI, "w") as file:
        file.write(hashed_pass)
