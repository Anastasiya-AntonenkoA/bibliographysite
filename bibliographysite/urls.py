"""
URL configuration for bibliographysite project.

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
from django.contrib import admin
from django.urls import path
from bibliography import views
from bibliography.views import ResourceListView, ResourceSearchView, login_view, materials_view, add_resource_view
from django.urls import include

urlpatterns = {
    path('admin/', admin.site.urls),
    path('resources/', ResourceListView.as_view(), name='resource_list'),
    path('resources/search/', ResourceSearchView.as_view(), name='resource_search'),
    path('base/', views.home_page, name='home'),
    path('/about/', views.about_us, name='about_us'),
    path('contact/', views.contact_page, name='contact'),
    path('login/', login_view, name='login'),
    path('your-app/', include('your_app.urls')),
    path('materials/', materials_view, name='materials'),
    path('add-resource/', add_resource_view, name='add_resource'),
    path('edit-resource/<int:pk>/', views.edit_resource_view, name='edit_resource'),

}
