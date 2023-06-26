from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q,Count


# Create your views here.


def main(request):
    return render(request,'pybo/main.html',)


def article_detail(request,question_id):
    page = request.GET.get('page', '1')
    #request에서 숫자를 호출받는다 ...
    # question=Question.objects.get(id=question_id)
    question = get_object_or_404(Question,pk=question_id)
    #페이징을 위한 index
    answer_list = question.answer_set.order_by('-voter','-create_date')
    #페이징 처리
    paginator = Paginator(answer_list,1)#페이지당 1개씩 보이기
    page_obj = paginator.get_page(page)


    #get_object(Question)=> Question.object.get의 의미
    context={'question':question,'answer_list': page_obj}
    return render(request,'pybo/question_detail.html',context)