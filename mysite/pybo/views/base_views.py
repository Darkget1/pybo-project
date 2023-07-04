from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q,Count
from ..models import Article,ArticleComment
from common.models import Profile



# Create your views here.


def main(request):
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')#검색어

    article_list = Article.objects.annotate(articlecomment_count=Count('articlecomment')).order_by('-articlecomment_count','-create_date')
    if kw:
        article_list = article_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw)  # 내용검색
        ).distinct()
    profile = Profile.objects
    #페이징 처리
    paginator = Paginator(article_list,3)#페이지당 1개씩 보이기
    page_obj = paginator.get_page(page)
    context = {'article_list': page_obj, 'profile':profile,'page':page,'kw':kw}


    return render(request,'index.html',context)


def article_index(request):
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')#검색어
    #조회
    # question_list = Question.objects.order_by('-create_date')


    article_list = Article.objects.order_by('-create_date')
    if kw:
        article_list = article_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw)  # 내용검색
        ).distinct()
    profile = Profile.objects
    #페이징 처리
    paginator = Paginator(article_list,3)#페이지당 1개씩 보이기
    page_obj = paginator.get_page(page)
    context = {'article_list': page_obj, 'profile':profile,'page':page,'kw':kw}

    return render(request, 'pybo/article_list.html' ,context)




