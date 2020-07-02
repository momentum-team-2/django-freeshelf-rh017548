"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from core import views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('core_temp/', core_views.list_books, name='list_books'),
    path('core_temp/add/', core_views.add_book, name='add_book'),
    path('core_temp/<int:pk>/', core_views.show_book, name='show_book'),
    path('core_temp/<int:pk>/edit/', core_views.edit_book,
         name='edit_book'),
    path('core_temp/<int:pk>/delete/', core_views.delete_book,
         name='delete_book'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
         
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
