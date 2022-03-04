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
from api.url import router
from rest_framework.documentation import include_docs_urls 
from rest_framework.schemas import get_schema_view 
from django.urls import path, include

schema_view = get_schema_view(title='wildcart') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='wildcart')), 
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('drf_social_oauth2.urls',namespace='drf')),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('schema/', schema_view), 
]