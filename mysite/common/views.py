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
            return redirect('index')
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
            # profile = Profile()
            # 업로드 이미지
            profile.images = request.FILES.get('images')
            # 작성일
            profile.create_date = timezone.now()
            # 작성한 유저
            profile.author = request.user
            # profile.birthdate = form.cleaned_data.get('birthdate')
            # profile.mbti = form.cleaned_data.get('mbti')
            # profile.workout = form.cleaned_data.get('workout')
            # profile.introduce = form.cleaned_data.get('introduce')
            # profile.url = form.cleaned_data.get('url')
            # messages.add_message(request, '프로필 작성이 완료되었습니다.')
            profile.save()
            return redirect('pybo:main')
    else:
        form = ProfileForm()
        # get일때
        return render(request, 'common/test_profile.html', {'form': form})


@login_required(login_url='common:login')
class profile_update(UpdateView):
    model = Profile
    contex_object_name = 'target_profile'
    form_class = ProfileForm
    success_url = reverse_lazy("common:")

# def profile_update(request, user):
#     """ profile 수정 """
#     profile = get_object_or_404(Profile, pk=user)
#     if request.user != profile.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:main')
#
#     if request.method == "POST":
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             """ 현재 유저의 프로필을 가져오고 받은 값으로 프로필을 갱신한다 """
#             old_profile = form.save(commit=False)
#             old_profile.author = request.user
#             old_profile.modify_date = timezone.now() # 수정일시 저장
#             old_profile.save()
#             messages.success(request, '프로필을 수정/저장했습니다.')
#             return redirect('profile_update')
#         else:
#             form = ProfileForm(instance=request.user)
#             context = {'form': form}
#             return render(request, 'common/mypage', context)
#
# @login_required
# def mypage(request):
#     return render(request, 'common/mypage.html')
#
#
