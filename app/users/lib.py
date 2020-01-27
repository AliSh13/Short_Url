from werkzeug.security import generate_password_hash, check_password_hash


def generate_hash(password):
    _hash = generate_password_hash(password)
    return _hash


def check_hash(hash, password):
    return check_password_hash(hash, password)