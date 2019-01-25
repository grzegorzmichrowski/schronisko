"""Projekt_koncowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Projekt_koncowy import settings
from animals.views import MainView, AnimalCreate, AnimalUpdate, AnimalDelete, BoxCreate, AnimalListWithFilterView
from employees.views import EmployeeCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', MainView.as_view(), name="main"),
    path('add_animal', AnimalCreate.as_view(), name="add_animal"),
    path('update_animal/<pk>', AnimalUpdate.as_view(success_url="/animal_list"), name="update_animal"),
    path('delete_animal/<pk>', AnimalDelete.as_view(), name="delete_animal"),
    path('add_employee', EmployeeCreate.as_view(), name="add_employee"),
    path('add_box', BoxCreate.as_view(), name="add_box"),
    path('animal_list', AnimalListWithFilterView.as_view(), name="animal_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

