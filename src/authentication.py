# authentication.py
from rest_framework import authentication, exceptions
import secrets
from .models import Team


def generate_token():
    return secrets.token_hex(16)  # 32 characters


class SingleSessionAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if token:
            try:
                team = Team.objects.get(token=token)
                return (team, None)
            except Team.DoesNotExist:
                raise exceptions.AuthenticationFailed('Unauthorized! Invalid token')
        raise exceptions.AuthenticationFailed('Unauthorized! Token not provided')