from django import forms
from .models import Comment
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('description',)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = 'blog:index'
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
