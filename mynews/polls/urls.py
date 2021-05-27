from django.urls import path
from .views import *

urlpatterns = [
    path('category/<slug:slug>', Categories),
    path('', NewsListView.as_view(), name='title'),
    path('new/<slug:slug>', NewsDetailView.as_view(), name='title'),
    path('new/<slug:slug>', CategoryDetail.as_view(), name='title')
]