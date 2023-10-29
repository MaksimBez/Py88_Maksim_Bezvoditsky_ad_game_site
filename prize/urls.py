from django.urls import include, path
from prize.views import SelectingPrize, MyPrize


urlpatterns = [
    path('prize/', SelectingPrize.as_view(), name='prize'),
    path('myprize/', MyPrize.as_view(), name='my_prize'),

]
