"""IMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import myapp.views as views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login',views.auth,name='login'),
    path('verify_otp',views.otp,name="otp"),
    path('items',views.additems,name="items"),
    path('updateitems',views.updateitems,name="updateitems"),
    path('edit',views.edit,name="edit"),
    path('update',views.update,name="update"),
    path('delete',views.delete,name="delete"),
    path('Search items',views.search,name="search"),
    path('<int:id>/',views.sell,name="sell"),
    path('sell',views.sell,name="sell"),
    path('record',views.addRecords,name="record"),
    path('logout',views.logout_view,name="logout"),



]
