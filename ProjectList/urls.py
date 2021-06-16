from django.conf.urls import url, include
from django.contrib import admin
from JMList import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),
    url('homepage/', views.home_page, name='home_page'),
    url('idlist/', views.emp_id, name='emp_id'),
    url('healthandhistory/', views.health_history, name='health_history'),
    url('idlistandhealth/', views.id_health, name='id_health'),
    url('employment/', views.dept_history, name='dept_history'),
    url('contacts/', views.view_contact, name='view_contact'),
    url('about/', views.view_about, name='view_about')]
    #url(r'^JMList/(\d+)/$', views.view_list, name='view_list'),
    #url(r'^JMList/(\d+)/add_item$', views.add_item, name='add_item')