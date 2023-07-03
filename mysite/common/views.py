from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm, ProfileForm
from common.models import Profile
from django.utils import timezone


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
def Profile_detail(request, profile_id):
    profile =get_object_or_404(Profile, pk=profile_id)
    context = {'profile': profile}
    return render(request, 'common/mypage1.html', context)

@login_required(login_url='common:login')
def Profile_update(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    if request.user != profile.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('common:mypage', profile_id=profile_id)

    if request.method == "POST":
        profile = ProfileForm(request.POST, instance=profile)
        if profile.is_valid():
            profile = profile.save(commit=False)
            profile.author = request.user
            profile.modify_date = timezone.now() # 수정일시 저장
            profile.save()
            return redirect('common:profile_detail', profile_id=profile_id)
    else:
        profile = ProfileForm(instance=profile)
    context = {'profile': profile}
    return render(request, 'common/test_profile.html', context)

# 참고 사이트
# https://parkhyeonchae.github.io/2020/03/30/django-project-13/
# https://github.com/ParkHyeonChae/django-reborn-web/blob/master/users/views.py

# from django.contrib.auth.forms import UserChangeForm
# from .choice import *
#
# class CustomCsUserChangeForm(UserChangeForm):
#     password = None
#     tel = forms.CharField(label='연락처', widget=forms.NumberInput(
#         attrs={'class': 'form-control', 'maxlength':'13', 'oninput':"maxLengthCheck(this)",}),
#     )
#     name = forms.CharField(label='이름', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'maxlength':'8',}),
#     )
#     student_id = forms.IntegerField(label='학번', widget=forms.NumberInput(
#         attrs={'class': 'form-control', 'maxlength':'8', 'oninput':"maxLengthCheck(this)",}),
#     )
#     grade = forms.ChoiceField(choices=GRADE_CHOICES, label='학년', widget=forms.Select(
#         attrs={'class': 'form-control',}),
#     )
#     circles = forms.ChoiceField(choices=CIRCLES_CHOICES, label='동아리', widget=forms.Select(
#         attrs={'class': 'form-control',}),
#     )
#
#     class Meta:
#         model = User()
#         fields = ['tel', 'name', 'student_id', 'grade', 'circles']

