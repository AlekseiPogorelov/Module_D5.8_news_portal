from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class SearchPostList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'search.html'
    context_object_name = 'newsposts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'newsposts'
    paginate_by = 10


    # def get_queryset(self):
    #     return Post.objects.filter(categoryType='NW')


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'newspost'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

    # def get_queryset(self):
    #
    #     return Post.objects.filter(categoryType='NW')


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ArticleList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'newsposts'
    paginate_by = 10


class ArticleDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'newspost'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('article.add_article',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('article.change_article',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('article.delete_article',)
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')