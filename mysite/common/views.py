from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from common.forms import UserForm, ProfileForm
from common.models import Profile
from django.utils import timezone


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
            return redirect('main')
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
            # messages.add_message(request, '프로필 작성이 완료되었습니다.')
            profile.save()
            return redirect('main')
    else:
        form = ProfileForm()
        # get일때
    return render(request, 'common/test_profile.html', {'form': form})


# @login_required(login_url='common:login')
# def profile_update(request):
#     """ profile 수정 """
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             """ 현재 유저의 프로필을 가져오고 받은 값으로 프로필을 갱신한다 """
#             old_profile = request.user.profile
#             old_profile.images = form.cleaned_data['images']
#             old_profile.img_date = form.cleaned_data['img_date']
#             old_profile.birthdate = form.cleaned_data['birthdate']
#             old_profile.mbti = form.cleaned_data['mbti']
#             old_profile.workout = form.cleaned_data['workout']
#             old_profile.introduce = form.cleaned_data['introduce']
#             old_profile.url = form.cleaned_data['url']
#             old_profile.save()
#             messages.success(request, '프로필을 수정/저장했습니다.')
#             return redirect('profile_update')
#         elif request.method == "GET":
#             form = ProfileForm(instance=request.user)
#             context = { 'form': form }
#             return render(request, 'common/test_profile.html', context)
#
# @login_required
# def mypage(request):
#     return render(request, 'common/mypage.html')


