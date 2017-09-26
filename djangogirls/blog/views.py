from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def post_list(request):
    # post_list view가 published_date가 존재하는 Post목록만 보여주도록 수정
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        # posts key의 value는 QuerySet
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


# post_detail기능을 하는 함수를 구현
# 'post'라는 key로 Post.objects.first()에 해당하는 Post객체를 전달
# 탬플릿은 'blog/post_detail.html'을 사용

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist as err:
        return HttpResponse('No post', status=404)

    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)
