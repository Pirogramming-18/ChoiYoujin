from django.shortcuts import render, redirect
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.

def post_feed(request):
    posts_list = []
    posts = Post.objects.all()
    for post in posts:
        comment_count = post.comment_set.all().count()
        post_count = post.postlike_set.all().count()
        is_liked_post = request.user.postlike_set.filter(post = post.id)
        posts_list.append((post, comment_count, post_count, is_liked_post))
    current_user = request.user
    ctx = {
        'posts' : posts_list,
        'current_user' : current_user,
    }
    return render(request, 'post_feed.html', context=ctx)


@csrf_exempt
def post_detail(request, pk):
    post = Post.objects.get(id = pk)
    user = request.user
    is_liked_post = request.user.postlike_set.filter(post = post.id)
    post_count = post.postlike_set.all().count()
    if request.method == 'POST':
        if request.POST['comment'] != '':
            comment_content = request.POST['comment']
            comment = Comment()
            comment.writer = request.user
            comment.post = post
            comment.content = comment_content
            comment.depth = 0
            comment.sequence = post.comment_set.all().count() + 1
            comment.save()
        else:
            messages.warning(request, '댓글을 다시 확인해주세요')
            return redirect('pirostagram:post_feed')  
    ctx = {
        'post' : post,
        'current_user' : user,
        'is_liked_post' : is_liked_post,
        'postlike_count' : post_count
    }
    return render(request, 'post_detail.html', context=ctx)


@csrf_exempt
def post_like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    request_user_id = req['request_user_id']

    post = Post.objects.get(id=post_id)
    user = User.objects.get(id=request_user_id)
    is_liked_post = post.postlike_set.filter(writer = user)
    print(is_liked_post)

    if is_liked_post.count() == 0:
        like = PostLike()
        like.writer = user
        like.post = post
        like.save()

    else:
        is_liked_post.delete()

    user.save()
    post.save()

    return JsonResponse({
        'id': post_id,
        'request_user_id' : request_user_id,
    })

@csrf_exempt
def comment_add_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    request_user_id = req['request_user_id']
    request_user_name = User.objects.get(id=request_user_id).username
    comment_content = req['text']

    post = Post.objects.get(id=post_id)
    user = User.objects.get(id=request_user_id)
    comment = Comment()
    comment.writer = user
    comment.post = post
    comment.content = comment_content
    comment.depth = 0
    comment.sequence = post.comment_set.all().count() + 1
    
    comment.save()
    user.save()
    post.save()

    return JsonResponse({
        'id': post_id,
        'request_user_name' : request_user_name,
        'text' : comment_content,
        'comment_id' : comment.id
    })


@csrf_exempt
def comment_delete_ajax(request):
    req = json.loads(request.body)
    comment_id = req['comment_id']
    comment = Comment.objects.get(id = comment_id)
    comment.delete()

    return JsonResponse({
        'comment_id' : comment_id
    })