from django.urls import path
from . import views
from dashGraphs import *



urlpatterns = [
	path('', views.home, name='home'),


]