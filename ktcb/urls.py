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
from django.urls import path, include
from account.views import signup
from store.views import home, product, product_detail, add_to_cart, cart, delele_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product, name='product'),
    path('product/<str:slug>/', product_detail, name='product_detail'),
    path('product/<str:slug>/add-to-cart', add_to_cart, name='add-to-cart'),
    path('cart/delete-cart/', delele_cart, name='delete-cart'),
    path('cart/', cart, name="cart"),
    path('signup/', signup, name='signup'),
    path('compte/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

