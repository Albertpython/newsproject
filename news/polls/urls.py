from django.urls import path
from.views import *

urlpatterns = [

	path('', Norutyun),
	path('news/<slug:slug>', NewsDetailView.as_view(), name='about'),
	path('', Ashxarh),
	# path('', WorldListView.as_view(), name='home'),
	path('news/<slug:slug>', WorldDetailView.as_view(), name='about'),

]