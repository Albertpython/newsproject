from django.shortcuts import render
from django.views.generic import DetailView
from .models import News, World

def Norutyun(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news':news})



class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    models = News
    queryset = News.objects.all()
    context_object_name = 'News'

def Ashxarh(request):
    world = World.objects.all()
    return render(request, 'news.html', {'news':world})


# class WorldListView(ListView):
#     template_name = ('news.html')
#     models = World
#     queryset = World.objects.all()

class WorldDetailView(DetailView):
    template_name = 'world_detail.html'
    models = World
    queryset = World.objects.all()
    context_object_name = 'World'