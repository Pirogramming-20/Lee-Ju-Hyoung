from django.urls import path
from .views import *

app_name = 'idea'

urlpatterns = [
    path('', main, name="main"),
    path('create/', create, name="create"),
    path('detail/<int:pk>/', detail, name="detail"),
    path('delete/<int:pk>/', delete, name="delete"),
    path('update/<int:pk>/', update, name="update"),
    path('sort/<str:sort_option>/', idea_list, name='idea_list_sorted'),
]
