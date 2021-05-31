from django.conf.urls import url, include
from django.contrib import admin
from JMList import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^JMList/new$', views.New_List, name='View_List'),
    url(r'^JMList/(\d+)/$', views.View_List, name='View_Item'),
    url(r'^JMList/(\d+)/add_item$', views.Add_Item, name='Add_Item'),]


'''
from django.conf.urls import url
from JMList import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'), 
    ]'''