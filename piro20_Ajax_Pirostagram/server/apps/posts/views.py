from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def main(request) :
    posts = Post.objects.all()
    
    comments_on_posts = {}

    for post in posts:
        comments = post.comments.all()
        comments_on_posts[post] = comments
        
    ctx={"posts":posts, "comments": comments_on_posts}
    return render(request, 'posts/main.html', ctx)

def create(request) :
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("/")
    else:
        form = PostForm()

    return render(request, "posts/post_create.html", {'form': form})
    

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
   
@csrf_exempt 
def post_like(request):
    req = json.loads(request.body) #id와 type 정보
    post_id = req['id']
    has_liked = req['type']
    
    post = Post.objects.get(id=post_id)
    
    if post.like % 2 == 0:
        post.like +=1
        has_liked +=1
    else:
        post.like -=1
        has_liked -=1
        
    post.save()
    
    return JsonResponse({'id': post_id, 'type': has_liked})