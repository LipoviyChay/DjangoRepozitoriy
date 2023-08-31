from django.urls import path

from .views import dz_index

urlpatterns=[
    path('lesson_4', dz_index)
]