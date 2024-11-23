"""
URL configuration for educa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 로그인 페이지로 연결
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # 로그아웃 페이지로 연결
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 관리자 페이지로 연결
    path('admin/', admin.site.urls),
    # 강좌 관련 URL을 포함
    path('course/', include('courses.urls')),
]

# 디버그 모드일 때 미디어 파일 제공
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
