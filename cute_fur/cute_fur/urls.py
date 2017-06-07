"""cute_fur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from hardware import views as views_1
from hardware import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/',views_1.test),
    url(r'^index.html$',views_1.index),
    url(r'^$',views_1.index),
    url(r'^calendar.html$',views_1.calendar),
    url(r'^media.html$',views_1.media),
    url(r'^arduino',views_1.post_test),
    url(r'^testzpx', views_1.test_zpx),
    url(r'^dbtest', views_1.dbcreate),
    url(r'^dbset', views_1.dbset)
]
