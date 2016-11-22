from django import forms
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
        question = Question(**self.cleaned_data)
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
        answer = Answer(text=self.cleaned_data['text'], question_id=self.cleaned_data['question'])
        answer.save()
        return answer