from django.urls import include, path
from promocode.views import RegistrationPromocode


urlpatterns = [
    path('promocode/', RegistrationPromocode.as_view(), name='promocode'),
]
