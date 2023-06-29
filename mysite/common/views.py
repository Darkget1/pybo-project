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

# @login_required(login_url='common:login')
# def mypage(request):
#     author = Profile.objects.get()
#     if author.profile:
#         profile = author.profile
#         context = {'profile':profile}
#         return render(request, 'common/mypage.html', context)
#     else:
#         return redirect('common/test_profile', author.pk)

@login_required
def mypage(request):
    return render(request, 'common/mypage.html')

# def article_detail(request,article_id):
#     article = get_object_or_404(Article,pk=article_id)
#     profile_author_id= article.author_id
#     profile = Profile.objects.get(author_id=profile_author_id)
#     context={'article':article,'profile':profile}
#     return render(request,'pybo/article_detail.html',context)

@login_required(login_url='common:login')
def change(request, user_id):
    profile = get_object_or_404(Profile)
    if request.user != profile.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('common:profile')

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.author = request.user
            profile.modify_date = timezone.now()  # 수정일시 저장
            profile.save()
            return redirect('/')
    else:
        form = ProfileForm()
    return render(request, 'common/update_profile.html', {'form':form})


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



