from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . models import Post,Category
from .forms import PostForm
from django . urls import reverse_lazy
from django.views import View

# Create your views here.
# def home(request):
#     return render(request,'home.html')
class HomeView(ListView):
    model= Post
    template_name = 'home.html'
    ordering = ['-id']
    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})
class Categoryview(View):
    def get(self, request, cats):
        category_post = Post.objects.filter(category = cats)
        return render(request,'category.html',{'cats':cats.title(),'category_post':category_post})
class ArticleView(DetailView):
    model= Post
    template_name = 'article_detail.html'
    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
class AddpostView(CreateView):
    model= Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
class AddCategoryView(CreateView):
    model= Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
class updatepostview(UpdateView):
    model= Post
    template_name = 'update_post.html'
    form_class = PostForm
    # fields = ['title','title_tag','body']
class deletepostview(DeleteView):
    model= Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    