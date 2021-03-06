"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from directory import views
from django.conf import settings
# from rest_framework.urlpatterns import format_suffix_pattern

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^update/(?P<pid>\d+)/$', views.update_contact, name='update_contact'),
    url(r'^delete/(?P<pid>\d+)/$', views.delete_contact, name='delete_contact'),
    url(r'^json$', views.ContactList.as_view()),
    url(r'^json/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

