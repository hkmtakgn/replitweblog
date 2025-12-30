from django.shortcuts import render
from replitweblog.models import Post


def replitweblog_home(request):
    posts = Post.objects.all()
    if posts is not None:
        posts = posts
    else:
        posts = None
    context = dict(posts=posts, )
    return render(request, "main/replitweblog-home.html", context)
