from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('new/<slug:slug>', NewsDetailView.as_view(), name='new'),
    path('test/<slug:slug>', CategoryDetail.as_view(), name='title')
    # path('r/register/$', RegisterFormView.as_view()),
    # path('r/login/$', LoginFormView.as_view()),
    # path('r/logout/$', LogiutFormView.as_view()),
]