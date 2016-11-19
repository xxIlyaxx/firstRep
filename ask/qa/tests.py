from django.test import TestCase

# Create your tests here.
#
#
# class TestQuestion(unittest.TestCase):
#     def test_question(self):
#         from qa.models import Question
#         try:
#             title = Question._meta.get_field('title')
#         except FieldDoesNotExist:
#             assert False, "title field does not exist in Question model"
#         assert isinstance(title, CharField), "title field is not CharField"
#         try:
#             text = Question._meta.get_field('text')
#         except FieldDoesNotExist:
#             assert False, "text field does not exist in Question model"
#         assert isinstance(text, TextField), "text field is not TextField"
#         try:
#             added_at = Question._meta.get_field('added_at')
#         except FieldDoesNotExist:
#             assert False, "added_at field does not exist in Question model"
#         assert isinstance(text, DateField) or isinstance(added_at, DateField), "added_at field is not DateTimeField"
#         try:
#             rating = Question._meta.get_field('rating')
#         except FieldDoesNotExist:
#             assert False, "rating field does not exist in Question model"
#         assert isinstance(rating, IntegerField), "text field is not IntegerField"
#         try:
#             author = Question._meta.get_field('author')
#         except FieldDoesNotExist:
#             assert False, "author field does not exist in Question model"
#         assert isinstance(author, ForeignKey), "author field is not ForeignKey"
#         assert author.related.parent_model == User, "author field does not refer User model"
#         try:
#             likes = Question._meta.get_field('likes')
#         except FieldDoesNotExist:
#             assert False, "likes field does not exist in Question model"
#         assert isinstance(likes, ManyToManyField), "likes field is not ManyToManyField"
#         assert likes.related.parent_model == User, "likes field does not refer User model"
#         user, _ = User.objects.get_or_create(username='x', password='y')
#         try:
#             question = Question(title='qwe', text='qwe', author=user)
#             question.save()
#         except:
#             assert False, "Failed to create question model, check db connection"
