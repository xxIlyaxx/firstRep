from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
# from ask.qa.models import *
# from ask.qa.forms import *
from qa.models import *
from qa.forms import *

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

    form = AnswerForm(initial={'question_id': passedId})


    return render(request, 'question.html', {
        'question': question,
        'answers': Answer.objects.filter(question_id=passedId),
        'form': form,
    })


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect('/question/' + str(question.id) + '/')
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form,
    })


def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect('/question/' + str(answer.question_id) + '/')
    return HttpResponseRedirect('/')


def test(request, *args, **kwargs):
    return HttpResponse('OK')
