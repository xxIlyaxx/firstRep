from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
# from ask.qa.models import *
from qa.models import *

# Create your views here.


def main(request):
    questions = Question.objects.new()
    limit = 10
    try:
        pageNumber = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(pageNumber)
    return render(request, 'qa/main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def popular(request):
    questions = Question.objects.popular()
    limit = 10
    try:
        pageNumber = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(pageNumber)
    return render(request, 'popular.html', {
    })

def question(request, id):
    pass


def test(request, *args, **kwargs):
    return HttpResponse('OK')
