from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone

from ..forms import ArticleForm
from ..models import Article,ArticleComment
from common.models import Profile,User
@login_required(login_url='common:login')
def article_create(request):
    form = ArticleForm()
    if request.method =='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.create_date=timezone.now()
            article.profile = Profile.objects.get(author_id=request.user)
            article.save()
            return redirect('pybo:main')
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request,'pybo/article_form.html',context)

@login_required(login_url='common:login')
def article_modify(request,article_id):
    article = get_object_or_404(Article,pk=article_id)
    if request.user != article.author:
        messages.error(request,'수정권한이 없습니다')
        return redirect('pybo:detail',article_id=article.id)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.modify_date = timezone.now() #수정일시 저장
            article.save()
            return redirect('pybo:article_detail',article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    context = {'form':form}
    return render(request,'pybo/article_form.html',context)


@login_required(login_url='common:login')
def article_delete(request, article_id):
    article = get_object_or_404(Article,pk=article_id)
    if request.user != article.author:
        messages.error(request,'삭제권한이 없습니다.')
        return redirect('pybo:article_detail', article_id=article.id)
    article.delete()
    return redirect('pybo:article_list')

def article_detail(request,article_id):
    article = get_object_or_404(Article,pk=article_id)
    profile_author_id= article.author_id
    profile = Profile.objects.get(author_id=profile_author_id)

    #하이파이브한 유저 찾기
    #글쓴이가 추천(즉 하이파이브를 해줘야) 가능!!
    articleComment_highfive_list = ArticleComment.objects.filter(highfive=article.author)
    print(articleComment_highfive_list)
    #하이파이브한 유저와 request.user 판별
    highfive_number = 0
    for articleComment_highfive in articleComment_highfive_list:
        print(articleComment_highfive)
        if articleComment_highfive.author == request.user:
            highfive_number += 1
    #댓글 단유저 찾기

    comment_list = ArticleComment.objects.filter(article_id=article_id)

    comment_user_number = 0
    for comment in comment_list:
        if comment.author == request.user:
            comment_user_number += 1
    # highfive_user_list = articleComment.highfive.all()
    context={'article':article,'profile':profile,'highfive_number':highfive_number,'comment_user_number':comment_user_number}
    return render(request,'pybo/article_detail.html',context)
