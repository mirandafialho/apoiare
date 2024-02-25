from django.urls import re_path
from .views import HomeView, AboutView 

urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^about$', AboutView.as_view(), name='about')
]
