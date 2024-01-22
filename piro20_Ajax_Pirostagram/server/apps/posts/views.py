from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def main(request) :
    posts = Post.objects.prefetch_related('comments').all() #post 객체와 연관된 comment도 함께 다 가져오기
    ctx={"posts":posts}
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

@csrf_exempt
def comment(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        post_id = req.get('id')
        post_comment = req.get('comment')
        if post_id and post_comment:
            try:
                post = Post.objects.get(id=post_id)
                comment = Comment(post=post, content=post_comment)
                comment.save()
                return JsonResponse({'status': 'success'})
            except Post.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Post does not exist'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request data'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
        
        
@csrf_exempt
def get_comments(request, pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(post__id=pk)
        serialized_comments = [{'id': comment.id, 'content': comment.content} for comment in comments]
        return JsonResponse(serialized_comments, safe=False)

    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def delete_comment(request, postId, commentId):
    if request.method == "POST":
        post = Post.objects.get(id = postId)
        comment = Comment.objects.filter (id = commentId, post = post)
        comment.delete()
        return JsonResponse({'message': '댓글이 삭제되었습니다.'})