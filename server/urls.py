"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.documentation import include_docs_urls # new
from rest_framework.schemas import get_schema_view # new
from django.urls import path, include

schema_view = get_schema_view(title='wildcart') # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='wildcart')), # new
    path('api/', include('api.url')),
    path('schema/', schema_view), # new
]