from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/index.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']
    success_url = reverse_lazy('music:index')
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']
    success_url = reverse_lazy('music:index')

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')





























'''from django.http import HttpResponse,Http404
from .models import Album
from django.views import
from django.shortcuts import render
from django.template import loader
# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    path = 'music/index.html'
    content = {
    'all_albums':all_albums,
    }
    return render(request,path,content)



def detail(request,album_id):
    try:
        album = Album.objects.get(pk = album_id)
    except:
        raise Http404("dosent exist")
    return HttpResponse('this is your album id = '+str(album_id))
'''
