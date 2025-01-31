from django.urls import path, include
from django.contrib import admin
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Optional, for admin panel
    path('saml2/', include('djangosaml2.urls')),  # SAML authentication routes
    path('accounts/profile/', views.home, name='home'),
]



