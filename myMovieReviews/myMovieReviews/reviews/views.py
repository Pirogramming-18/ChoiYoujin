from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    # db의 모든 객체들을 가지고 와서 리스트화
    reviews = Post.objects.all()
    ctx = {'reviews' : reviews}
    return render(request, template_name='list.html', context = ctx)

# http request와 post의 index인 pk 받기
def post_detail(request, pk):
    # 해당 post 글만 가져오기
    review = Post.objects.get(id=pk)
    ctx = {'review' : review}

    return render(request, template_name= 'detail.html', context=ctx)

def post_create(request):
    if request.method == 'POST':
        # request를 보냈을 때 post 메소드 객체를 가져옴
        form = PostForm(request.POST)
        if form.is_valid(): # 이 폼이 유효한지 확인
            post = form.save()
            # list라는 url 가진 곳으로 이동
            return redirect('reviews:list')
    else:
        form = PostForm()
        ctx = {'form' : form}
        return render(request, template_name='post_form.html', context=ctx)

def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save()
            return redirect('reviews:detail', pk)
    else :
        form = PostForm(instance = post)
        ctx = {'form' : form}

        return render(request, template_name = 'post_form.html', context = ctx)

def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('reviews:list')