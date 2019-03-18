"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""


from django.conf.urls import url
from blog2 import views

urlpatterns = [
    url(r'^index/$', views.index), #正则，^为匹配起始位置,$结尾
]