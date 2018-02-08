from django.forms import ModelForm
from .models import Feedback

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['id', 'name', 'email', 'comment']