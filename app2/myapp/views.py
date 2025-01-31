from django.http import HttpResponse
import os
from django.http import HttpResponseRedirect
from djangosaml2.views import LogoutView
from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_in

def home(request):
    # Read the HTML file and return it as a response
    html_path = os.path.join(os.path.dirname(__file__), "home.html")
    with open(html_path, "r") as file:
        html_content = file.read()
    
    return HttpResponse(html_content, content_type="text/html")

