from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, New



class NewsListView(ListView):
    """ News """
    model = New
    queryset = New.objects.filter(status='published').order_by('-date')
    template_name = 'news_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class NewsDetailView(ListView):
    """ News new page """

    model = Category
    template_name = 'news_detail.html'
    def get_queryset(self, **kwargs):
        queryset = New.objects.filter(category__slug=self.kwargs['slug'], status='published').order_by('-date')
        return queryset



class CategoryDetail( ListView):
    """ News by category """

    template_name = 'category_detail.html'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        queryset = New.objects.filter(category__slug=self.kwargs['slug'], status='published').order_by('-date')
        return queryset

