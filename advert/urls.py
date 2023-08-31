from django.urls import path

from .views import index_

urlpatterns=[
    path('', index_)
]