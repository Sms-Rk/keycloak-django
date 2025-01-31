from django.http import HttpResponse
import os

def home(request):
    # Read the HTML file and return it as a response
    html_path = os.path.join(os.path.dirname(__file__), "home.html")
    with open(html_path, "r") as file:
        html_content = file.read()
    
    return HttpResponse(html_content, content_type="text/html")
