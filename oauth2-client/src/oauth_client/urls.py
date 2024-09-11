from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('oauth/login/', views.oauth_login, name='oauth_login'),
    path('oauth/callback/', views.oauth_callback, name='oauth_callback'),
    path('protected-resource/', views.protected_resource, name='protected_resource'),
]
