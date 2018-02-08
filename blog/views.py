from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm

def post_list(request):
    return render(request, 'blog/post_list.html',{})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/blog/list')
    else:
        form = PostForm() #Wirting part

    return render(request, '이지호.html', {'form': form})
# Create your views here.
