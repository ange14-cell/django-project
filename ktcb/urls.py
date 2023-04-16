"""
URL configuration for ktcb project.

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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from account.views import signup
from store.views import product, product_detail, add_to_cart, cart, delele_cart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product, name='product'),
    path('product/<str:slug>/', product_detail, name='product_detail'),
    path('product/<str:slug>/add-to-cart', add_to_cart, name='add-to-cart'),
    path('cart/delete-cart/', delele_cart, name='delete-cart'),
    path('cart/', cart, name="cart"),
    path('signup/', signup, name='signup'),
    path("login/", views.LoginView.as_view(template_name="registration/login.html", redirect_authenticated_user=True), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),
    #path('compte/', include('django.contrib.auth.urls')),

    path('reset_password/', views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name='password_reset'),
    path('reset_password_send/', views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name='password_reset_sent'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

import django.contrib.auth.urls

