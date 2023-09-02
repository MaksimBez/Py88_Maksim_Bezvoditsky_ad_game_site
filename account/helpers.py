from django.contrib.sites.models import Site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model

User = get_user_model()

SEPARATOR = 'SEPARATOR'


def get_current_host():
    try:
        return f'http://{Site.objects.get_current().domain}'
    except Site.DoesNotExist:
        return 'localhost'


def generate_activation_link(user):
    activation_link = urlsafe_base64_encode(
        force_bytes(f'{user.id}{SEPARATOR}{user.email}')
    )
    return activation_link


def check_activation_link(link):
    checking_data = force_str(urlsafe_base64_decode(link))
    user_id, email = checking_data.split(SEPARATOR)
    try:
        user = User.objects.get(id=user_id, email=email)
        return user
    except User.DoesNotExist:
        return None
