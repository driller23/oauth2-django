import requests
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def oauth_login(request):
    auth_url = (f"{settings.OAUTH2_PROVIDER['AUTHORIZATION_URL']}?"
                f"client_id={settings.OAUTH2_PROVIDER['CLIENT_ID']}&"
                f"redirect_uri={settings.OAUTH2_PROVIDER['REDIRECT_URL']}&"
                f"scope={settings.OAUTH2_PROVIDER['SCOPE']}&"
                f"response_type=code")
    return redirect(auth_url)

def oauth_callback(request):
    code = request.GET.get('code')
    token_url = settings.OAUTH2_PROVIDER['TOKEN_URL']
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': settings.OAUTH2_PROVIDER['REDIRECT_URL'],
        'client_id': settings.OAUTH2_PROVIDER['CLIENT_ID'],
        'client_secret': settings.OAUTH2_PROVIDER['CLIENT_SECRET'],
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get('access_token')
    request.session['oauth_token'] = access_token
    return redirect('protected_resource')

def protected_resource(request):
    token = request.session.get('oauth_token')
    if not token:
        return redirect('oauth_login')
    
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('http://oauth2-server:8000/api/hello/', headers=headers)
    
    if response.status_code == 200:
        return HttpResponse(f"Protected Resource: {response.json()['message']}")
    else:
        return HttpResponse("Failed to access protected resource", status=403)
