from django.shortcuts import render
from .models import Post

# Create your views here.



def feed(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'feed.html', {'postlist':postlist})


def upload(request):
    return render(request,'upload.html')