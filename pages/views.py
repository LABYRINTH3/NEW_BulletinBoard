from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post

CustomUser = get_user_model()


@login_required
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



def delete(request, id):
    delete_blog = Post.objects.get(id=id)
    delete_blog.delete()
    return redirect('board')


@login_required
def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'pages/edit.html', {'post': edit_post})

@login_required
def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    # update_post.author = request.POST['author']
    update_post.content = request.POST['content']
    update_post.created_at = timezone.now()
    update_post.save()
    return redirect('post_detail', update_post.id)
