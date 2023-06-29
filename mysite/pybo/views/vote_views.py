from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import ArticleComment


@login_required(login_url='common:login')
def high_five(request, articleComment_id):

    articleComment = get_object_or_404(ArticleComment, pk=articleComment_id)
    if request.user == articleComment.author:
        messages.error(request, '본인의 글에는 하이파이브 불가능 합니다.')
    else:
        articleComment.high_five.add(request.user)
    return redirect('pybo:article_detail', article_id=articleComment.article.id)