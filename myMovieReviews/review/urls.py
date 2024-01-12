from django.urls import path, include
from .views import *

app_name = 'review'

urlpatterns = [
    path('', start, name='start'),
    path('reviews/', reviews_list, name='review_list'),
    path('reviews/<int:pk>', review_read),
    path('reviews/create', review_create),
    path('reviews/<int:pk>/update', review_update),
    path('reviews/<int:pk>/delete', review_delete),
]