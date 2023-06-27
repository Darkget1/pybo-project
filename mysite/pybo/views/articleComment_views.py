from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect,resolve_url
from django.utils import timezone

from ..forms import ArticleCommentForm
from ..models import Article, ArticleComment

@login_required(login_url='common:login')
def articleComment_create_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            articleComment = form.save(commit=False)
            articleComment.author = request.user
            articleComment.create_date = timezone.now()
            articleComment.article = article
            articleComment.save()
            return redirect('{}#ArticleComment_{}'.format(resolve_url('pybo:article_detail', article_id=articleComment.article.id)
                                                   , articleComment.id))
    else:
        form = ArticleCommentForm()
    context = {'form':form}
    return render(request, 'pybo/articleComment_form.html',context)


@login_required(login_url='common:login')
def articleComment_modify_article(request, articleComment_id):
    articleComment = get_object_or_404(ArticleComment, pk=articleComment_id)
    if request.user != articleComment.author:
        messages.error(request,'댓글수정권한이 없습니다')
        return redirect('pybo:detail',article_id=articleComment.question.id)

    if request.method == "POST":
        form = ArticleCommentForm(request.POST,instance=articleComment)
        if form.is_valid():
            articleComment = form.save(commit=False)
            articleComment.author = request.user
            articleComment.modify_date = timezone.now()
            articleComment.save()
            return redirect('{}#ArticleComment_{}'.format(resolve_url('pybo:article_detail', article_id=articleComment.article.id)
                                                   , articleComment.id))
    else:
        form = ArticleCommentForm()
    context = {'form':form}
    return render(request, 'pybo/articleComment_form.html',context)

@login_required(login_url='common:login')
def articleComment_delete_article(request,articleComment_id):
    articleComment = get_object_or_404(ArticleComment,pk=articleComment_id)
    if request.user != articleComment.author:
        messages.error(request, '댓글삭제권한이 없습니다.')
        return redirect('pybo:article_detail',article_id=articleComment.article_id)
    else:
        articleComment.delete()
    return redirect('pybo:article_detail',article_id=articleComment.article.id)