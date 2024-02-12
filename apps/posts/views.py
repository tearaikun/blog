from django.shortcuts import render

from apps.posts.models import Post


def get_post(request):
    posts = Post.objects.all()
    return render(request, 'posts/post.html', {'posts': posts})