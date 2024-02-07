from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post

CustomUser = get_user_model()


def create_post(request, user_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = CustomUser.objects.get(pk=user_id)  # 현재 로그인한 사용자를 가져옵니다.
        new_post = Post.objects.create(title=title, content=content, author=author, created_at=timezone.now())
        # 게시글 작성 후, 해당 글의 상세 페이지로 이동하도록 redirect
        return redirect('post_detail', post_id=new_post.id)
    else:
        return render(request, 'pages/create_post.html')


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'pages/post_detail.html', {'post': post})

def board(request):
    posts = Post.objects.all()
    return render(request, 'pages/board.html', {'posts': posts})


def home(request):
    return render(request, 'pages/home.html')
