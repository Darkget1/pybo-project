from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q,Count
from ..models import Article
from common.models import Profile



# Create your views here.


def main(request):
    return render(request,'index.html',)


def article_index(request):
    page = request.GET.get('page','1')
    # article.profile.objects.set_all
    article_list = Article.objects.order_by('-voter','create_date')
    profile = Profile.objects
    #페이징 처리
    paginator = Paginator(article_list,3)#페이지당 1개씩 보이기
    page_obj = paginator.get_page(page)
    context = {'article_list': page_obj, 'profile':profile}

    return render(request, 'pybo/article_list.html' ,context)

# def article_detail(request,question_id):
#     page = request.GET.get('page', '1')
#     #request에서 숫자를 호출받는다 ...
#     # question=Question.objects.get(id=question_id)
#     question = get_object_or_404(Question,pk=question_id)
#     #페이징을 위한 index
#     answer_list = question.answer_set.order_by('-voter','-create_date')
#     #페이징 처리
#     paginator = Paginator(answer_list,1)#페이지당 1개씩 보이기
#     page_obj = paginator.get_page(page)
#
#
#     #get_object(Question)=> Question.object.get의 의미
#     context={'question':question,'answer_list': page_obj}
#     return render(request,'pybo/question_detail.html',context)