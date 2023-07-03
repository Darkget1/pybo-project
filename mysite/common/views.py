from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm, ProfileForm
from common.models import Profile, User
from django.utils import timezone
from pybo.models import ArticleComment,Article
from datetime import datetime


def index(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # next_url = request.GET.get('next') or 'profile'
            login(request, user)
            return redirect('common:profile')
    else:
        form = UserForm()
    return render(request, 'common/test_signup.html', {'form': form})


@login_required(login_url='common:login')
def profile(request):
    """ profile 생성 """

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # post일때
            # 업로드 이미지
            profile.images = request.FILES.get('images')
            # 작성일
            profile.create_date = timezone.now()
            # 작성한 유저
            profile.author = request.user
            profile.save()
            # messages.add_message(request, '프로필 작성이 완료되었습니다.')
            return redirect('main')
    else:
        form = ProfileForm()
        # get일때
    return render(request, 'common/test_profile.html', {'form': form})

@login_required(login_url='common:login')
def Profile_detail(request):
    articlecomment=get_object_or_404(Article,author=request.user)
    article=get_object_or_404(Article,author=request.user)
    user = get_object_or_404(User,username=request.user)
    print(user.author_article)
    profile =get_object_or_404(Profile, author=request.user)
    context = {'profile': profile,'articlecomment':articlecomment,'article':article,'user':user}
    return render(request, 'common/mypage1.html', context)
#수정중
@login_required(login_url='common:login')
def Profile_update(request,profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)

    if request.user != profile.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('common:mypage',profile_id=profile.id)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            if request.FILES.get('images') is None:
                messages.error(request, '이미지가 없습니다.')
                return redirect('common:profile_update',profile_id=profile.id)
            profile.images = request.FILES.get('images')


            profile.author = request.user
            profile.save()
            return redirect('common:mypage')
    else:
        form = ProfileForm(instance=profile)


    context = {'form': form}
    return render(request, 'common/test_profile.html', context)
