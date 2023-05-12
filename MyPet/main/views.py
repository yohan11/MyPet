from django.shortcuts import render, redirect


from .forms import FileUploadForm
from .models import Post
from django.core.files.storage import FileSystemStorage

# Create your views here.



def feed(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'feed.html', {'postlist':postlist})

def upload(request):
    return render(request,'upload.html')

def inputform(request):
    if request.method == 'POST' :
        username = None
        if request.user.is_authenticated:
            username = request.user
        user_id=username
        description = request.POST['input-description']
        img = request.FILES["input-img"]
        fileupload = Post(
            user_id=user_id,
            description=description,
            img=img,
        )
        fileupload.save()
        

    return redirect('feed')