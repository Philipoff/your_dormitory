from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException
from passlib.context import CryptContext


class Auth:
    hasher = CryptContext(schemes=['bcrypt'])
    secret = "your_dormitory_ETU"

    def hash_password(self, password):
        return self.hasher.hash(password)

    def verify_password(self, password, hash_password):
        return self.hasher.verify(password, hash_password)

    def create_token(self, username):
        payload = {
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=0, minutes=30),
            "scope": "access_token",
            "sub": username
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm="HS256"
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            if payload["scope"] == "access_token":
                return payload["sub"]
            raise HTTPException(status_code=401, detail="Invalid scope for token")
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

    def create_refresh_token(self, username):
        payload = {
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=0, hours=10),
            "scope": "refresh_token",
            "sub": username
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm="HS256"
        )

    def refresh_token(self, refresh_token):
        try:
            payload = jwt.decode(refresh_token, self.secret, algorithms=['HS256'])
            if payload["scope"] == "refresh_token":
                username = payload["sub"]
                new_token = self.create_token(username)
                return new_token
            raise HTTPException(status_code=401, detail="Invalid scope for token")
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Refresh token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid refresh token")


if __name__ == "__main__":
    auth = Auth()
    test_hash = auth.hash_password("12345")
    is_correct = auth.verify_password("12345", test_hash)
    print(is_correct)
    print(test_hash)
