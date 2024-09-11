from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from oauth2_provider.decorators import protected_resource
from django.http import JsonResponse

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

@protected_resource(scopes=['read'])
def api_hello(request):
    return JsonResponse({"message": "Hello, OAuth2 World!"})

# oauth2-server/src/oauth_server/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/hello/', views.api_hello, name='api_hello'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
]
