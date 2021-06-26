from django.conf.urls import url, include
from django.contrib import admin
from JMList import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),                        
    url(r'^new_validid$', views.new_validid, name='new_validid'),      
    url(r'^(\d+)/addemp_id$', views.addemp_id, name='addemp_id'),      
    url(r'^(\d+)/view_validid$', views.view_validid, name='view_validid'),
    url(r'^contacts/$', views.view_contact, name='view_contact'),
    url(r'^about/$', views.view_about, name='view_about'),

    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),


    ]


'''
    url(r'^healthandhistory/$', views.health_history, name='health_history'),
    url(r'^idlistandhealth/$', views.id_health, name='id_health'),
    url(r'^employment/$', views.dept_history, name='dept_history'),
    url(r'^contacts/$', views.view_contact, name='view_contact'),
    url(r'^about/$', views.view_about, name='view_about')
    #url(r'^JMList/(\d+)/$', views.view_list, name='view_list'),
    #url(r'^JMList/(\d+)/add_item$', views.add_item, name='add_item')
'''