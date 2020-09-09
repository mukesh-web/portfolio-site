"""portfolio URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog import views
urlpatterns = [
    path('',views.index,name='home'),
    path('portfolio/<int:blog_id>', views.portfolio, name='folio'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)