from django.urls import path, include
from .views import *

app_name = 'review'

urlpatterns = [
    path('', reviews_list, name='review_list'),
    path('<int:pk>', review_read),
    path('create', review_create),
]