from django.urls import include, path
from account.views import RegistrationUser


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegistrationUser.as_view(), name='register'),
]
