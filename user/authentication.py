import jwt
from jwt import PyJWKClient
from rest_framework import authentication, exceptions
import os
from dotenv import load_dotenv
from .models import User


class Auth0JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        load_dotenv()
        token = self._get_token(request)
        if not token:
            return None

        try:
            jwks_client = PyJWKClient(
                f"https://{os.getenv('AUTH0_DOMAIN')}/.well-known/jwks.json")
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=os.getenv("AUTH0_ALGORITHMS"),
                audience=os.getenv("AUTH0_AUDIENCE"),
                issuer=f"https://{os.getenv('AUTH0_DOMAIN')}/",
            )
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Token expired")
        except jwt.PyJWTError as e:
            print(e)
            raise exceptions.AuthenticationFailed("Invalid token") from e

        user = self._get_user(payload)
        return (user, None)

    def _get_token(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        if auth_header.startswith("Bearer "):
            return auth_header.split(" ")[1]
        return None

    def _get_user(self, payload):
        auth0_id = payload.get("sub")  # Auth0 user ID
        try:
            return User.objects.get(auth0_id=auth0_id)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("User not found")
