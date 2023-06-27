from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from common.forms import UserForm
from common.models import Profile
from django.utils import timezone


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = UserForm()
    return render(request, 'common/test_signup.html',{'form':form})

@login_required(login_url='common:login')
def profile(request):
    if request.method == 'POST':
        #post일때
        profile = Profile()
        #업로드 이미지
        profile.images = request.FILES.get('images')
        #작성일
        profile.create_date = timezone.now()
        #작성한 유저
        profile.author = request.user
        profile.save()
        return redirect('pybo:main')
    else:
        #get일때
        return render(request, 'common/test_profile.html')
