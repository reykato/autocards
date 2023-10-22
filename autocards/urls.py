"""
URL configuration for autocards project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def curry_redirect(target):
    def moved_permanently(request):
        return redirect(f'http://{request.get_host()}{target}')
    return moved_permanently

urlpatterns = [
    path('', curry_redirect('/autocards_app/browse_decks')),
    path('admin/', admin.site.urls),
    path('autocards_app/', include('autocards_app.urls'))
]
