from django.conf.urls import url, include
from django.contrib import admin
from JMList import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^JMList/new$', views.new_list, name='new_list'),
    url(r'^JMList/(\d+)/$', views.view_list, name='view_list'),
    url(r'^JMList/(\d+)/add_item$', views.add_item, name='add_item'),]


'''
from django.conf.urls import url
from JMList import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'), 
    ]'''