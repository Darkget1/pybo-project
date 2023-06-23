from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from common.forms import UserForm
from common.models import Profile

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/test_signup.html',{'form':form})


# Create your views here.

def update_profile(request,):
    if request.method == "POST":
        # 폼에서 데이터를 받아와 변수화시키기

        profile_img = request.FILES["input_file_img"]

        # 정보를 파일에 저장하기
        save_profile_img = Profile(
            profile_img=profile_img
        )
        save_profile_img.save()

    profile_img_list = Profile.objects.all()

    return render(request, "common/test_profile.html", context={
        "profile_img_list": profile_img_list})