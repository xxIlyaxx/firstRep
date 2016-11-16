from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.


def test(request, *args, **kwargs):
    return HttpResponse('OK')
