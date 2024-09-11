from oauth2_provider.decorators import protected_resource
from django.http import JsonResponse

@protected_resource(scopes=['read'])
def api_hello(request):
    return JsonResponse({"message": "Hello, OAuth2 World!"})
