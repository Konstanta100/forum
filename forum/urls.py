from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #?P<pk> Django возьмёт всё, что придется на эту часть строки, и передаст представлению в качестве переменной pk
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
