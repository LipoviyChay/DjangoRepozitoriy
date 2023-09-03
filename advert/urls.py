from django.urls import path

from .views import index_, top_sellers

urlpatterns=[
    path('', index_, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers')
]