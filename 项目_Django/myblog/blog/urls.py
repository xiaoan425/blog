"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),  # 正则，^为匹配起始位置,$结尾
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)/$', views.edit_page,name='edit_page'),
    url(r'^edit/action/$',views.edit_action,name='edit_action')
]
