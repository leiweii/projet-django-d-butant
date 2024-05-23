"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from liste import views
import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('about-us/', views.about, name='about-us'),
    path('bands/', views.band_list),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/',views.band_list, name='band-list'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/change/', views.band_update, name='band-update'),
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'),

    path('annonces/', views.annonce_list),
    path('annonces/<int:id>/', views.annonce_det, name='annonce-det'),
    path('annonces/',views.annonce_list, name='annonce-list'),
    path('annoncec/add/', views.annonce_create, name='annonce-create'),
    path('annonces/<int:id>/change/', views.annonce_update, name='annonce-update'),
    path('annonces/<int:id>/delete/', views.annonce_delete, name='annonce-delete'),

    path('contact-us/',views.contact, name='contact'),
    path('confirmation/', views.confirmation, name='confirmation'),

    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', blog.views.home, name='home'),
]
