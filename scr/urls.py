"""scr URL Configuration

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
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from pages.views import home_view, contact_view, sign_in, logout_view, login_view, text_view, car_view, order_view, material, listall, delete, about, collect,history, us, detail, detail1, detail3, detail4, detail5, detail6, detail7
urlpatterns = [
    path('home/', home_view, name='home'),
    path('contact/', contact_view),
    path('sign/', sign_in),
    path('login/', login_view),
    path('logout/', logout_view),
    path('profile/', home_view),
    path('text/', text_view),
    path('car/', car_view),
    path('order/', order_view),
    path('material/', material),
    path('listall/', listall),
    path('delete/', delete),
    path('about/', about),
    path('collect/', collect),
    path('us/', us),
    path('history/', history),
    path('detail/<int:id>/', detail, name='detail'),
    path('detail1/', detail1),
    path('detail3/', detail3),
    path('detail4/', detail4),
    path('detail5/', detail5),
    path('detail6/', detail6),
    path('detail7/', detail7),

    path('admin/', admin.site.urls),
]+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
