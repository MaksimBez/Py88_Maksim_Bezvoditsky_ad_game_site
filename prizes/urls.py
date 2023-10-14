from django.urls import include, path
from prizes.views import SelectingPrizes


urlpatterns = [
    path('prizes/', SelectingPrizes.as_view(), name='prizes'),
]
