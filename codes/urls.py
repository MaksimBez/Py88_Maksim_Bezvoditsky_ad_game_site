from django.urls import include, path
from codes.views import RegistrationCodes


urlpatterns = [
    path('codes/', RegistrationCodes.as_view(), name='codes'),
]
