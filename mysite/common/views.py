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
            next_url = request.GET.get('next') or 'profile'
            login(request, user)
            return redirect('next_url')
    else:
        form = UserForm()
    return render(request, 'common/test_signup.html', {'form': form})


@login_required(login_url='common:login')
def profile(request):
    """ profile 생성 """
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            # post일때
            profile = Profile()
            # 업로드 이미지
            profile.images = request.FILES.get('images')
            # 작성일
            profile.create_date = timezone.now()
            # 작성한 유저
            profile.author = request.user
            profile.save()
            messages.add_message(request, '프로필 작성이 완료되었습니다.')
            return redirect('pybo:main')
    else:
        form = ProfileForm()
        context = { 'form':form }
        # get일때
        return render(request, 'common/test_profile.html')


@login_required(login_url='common:login')
def profile_update(request):
    user = get_object_or_404(User, pk=request.user.pk)
    """ profile 수정 """
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, 'common/test_profile.html')
        else:
            form = ProfileForm(instance=request.user.profile)
            context = { 'form': form }
            return render(request, 'common/profile_update.html', context)

@login_required
def mypage(request):
    return render(request, 'common/mypage.html')


