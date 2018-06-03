from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Post, CommentPost


def post_list(request):
    post = Post.objects.filter(moder=True)
    return render(request, "post/post_list.html", {"posts": post})

def post_single(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = CommentPost.objects.filter(post=post, moder=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.user = request.user
            comm.post = post
            comm.save()
    else:
        form = CommentForm()
    return render(request, "post/post_single.html", {"post": post, "form":
        form, 'comment':comment})
# from django.template import loader, Context
# from django.http import HttpResponse
# from post.models import BlogPost
# from django.core.context_processors import csrf
# from django.shortcuts import render
#
# def archive(request):
#     posts = BlogPost.objects.all()
#     t = loader.get_template("archive.html")
#     c = Context({"posts": posts })
#     c.update(csrf(request))
#     return HttpResponse(t.render(c))