from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone
from django.http import Http404


def index(request):
    template = 'blog/index.html'
    context = {'post_list': Post.objects.filter(is_published__exact=True,
                                                category__is_published__exact=True,
                                                pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
                }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post, id=post_id, pub_date__lte=timezone.now(),
                             is_published=True, category__is_published=True)

    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'

    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    post_list = Post.objects.filter(is_published__exact=True,
                                    pub_date__lte=timezone.now(),
                                    category__slug=category_slug).order_by('-pub_date')

    context = {'post_list': post_list,
               'category': category}
    return render(request, template, context)
