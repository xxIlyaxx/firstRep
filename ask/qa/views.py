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
    return render(request, 'main.html', {
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
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def question(request, id):
    try:
        passedId = int(id)
    except ValueError:
        raise Http404

    try:
        question = Question.objects.get(id=passedId)
    except Question.DoesNotExist:
        raise Http404

    return render(request, 'question.html', {
        'question': question,
        'answers': Answer.objects.filter(question_id=passedId)
    })


def test(request, *args, **kwargs):
    return HttpResponse('OK')
