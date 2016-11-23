from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from qa.models import *


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title == u'':
            raise forms.ValidationError('Field is not filled')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == u'':
            raise forms.ValidationError('Field is not filled')
        return text

    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(author=self._user, **self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == u'':
            raise forms.ValidationError('Field is not filled')
        return text

    def clean_question(self):
        try:
            question = Question.objects.get(id=self.cleaned_data['question'])
        except Question.DoesNotExist:
            raise forms.ValidationError('The question does not exist')
        return question.id

    def clean(self):
        return self.cleaned_data

    def save(self):
        answer = Answer(author=self._user, text=self.cleaned_data['text'], question_id=self.cleaned_data['question'])
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == u'':
            raise forms.ValidationError('Field is not filled')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if email == u'':
            raise forms.ValidationError('Field is not filled')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == u'':
            raise forms.ValidationError('Field is not filled')
        return password

    def clean(self):
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == u'':
            raise forms.ValidationError('Field is not filled')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == u'':
            raise forms.ValidationError('Field is not filled')
        return password

    def clean(self):
        user = authenticate(**self.cleaned_data)
        if user is None:
            raise forms.ValidationError('Username/password does not exist')
        return self.cleaned_data

    def login(self, request):
        user = authenticate(**self.cleaned_data)
        login(request, user)
        return user
