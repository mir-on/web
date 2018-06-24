from django.http import HttpResponse, Http404

from django.core.paginator import Paginator
from qa.models import Question
from django.shortcuts import render


def test(request, *args, **kwargs):
    print('xxx')
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 50:
        limit = 10
    print("limit = %d" % limit)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def new(request):
    dir(request)
    print("===========================")
    qs = Question.objects.new()
    print("qs len = %d" % (len(qs)))
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    print("no = %d" % page)
    paginator = Paginator(qs, 10)
    baseurl = '/?page='
    p = paginator.page(page)
    print(paginator.page_range)
    range = paginator.page_range
    print(paginator.num_pages)
    print("page number = %d" % p.number)
    x = render(request, 'ask/new.html', {
        'paginator': paginator,
        'questions': p.object_list,
        'page': p,
        'baseurl': baseurl,
    })
    print("===========================")
    print(x)
    print(x.content)
    return x

