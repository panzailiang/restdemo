# -*- encoding:utf8 -*-
"""restdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_nested import routers
from .myapp.apis import UserViewSet, GroupViewSet, MembershipViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
# router.register('groups/<int:group_pk>/', MembershipViewSet, base_name='membership')

# r2 = routers.DefaultRouter()
# r2.register('membership', MembershipViewSet, base_name='membership')
r2 = routers.NestedDefaultRouter(router, r'groups', lookup='group') 
r2.register('membership', MembershipViewSet, base_name='membership')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'docs/', include_docs_urls(title='My App API Docs', description='API接口')),
    path('', include(router.urls)),
    path('', include(r2.urls))
]
