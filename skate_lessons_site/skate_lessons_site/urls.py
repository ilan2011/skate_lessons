"""skate_lessons_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from base import views as base_views
from lessons import views as lessons_views
from accounts import views as account_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.home, name='home'),
    path('about', base_views.about, name='about'),
    path('lessons/view_lessons', lessons_views.view_lessons, name='view_lessons'),
    path('lessons/book_lesson', lessons_views.book_lesson, name='book_lesson'),
    path('accounts/login/', account_views.login_view, name='login'),
    path('accounts/logout/', account_views.logout_view, name='logout'),
    path('accounts/signup/', account_views.signup_view, name='signup'),

]
