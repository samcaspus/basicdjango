from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'music'

urlpatterns = [
    url(r'music/delete/(?P<pk>[0-9]+)/', views.AlbumDelete.as_view(), name='delete-album'),
        url(r'music/update/(?P<pk>[0-9]+)/', views.AlbumUpdate.as_view(), name='update-album'),
    url(r'music/add', views.AlbumCreate.as_view(), name='add-album'),
    url(r'music/(?P<pk>[0-9]+)',views.DetailView.as_view() ,name='detail'),
    url(r'music', views.IndexView.as_view() , name='index'),
    url(r'', views.IndexView.as_view() , name='index'),

]
