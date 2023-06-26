from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone

from ..forms import ArticleForm
from ..models import Article
@login_required(login_url='common:login')
def article_create(request):
    form = ArticleForm()
    if request.method =='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            aticle = form.save(commit=False)
            aticle.author = request.user
            aticle.create_date=timezone.now()
            aticle.save()
            return redirect('pybo:main')
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request,'pybo/article_form.html',context)

# @login_required(login_url='common:login')
# def question_modify(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     if request.user != question.author:
#         messages.error(request,'수정권한이 없습니다')
#         return redirect('pybo:detail',question_id=question.id)
#
#     if request.method == "POST":
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user
#             question.modify_date = timezone.now() #수정일시 저장
#             question.save()
#             return redirect('pybo:detail',question_id=question.id)
#     else:
#         form = QuestionForm(instance=question)
#     context = {'form':form}
#     return render(request,'pybo/question_form.html',context)
#
#
# @login_required(login_url='common:login')
# def question_delete(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     if request.user != question.author:
#         messages.error(request,'삭제권한이 없습니다.')
#         return redirect('pybo:detail', question_id=question.id)
#     question.delete()
#     return redirect('pybo:index')
