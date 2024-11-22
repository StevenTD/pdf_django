from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.page_request_list, name='page_list'),
]
