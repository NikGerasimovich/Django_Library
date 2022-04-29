"""locallibrary URL Configuration

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
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='admin')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

""""" Есть несколько способов расширить urlpatternsсписок (ранее мы просто добавляли новый элемент списка, 
используя +=оператор для четкого разделения старого и нового кода). Вместо этого мы могли бы просто включить эту 
новую карту шаблонов в исходное определение списка: 
                                                    

urlpatterns += [
    path('catalog/', include('catalog.urls'))
]

# Принимает новый относительный URL для перенаправления на /catalog(1й арг)
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permament=True))
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""