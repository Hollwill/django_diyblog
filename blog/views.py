from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormMixin
from .models import Blog, Comment, Blogger
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse


class BlogIndexView(TemplateView):
    template_name = 'blog/index.html'


class BlogsView(ListView):
    template_name = 'blog/blogs.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Blog.objects.all()
        # Отбираем первые 10 статей
        paginator = Paginator(articles, 5)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        return articles


class BloggersView(ListView):
    template_name = 'blog/bloggers.html'
    context_object_name = 'bloggers'

    def get_queryset(self):
        bloggers = Blogger.objects.all()
        return bloggers


class BloggerDetailView(DetailView):
    model = Blogger

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['blogs'] = Blog.objects.all()
        return context


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comments'] = Comment.objects.all()
        return context


class CommentCreateView(CreateView,):
    template_name = 'blog/create_comment.html'
    form_class = CommentForm
    model = Comment

    def get_success_url(self):
        return reverse('blog:blog_detail',
                       kwargs={'pk': str(self.object.blog.pk)})

    def form_valid(self, form):
        form.instance.commentator = self.request.user
        form.instance.blog = Blog.objects.get(pk=self.kwargs['pk'])
        return super(CommentCreateView, self).form_valid(form)

    def get_queryset(self):
        return Blog.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['blog'] = Blog.objects.get(pk=self.kwargs['pk'])
        return context
